#!/bin/bash

read -p "Enter EMAIL: " email
read -p "Enter PASSWORD: " password
read -p "Confirm EMAIL or PASSWORD? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

gmail='**'$email'**'
gmail_password='**'$password'**'

export mail=gmail
export password=gmail_password

export FLASK_APP=run.py
flask run
