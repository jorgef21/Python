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
For windows download Oracle instantclient and use the variables LOCATION = r"C:\instantclient_19_3"
  os.environ['PATH'] = LOCATION + ';' + os.environ['PATH'
  Run: python data_row_count_test.py tables_context ie: sales
"""
import os
import sys
import platform
import cx_Oracle
import snowflake.connector
import csv
import pymsteams
from settings import oracle_conn_string,snf_user,snf_password,teams_webhook


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
snf_version = cur.fetchone()

# ORACLE CONNCTION
LOCATION = r"C:\instantclient_19_3"
os.environ['PATH'] = LOCATION + ';' + os.environ['PATH']
conn = cx_Oracle.connect(oracle_conn_string)
cursor = conn.cursor()
print('Welcone, Oracle Version: '+conn.version)
print('Snowflake Version: '+snf_version[0])

def row_count_test():
   #Variables
  count_oracle = 0 
  count_snf = 0
  passed = 0
  failed = 0
  rest = 0
  myTeamsMessage = pymsteams.connectorcard(teams_webhook)
  Section1 = pymsteams.cardsection()
  Section2 = pymsteams.cardsection()
  executed = 0
  passed = 0
  failed = 0 
  error_table = []
  file = ''
  
  if len(sys.argv)>1:
    if (sys.argv[1]=='sales'):
      file='./sales.csv'
      Section1.title('Sales Tables test summary: ')
    elif (sys.argv[1]=='customers'):
      file='./customer.csv'
      Section1.title('Customer Tables test summary: ')
  else:
    print('No Parameter')

  if file != '':
    with open (file,'r') as csvfile:
      query = 'SELECT COUNT(0) FROM '
      reader = csv.reader(csvfile,delimiter=',')
      for row in reader:
          cursor.execute(query+row[0]) #add table name from csv
          cur.execute(query+row[0])   #add table name from csv
          count_oracle = cursor.fetchone()[0] #cursor result
          count_snf =cur.fetchone()[0]
          rest = int(count_oracle)-int(count_snf)
          if (rest==0): 
              executed = executed+1
              passed = passed+1
              print(row[0]+'==================> TEST PASSED :) !')
          else:
              failed += 1
              executed += 1 
              error_table.append(row[0])
              print(row[0]+'==================> TEST FAILED :( !'+'   ORACLE ROWCOUNT: '+str(count_oracle)+' SNOWFLAKE ROWCOUNT: '+str(count_snf)+'   DIFF: '+str(rest))
      print('\n Test executed: '+str(executed)+' Passed: '+str(passed)+' Failed: '+str(failed))
      #Send notification
      Section1.text('Test Executed: '+str(executed)+'  Passed: '+str(passed)+'  Failed: '+str(failed))
      #Section 2
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
  else:
      print('No file')

if __name__ == "__main__":
    """
     Initiate connection
     Run test
     Close connection
     Send  notification to teams webwook
    """ 
    row_count_test()
    cursor.close()            #close oracle conn
    cur.close()               #close snowflake conn