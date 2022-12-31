import pandas as pd
from validators import validate_email, validate_sms, validate_duplicates
from io import TextIOWrapper
from worker import scheduler, send_mail, send_sms
from datetime import datetime

DATA_FILE_PATH = "./data.csv"
OUTPUT_FILE_PATH = "./output.txt"

def start_process(data: pd.DataFrame, output_file: TextIOWrapper) -> None:
    cache = {}
    for row_number in range(len(data)):
        row = data.iloc[row_number]

        message = row["Message"]
        country = row["Country"]
        if pd.notna(row["Email"]):
            try:
                email_address = row["Email"]
                # First validate Email
                validate_email(email_address)

                # validate for duplicates
                validate_duplicates(email_address, message, cache)

                # check here for future date and schedule message
                if pd.notna(row["Schedule On"]):
                    schedule_date: str = row["Schedule On"]
                    day, month, year = schedule_date.split("-")
                    schedule_date = datetime(int(year), int(month), int(day))
                    if schedule_date < datetime.today():
                        raise Exception("Invalid Schedule Date")
                    scheduler.add_job(send_mail, 'date', run_date=schedule_date, args=[email_address, country])
                else:
                    send_mail(email_address, country)

                ## if email send is successful, add email into cache
                if cache.get(email_address):
                    cache[email_address].append(message)
                else:
                    cache[email_address] = [message]

                output_file.write(f"Success. Type: Email, ID: {row_number} \n")
            except Exception as e:
                output_file.write(f"Failure. Type: Email, ID: {row_number}, Reason: {e} \n")


        if pd.notna(row["Phone"]):
            try:
                phone_number = row["Phone"]

                # validate sms
                validate_sms(message, phone_number, country)

                # validate for duplicates
                validate_duplicates(phone_number, message, cache)

                # check here for future date and schedule message
                if pd.notna(row["Schedule On"]):
                    schedule_date: str = row["Schedule On"]
                    day, month, year = schedule_date.split("-")
                    schedule_date = datetime(int(year), int(month), int(day))
                    if schedule_date < datetime.today():
                        raise Exception("Invalid Schedule Date")
                    scheduler.add_job(send_sms, 'date', run_date=schedule_date, args=[phone_number, country, message])
                else:
                    send_sms(phone_number, country, message)

                # if text send is successful, add phone number into cache
                if cache.get(phone_number):
                    cache[phone_number].append(message)
                else:
                    cache[phone_number] = [message]
                

                output_file.write(f"Success. Type: Text, ID: {row_number} \n")
            except Exception as e:
                output_file.write(f"Failure. Type: Text, ID: {row_number}, Reason: {e} \n")


if __name__ == "__main__":
    data = pd.read_csv(DATA_FILE_PATH)
    output_file = open(OUTPUT_FILE_PATH, "a")

    start_process(data, output_file)

    output_file.close()
