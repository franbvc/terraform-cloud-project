from __future__ import print_function, unicode_literals

import json
import os
import sys
from pprint import pprint

from dotenv import load_dotenv
from PyInquirer import print_json, prompt

from utils.aws_utils import *
from utils.destroy_plan import *
from utils.edit_plan import *
from utils.exe_cmd import *
from utils.query import *
from utils.questions import *


def main():
    load_dotenv()
    os.chdir("./terraform")

    while True:
        answer = prompt(question_1)

        if answer["action_type"] == "Edit Plan":
            edit_plan()

        elif answer["action_type"] == "Execute Command":
            execute_cmd()

        elif answer["action_type"] == "Query Data":
            query()

        elif answer["action_type"] == "Destroy Plan":
            destroy_plan()

        elif answer["action_type"] == "Exit":
            print("Exiting...")
            return


if __name__ == "__main__":
    main()
