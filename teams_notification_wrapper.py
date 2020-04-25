"""
Wrapper to send notifications to Teams Channels

- Export settings from settings.py, need to create a file with teams_webhook
- Takes Job name from ENV variable job_name
"""
import pymsteams
import os
import pytz
from datetime import datetime
from settings import teams_webhook


myTeamsMessage = pymsteams.connectorcard(teams_webhook)
current_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
current_date_et = datetime.now()
current_date_peru = current_date_et.astimezone(pytz.timezone('America/Lima'))
peru_time_format = current_date_peru.strftime("%Y-%m-%d %H:%M:%S")
job_name = os.environ['job_name']

def send_teams_notification(job_name):
    myTeamsMessage.title(job_name)
    myTeamsMessage.text('Job '+job_name+' completed at: '+peru_time_format)
    myTeamsMessage.send()

def main():
    send_teams_notification(job_name)

if __name__ == "__main__":
    main()