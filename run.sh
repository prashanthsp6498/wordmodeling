#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'


file='.auth.json'
if [ -r $file ]
then
    printf "\n${GREEN}AUTHENTICATION FILE EXISTS${NC}\n\n\n\n"
    email=`jq '.mail' .auth.json`
    password=`jq '.password' .auth.json`

else
    printf "\n${RED}AUTHENTICATION FILE DOES NOT EXIST${NC}\n${GREEN}Creating AUTH file${NC}\n\n"
    read -p "Enter EMAIL: " email
    read -p "Enter PASSWORD: " password
    read -p "Confirm EMAIL or PASSWORD? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
    printf '{\n\t"mail":"%s",\n\t"passowrd":"%s"\n}' $email $password >> .auth.json
fi


gmail='**'$email'**'
gmail_password='**'$password'**'

export mail=gmail
export password=gmail_password

export FLASK_APP=run.py
flask run
