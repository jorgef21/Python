"""
Features:
 Perform automated rowcount testing from OracleDB source and Snowflake Cloud DW
 Parametrized table input
 Notifications to MS Teams using webwooks 

Instructions:
- Use CSV file as tablename input
- Need to add a file settigns.py with conn strings
  oracle_conn_string = ''         full OracleDB conn string
  snf_user = ''		          Snowflake User
  snf_password= ''		  Snowflake pw
  teams_webhook = ''		  Teams channel webhook
"""
import os
import sys
import platform
import cx_Oracle
import snowflake.connector
import csv
import pymsteams
from settings import oracle_conn_string,snf_user,snf_password,teams_webhook

#Global Variables
myTeamsMessage = pymsteams.connectorcard(teams_webhook)
query = 'SELECT COUNT(0) FROM '
count_oracle = 0 
count_snf = 0
executed = 0
passed = 0
failed = 0
rest = 0
error_table = []
file = ''

def db_init_connect():
# SNOWFLAKE CONNECTION
  con = snowflake.connector.connect(
      user=snf_user,
      password=snf_password,
      account='laureate',
      warehouse='ETL_WAREHOUSE',
      database='BI_CDW_PROD',
      schema='UPN_STG_SIS_BNRODS_ODSMGR',
      role = 'BI_READ'
    )
  cur = con.cursor()
  cur.execute('SELECT current_version()')
  one_row = cur.fetchone()

  # ORACLE CONNCTION
  conn = cx_Oracle.connect(oracle_conn_string)
  cursor = conn.cursor()
  print('Welcone, Oracle Version: '+conn.version)
  print('Snowflake Version: '+one_row[0])

def db_close_conn():
  cursor.close()            
  cur.close()

def row_count_test():
  Section1 = pymsteams.cardsection()
  if (sys.argv[1]=='composite'):
  file='/home/informatica/test/composite_tables.csv'
  Section1.title('Composite Tables test summary: ')
  elif (sys.argv[1]=='loe'):
  file='/home/informatica/test/loe_tables.csv'
  Section1.title('LOE Tables test summary: ')

  with open (file,'r') as csvfile:
     reader = csv.reader(csvfile,delimiter=',')
     for row in reader:
         cursor.execute(query+row[0])
         cur.execute(query+row[0])
         count_oracle = cursor.fetchone()[0]
         count_snf =cur.fetchone()[0]
         rest = int(count_oracle)-int(count_snf)
         if (rest==0): 
            executed += 1
            passed += 1
            print(row[0]+'==================> TEST PASSED :) !')
         else:
            failed += 1
            executed += 1 
            error_table.append(row[0])
            print(row[0]+'==================> TEST FAILED :( !'+'   ORACLE ROWCOUNT: '+str(count_oracle)+' SNOWFLAKE ROWCOUNT: '+str(count_snf)+'   DIFF: '+str(rest))
     print('\n Test executed: '+str(executed)+' Passed: '+str(passed)+' Failed: '+str(failed))

def teams_notification():
#SEND NOTIFICATION TO TEAMS
  Section1.text('Test Executed: '+str(executed)+'  Passed: '+str(passed)+'  Failed: '+str(failed))
  #Section 2
  Section2 = pymsteams.cardsection()
  Section2.title('Tables with errors: ')
  Section2.text(" | ".join(error_table))

  if error_table:
      myTeamsMessage.color('990000')
  else:
      myTeamsMessage.color('56e16d')
      
  myTeamsMessage.title('Oracle-SNF Data check')
  myTeamsMessage.addSection(Section1)
  myTeamsMessage.addSection(Section2)
  myTeamsMessage.summary('done!')
  myTeamsMessage.send()

if if __name__ == "__main__":
    """
     Initiate connection
     Run test
     Close connection
     Send  notification to teams webwook
    """
  db_init_connect()
  row_count_test()
  teams_notification()
  db_close_conn()  
