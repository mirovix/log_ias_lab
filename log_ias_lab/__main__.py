import os
import sys

import datetime
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from log_ias_lab.log_lab import LogLab


def get_italian_holidays():
    url = "https://date.nager.at/Api/v2/PublicHolidays"
    year = datetime.datetime.now().year
    country_code = "IT"  # Italy

    response = requests.get(f"{url}/{year}/{country_code}")
    holidays_list = []

    if response.status_code == 200:
        for holiday in response.json():
            holiday_date = holiday['date']
            holidays_list.append(holiday_date[5:10])
    else:
        holidays_list = ['01-01', '01-06', '04-25', '05-01', '08-15', '11-01', '12-08', '12-25', '12-26']

    return holidays_list


if __name__ == '__main__':
    username = os.environ.get('DEI_USER')
    password = os.environ.get('DEI_PASSWORD')
    laboratory = os.environ.get('DEI_LAB_NAME', "DEI/O | SSL Lab")
    print(f"Logging in as {username} to {laboratory}")

    today = datetime.datetime.now()
    today_str = today.strftime("%d-%m")

    holidays = get_italian_holidays()

    if today.weekday() >= 5:
        print("Today is a weekend. Skipping the script.")
        sys.exit()

    if today_str in holidays:
        print(f"Today is a holiday ({today_str}). Skipping the script.")
        sys.exit()

    log_lab = LogLab(username=username, password=password, laboratory_name=laboratory)
    log_lab.run()
