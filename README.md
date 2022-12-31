# Assignment_SMS_Magic
This program is written to send Text Message and Email by reading fields - Message, email id, phone number and Country from a given CSV file "data.csv".

### Project Requirements:
- Python 3.8.10

### Steps for setting up the project in local

1. Clone GitHub Repo: [https://github.com/Shreya412/Assigment_SMS_magic.git](https://github.com/Shreya412/Assigment_SMS_magic.git)
2. Create Virtual Env: ` python -m venv venv `
3. Activate venv: `source venv/bin/activate`(Linux) and `venv\Scripts\activate`(Windows)
4. Download dependencies: `pip install -r requirements.txt`
5. Run main.py which contains driver code for sending email. SMS or both

### Documentation:

main.py:
- driver code for sending Email, SMS or both.

output.txt:
- an output file containing success/failure and reason for failure along with row_number

validators.py:
- collection of all validators function.
```
def validate_email()          #for email validation
def validate_message()        #for message validation 
def validate_phone_number()   #for phone_number validation
def validate_hours()          #for hours validation
def validate_sms()            #agrregate function for validating message length, phone_number, hour timings for respective country
def validate_duplicates()     #for duplicate messsage validation
```

exceptions.py:
- collection of all necessary exceptions which needs to be thrown at the time of error

utils.py:
- collection of function for checking time for different timezone

workers.py:
- contains schedular function for sending Email as well as SMS.
- for sending real time SMS https://api.sms-magic.com/doc/#api-Send_SMS-Send_SMS___post API is used.
