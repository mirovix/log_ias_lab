import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from log_ias_lab.log_lab import LogLab

if __name__ == '__main__':
    username = os.environ.get('DEI_USER')
    password = os.environ.get('DEI_PASSWORD')
    laboratory = os.environ.get('DEI_LAB_NAME', "DEI/O | SSL Lab")
    print(f"Logging in as {username} to {laboratory}")
    log_lab = LogLab(username=username, password=password, laboratory_name=laboratory)
    log_lab.run()
