from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from utils import get_timezone
scheduler = BackgroundScheduler()
scheduler.start()

def send_mail(email_address, country):
    print(f"Mail Successfully Sent to {email_address} at {datetime.now(get_timezone(country))}")

def send_sms(phone_number, country, message):
    import requests
    url = "https://api.txtbox.in/v1/sms/send"
    payload = "mobile_number="+str(phone_number)+"&sms_text="+str(message)+"&sender_id=market"
    headers = {
    'apiKey': "9f81fddf27be1aa3e73a0619392cbc0c",
    'content-type': "application/x-www-form-urlencoded",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    print(f"Text Successfully Sent to {phone_number} at {datetime.now(get_timezone(country))}")