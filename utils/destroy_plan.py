from __future__ import print_function, unicode_literals

import json
import os
import sys
from pprint import pprint

from dotenv import load_dotenv
from PyInquirer import print_json, prompt

from utils.questions import *


def destroy_plan():
    while True:
        answer = prompt(question_destroy_plan)

        if answer["action_type"] == "Yes":
            os.system("terraform destroy")

        return
