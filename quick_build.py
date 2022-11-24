from __future__ import print_function, unicode_literals

import os
import sys
from pprint import pprint

from dotenv import load_dotenv


def main():
    load_dotenv()
    os.chdir("./terraform")

    os.system("terraform init")
    os.system("terraform fmt")
    os.system("terraform validate")
    os.system("terraform apply -auto-approve")
    # os.system("terraform plan")


if __name__ == "__main__":
    main()
