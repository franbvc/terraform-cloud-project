from __future__ import print_function, unicode_literals

import json
import os
import sys
from pprint import pprint

from dotenv import load_dotenv
from PyInquirer import print_json, prompt

from utils.questions import *


def query():
    while True:
        answer = prompt(question_query)

        if answer["action_type"] == "Query Instances":
            os.system("terraform output instance_summary")

        elif answer["action_type"] == "Query Users":
            os.system("terraform output user_summary")

        elif answer["action_type"] == "Query Security Groups":
            os.system("terraform output security_group_summary_reduced")

        elif answer["action_type"] == "Query Security Groups + Rules":
            os.system("terraform output security_group_summary_full")

        elif answer["action_type"] == "Go back to menu":
            return
