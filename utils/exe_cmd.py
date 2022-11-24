from __future__ import print_function, unicode_literals

import json
import os
import sys
from pprint import pprint

from dotenv import load_dotenv
from PyInquirer import print_json, prompt

from utils.questions import *


def execute_cmd():
    while True:
        answer = prompt(question_execute_cmd)

        if answer["action_type"] == "Init":
            os.system("terraform init")

        elif answer["action_type"] == "Format":
            os.system("terraform fmt")

        elif answer["action_type"] == "Validate":
            os.system("terraform validate")

        elif answer["action_type"] == "Plan":
            os.system("terraform plan")

        elif answer["action_type"] == "Apply":
            os.system("terraform apply")

        elif answer["action_type"] == "Destroy":
            os.system("terraform destroy")

        elif answer["action_type"] == "Go back to menu":
            return
