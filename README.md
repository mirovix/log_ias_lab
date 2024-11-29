# Log automatically to DEI Ias Lab

This script allows you to log automatically to the DEI Ias Lab.

## Installation
```bash
mkdir ~/log_ias_lab
cd ~/log_ias_lab
git clone https://github.com/mirovix/log_ias_lab.git
```

## Configure
```bash
cd ~/log_ias_lab/log_ias_lab
python3 -m pip install -r requirements.txt
echo 'export DEI_USER="tuo_username"' >> ~/.bashrc && source ~/.bashrc
echo 'export DEI_PASSWORD="tua_password"' >> ~/.bashrc && source ~/.bashrc
echo 'export DEI_LAB_NAME="DEI/O | SSL Lab"' >> ~/.bashrc && source ~/.bashrc
```

## Usage
```bash
cd ~/log_ias_lab/log_ias_lab
python3 log_ias_lab
```

## Usage ad Service that runs at 08.00
```bash
(crontab -l; echo "0 8 * * * /bin/bash -i -c 'source $HOME/.bashrc && cd $HOME/log_ias_lab/ && python3 log_ias_lab >> $HOME/log_ias_lab.log 2>&1'") | crontab -
```
