from typing import Any
import re
from datetime import datetime
from utils import get_timezone
from exceptions import *

def validate_email(email: Any) -> None:
    email_valid_pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if not re.match(email_valid_pattern, email):
        raise InvalidEmail("Invalid Email address. Email should be in the form of name@example.com")


def validate_message(message: Any) -> None:
    message_length = len(message)
    if message_length <= 1 or message_length > 160:
        raise InvalidMessage(
            f"Message length should be >1 and <=160. Your message has length of {message_length}")


def validate_phone_number(phone_number: Any) -> None:
    try:
        phone_number = int(phone_number)
    except ValueError:
        raise InvalidPhoneNumber("Phone Number should be Integer Only")

    phone_number_length = len(str(phone_number))
    if phone_number_length != 10:
        raise InvalidPhoneNumber(
            f"Phone Number length should be 10. Your Phone Number has length of {phone_number_length}")

def validate_hours(country: Any) -> None:
    current_time = None
    time_zone = get_timezone(country)
    current_time = int(datetime.now(time_zone).strftime('%H'))
    
    if current_time < 10 or current_time > 17:
        raise InvalidHours(
            f"Message can only be sent between 10AM to 5PM. Your timing is {current_time} hours"
        )

def validate_sms(message, phone_number, country):
    # try:
    validate_message(message)
    validate_phone_number(phone_number)
    validate_hours(country)
    # except ValueError:
    #     raise InvalidSMS("Message constraints not satisfied.")
    
# def check_duplicate_email(email, message,dict_email) -> None:
#     if email in dict_email:
        
#         list_msg = dict_email[email]
#         for msg in list_msg:
#             if message == msg:
#                 raise CheckDuplicateEmail(
#             f"Duplicate message detected for {email}")
#             else:
#                 dict_email[email].append(message)
#                 print(dict_email)

#     else:
#         dict_email[email] = []
#         dict_email[email].append(message)

# def check_duplicate_sms(phone_number, message,dict_sms) -> None:
#     if phone_number in dict_sms:
        
#         list_msg = dict_sms[phone_number]
#         for msg in list_msg:
#             if message == msg:
#                 raise CheckDuplicateSMS(
#             f"Duplicate message detected for {phone_number}")
#             else:
#                 dict_sms[phone_number].append(message)

#     else:
#         dict_sms[phone_number] = []
#         dict_sms[phone_number].append(message)


def validate_duplicates(key: str, message: str, cache: dict):
    if key in cache and message in cache[key]:
        raise DuplicateMessage(f"Duplicate Message found for {key}")
