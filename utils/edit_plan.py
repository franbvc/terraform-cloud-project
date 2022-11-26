from __future__ import print_function, unicode_literals

import json
import os
import sys
from pprint import pprint

from dotenv import load_dotenv
from PyInquirer import print_json, prompt

from utils.aws_utils import *
from utils.questions import *
from utils.resource_questions import *
from utils.utils import *

OKGREEN = "\033[92m"
ENDC = "\033[0m"
FAIL = "\033[91m"
WARNING = "\033[93m"


def dict_to_file(dict, file_name):
    with open(file_name, "w") as file:
        file.write(json.dumps(dict))


def create():
    while True:
        answer = prompt(question_create)

        if answer["resource_type"] == "VPC":
            answer = prompt(question_vpc)
            dict_to_file(answer, "../commit/vpc.json")
            print(
                f"{OKGREEN}File saved to commit/vpc.json, please commit changes to apply.{ENDC} \n"
            )

        elif answer["resource_type"] == "Subnet":
            with open("../terraform/config/subnet.json", "r") as file:
                subnets = json.load(file)

            subnet_name_list = [subnets[i]["subnet_name"] for i in subnets.keys()]
            counter = len(subnets)

            while True:
                answer = prompt(question_subnet)
                if answer["subnet_name"] in subnet_name_list:
                    print(
                        f"{FAIL}Subnet name already exists, please try again.{ENDC} \n"
                    )
                    continue

                subnet_name_list.append(answer["subnet_name"])
                subnets[f"subnet_{counter}"] = answer
                counter += 1
                answer = prompt(question_subnet_create_more)
                if answer["create_more"] == "No":
                    break

            dict_to_file(subnets, "../commit/subnet.json")
            print(
                f"{OKGREEN}File saved to commit/subnet.json, please commit changes to apply.{ENDC} \n"
            )

        elif answer["resource_type"] == "Security Group":
            with open("../terraform/config/sg.json", "r") as file:
                security_groups = json.load(file)

            counter = len(security_groups)
            security_group_name_list = [
                security_groups[i]["sg_name"] for i in security_groups.keys()
            ]

            while True:
                answer = prompt(question_security_group)
                if answer["sg_name"] in security_group_name_list:
                    print(
                        f"{FAIL}Security group name already exists, please try again.{ENDC} \n"
                    )
                    continue

                security_group_name_list.append(answer["sg_name"])
                security_groups[f"sg_{counter}"] = answer
                counter += 1
                answer = prompt(question_security_group_create_more)
                if answer["create_more"] == "No":
                    break

            dict_to_file(security_groups, "../commit/sg.json")
            print(
                f"{OKGREEN}File saved to commit/sg.json, please commit changes to apply.{ENDC} \n"
            )

        elif answer["resource_type"] == "Security Group Rule (Ingress)":
            with open("../terraform/config/sg.json", "r") as file:
                security_groups = json.load(file)

            security_groups_list = [i for i in security_groups.keys()]
            if len(security_groups_list) == 0:
                print(
                    f"{FAIL}No security groups found, please create a security group first. (Don't forget to commit!){ENDC} \n"
                )
                continue

            with open("../terraform/config/sg_ingress.json", "r") as file:
                rules = json.load(file)
            counter = len(rules)

            while True:
                question_sg_rule[0]["choices"] = [
                    {"name": i} for i in security_groups_list
                ]
                answer = prompt(question_sg_rule)
                rules, counter = process_sg_rule(rules, answer, counter)
                answer = prompt(question_sg_rule_create_more)
                if answer["create_more"] == "No":
                    break

            dict_to_file(rules, "../commit/sg_ingress.json")
            print(
                f"{OKGREEN}File saved to commit/sg_ingress.json, please commit changes to apply.{ENDC} \n"
            )

        elif answer["resource_type"] == "Security Group Rule (Egress)":
            with open("../terraform/config/sg.json", "r") as file:
                security_groups = json.load(file)

            security_groups_list = [i for i in security_groups.keys()]
            if len(security_groups_list) == 0:
                print(
                    f"{FAIL}No security groups found, please create a security group first. (Don't forget to commit!){ENDC} \n"
                )
                continue

            with open("../terraform/config/sg_egress.json", "r") as file:
                rules = json.load(file)
            counter = len(rules)

            while True:
                question_sg_rule[0]["choices"] = [
                    {"name": i} for i in security_groups_list
                ]
                answer = prompt(question_sg_rule)
                rules, counter = process_sg_rule(rules, answer, counter)
                answer = prompt(question_sg_rule_create_more)
                if answer["create_more"] == "No":
                    break

            dict_to_file(rules, "../commit/sg_egress.json")
            print(
                f"{OKGREEN}File saved to commit/sg_egress.json, please commit changes to apply.{ENDC} \n"
            )

        elif answer["resource_type"] == "EC2 Instance":
            with open("../terraform/config/subnet.json", "r") as file:
                subnets = json.load(file)

            with open("../terraform/config/sg.json", "r") as file:
                security_groups = json.load(file)

            subnets_list = [i for i in subnets.keys()]
            security_groups_list = [i for i in security_groups.keys()]

            if len(subnets_list) == 0:
                print(
                    f"{FAIL}No subnets found, please create a subnet first. (Don't forget to commit!){ENDC} \n"
                )
                continue

            if len(security_groups_list) == 0:
                print(
                    f"{FAIL}No security groups found, please create a security group first. (Don't forget to commit!){ENDC} \n"
                )
                continue

            with open("../terraform/config/ec2.json", "r") as file:
                instances = json.load(file)

            counter = len(instances)
            instances_name_list = [instances[i]["name"] for i in instances.keys()]

            while True:
                question_ec2[4]["choices"] = [
                    f"{i}, ({subnets[i]['subnet_name']})" for i in subnets_list
                ]
                question_ec2[5]["choices"] = [
                    {"name": f"{i}, ({security_groups[i]['sg_name']})"}
                    for i in security_groups_list
                ]
                answer = prompt(question_ec2)
                if answer["name"] in instances_name_list:
                    print(
                        f"{FAIL}Instance name already exists, please try again.{ENDC} \n"
                    )
                    continue

                instances_name_list.append(answer["name"])
                answer["ami"] = ami_dict[answer["ami"]]
                answer["instance_type"] = instance_type_dict[answer["instance_type"]]
                answer["subnet"] = answer["subnet"].split(",")[0]
                answer["security_group_ids"] = [
                    i.split(",")[0] for i in answer["security_group_ids"]
                ]

                instances[f"instance_{counter}"] = answer
                counter += 1
                answer = prompt(question_ec2_create_more)
                if answer["create_more"] == "No":
                    break

            dict_to_file(instances, "../commit/ec2.json")
            print(
                f"{OKGREEN}File saved to commit/ec2.json, please commit changes to apply.{ENDC} \n"
            )

        elif answer["resource_type"] == "IAM User":
            with open("../terraform/config/user.json", "r") as file:
                users = json.load(file)

            counter = len(users)
            users_name_list = [users[i]["name"] for i in users.keys()]

            while True:
                answer = prompt(question_user)
                if answer["name"] in users_name_list:
                    print(f"{FAIL}User name already exists, please try again.{ENDC} \n")
                    continue

                users_name_list.append(answer["name"])
                users[f"user_{counter}"] = answer

                answer_policy = prompt(question_user_add_policy)

                if answer_policy["add_policy"] == "Yes":
                    answer_policy_info = prompt(question_user_policy)
                    users[f"user_{counter}"]["policy"] = policy_dict(answer_policy_info)

                else:
                    users[f"user_{counter}"]["policy"] = {}

                counter += 1
                answer = prompt(question_user_create_more)
                if answer["create_more"] == "No":
                    break

            dict_to_file(users, "../commit/user.json")
            print(
                f"{OKGREEN}File saved to commit/user.json, please commit changes to apply.{ENDC} \n"
            )

        elif answer["resource_type"] == "Go back to menu":
            return


def update():
    while True:
        answer = prompt(question_update)
        if answer["resource_type"] == "Security Group Rule (Ingress)":
            with open("../commit/sg.json", "r") as file:
                security_groups = json.load(file)
            with open("../commit/sg_ingress.json", "r") as file:
                sg_ingress_rules = json.load(file)

            question_sg_rule_update[0]["choices"] = [
                f"Name: {i}, \n"
                f"From Port: {sg_ingress_rules[i]['from_port']}, \n"
                f"To Port: {sg_ingress_rules[i]['to_port']}, \n"
                f"Protocol: {sg_ingress_rules[i]['protocol']}, \n"
                f"CIDR Blocks: {sg_ingress_rules[i]['cidr_blocks']}, \n"
                f"Security Group: {security_groups[sg_ingress_rules[i]['sg']]['sg_name']}, \n"
                for i in sg_ingress_rules.keys()
            ]

            answer = prompt(question_sg_rule_update)
            selected_rule = answer["sg_rule"].split(",")[0].split(":")[1].strip()

            answer_field = prompt(question_sg_rule_update_field)

            if answer_field["sg_rule_field"] == "cidr_blocks":
                question_sg_rule_update_value[0]["default"] = ",".join(
                    sg_ingress_rules[selected_rule][answer_field["sg_rule_field"]]
                )

            else:
                question_sg_rule_update_value[0]["default"] = str(
                    sg_ingress_rules[selected_rule][answer_field["sg_rule_field"]]
                )

            answer_value = prompt(question_sg_rule_update_value)

            if answer_field["sg_rule_field"] == "cidr_blocks":
                sg_ingress_rules[selected_rule][
                    answer_field["sg_rule_field"]
                ] = answer_value["sg_rule_value"].split(",")

            elif (answer_field["sg_rule_field"] == "from_port") or (
                answer_field["sg_rule_field"] == "to_port"
            ):
                sg_ingress_rules[selected_rule][answer_field["sg_rule_field"]] = int(
                    answer_value["sg_rule_value"]
                )

            else:
                sg_ingress_rules[selected_rule][
                    answer_field["sg_rule_field"]
                ] = answer_value["sg_rule_value"]

            dict_to_file(sg_ingress_rules, "../commit/sg_ingress.json")
            print(
                f"{OKGREEN}File saved to commit/sg_ingress.json, please commit changes to apply.{ENDC} \n"
            )

        elif answer["resource_type"] == "Security Group Rule (Egress)":
            with open("../commit/sg.json", "r") as file:
                security_groups = json.load(file)
            with open("../commit/sg_egress.json", "r") as file:
                sg_egress_rules = json.load(file)

            question_sg_rule_update[0]["choices"] = [
                f"Name: {i}, \n"
                f"From Port: {sg_egress_rules[i]['from_port']}, \n"
                f"To Port: {sg_egress_rules[i]['to_port']}, \n"
                f"Protocol: {sg_egress_rules[i]['protocol']}, \n"
                f"CIDR Blocks: {sg_egress_rules[i]['cidr_blocks']}, \n"
                f"Security Group: {security_groups[sg_egress_rules[i]['sg']]['sg_name']}, \n"
                for i in sg_egress_rules.keys()
            ]

            answer = prompt(question_sg_rule_update)
            selected_rule = answer["sg_rule"].split(",")[0].split(":")[1].strip()

            answer_field = prompt(question_sg_rule_update_field)

            if answer_field["sg_rule_field"] == "cidr_blocks":
                question_sg_rule_update_value[0]["default"] = ",".join(
                    sg_egress_rules[selected_rule][answer_field["sg_rule_field"]]
                )

            else:
                question_sg_rule_update_value[0]["default"] = str(
                    sg_egress_rules[selected_rule][answer_field["sg_rule_field"]]
                )

            answer_value = prompt(question_sg_rule_update_value)

            if answer_field["sg_rule_field"] == "cidr_blocks":
                sg_egress_rules[selected_rule][
                    answer_field["sg_rule_field"]
                ] = answer_value["sg_rule_value"].split(",")

            elif (answer_field["sg_rule_field"] == "from_port") or (
                answer_field["sg_rule_field"] == "to_port"
            ):
                sg_egress_rules[selected_rule][answer_field["sg_rule_field"]] = int(
                    answer_value["sg_rule_value"]
                )

            else:
                sg_egress_rules[selected_rule][
                    answer_field["sg_rule_field"]
                ] = answer_value["sg_rule_value"]

            dict_to_file(sg_egress_rules, "../commit/sg_egress.json")
            print(
                f"{OKGREEN}File saved to commit/sg_egress.json, please commit changes to apply.{ENDC} \n"
            )

        elif answer["resource_type"] == "EC2 Instance":
            # update the sg of the ec2 instance
            with open("../commit/ec2.json", "r") as file:
                ec2_instances = json.load(file)
            with open("../commit/sg.json", "r") as file:
                security_groups = json.load(file)

            question_ec2_update[0]["choices"] = [
                f"Local ID: {i}, \n"
                f"Name: {ec2_instances[i]['name']}, \n"
                f"AMI: {ec2_instances[i]['ami']}, \n"
                f"Instance Type: {ec2_instances[i]['instance_type']}, \n"
                f"Subnet: {ec2_instances[i]['subnet']}, \n"
                for i in ec2_instances.keys()
            ]

            answer_ec2 = prompt(question_ec2_update)

            question_ec2_update_sg[0]["choices"] = [
                {"name": f"{i}, ({security_groups[i]['sg_name']})"}
                for i in security_groups.keys()
            ]

            answer_sg = prompt(question_ec2_update_sg)

            answer_sg["security_group_ids"] = [
                i.split(",")[0] for i in answer_sg["security_group_ids"]
            ]

            instance = answer_ec2["ec2"].split(",")[0].split(":")[1].strip()

            ec2_instances[instance]["security_group_ids"] = answer_sg[
                "security_group_ids"
            ]

            dict_to_file(ec2_instances, "../commit/ec2.json")
            print(
                f"{OKGREEN}File saved to commit/ec2.json, please commit changes to apply.{ENDC} \n"
            )

        elif answer["resource_type"] == "Go back to menu":
            return


def delete():
    while True:
        answer = prompt(question_delete)

        if answer["resource_type"] == "Security Group":
            with open("../commit/sg.json", "r") as file:
                security_groups = json.load(file)

            question_sg_to_delete[0]["choices"] = [
                {"name": f"{i}, ({security_groups[i]['sg_name']})"}
                for i in security_groups.keys()
            ]

            answer = prompt(question_sg_to_delete)

            if len(answer["sg"]) == 0:
                print(f"{FAIL}No security groups selected, please try again.{ENDC} \n")
                continue

            for i in answer["sg"]:
                security_groups.pop(i.split(",")[0])

            dict_to_file(security_groups, "../commit/sg.json")
            print(
                f"{OKGREEN}File saved to commit/sg.json, please commit changes to apply.{ENDC} \n"
            )

        elif answer["resource_type"] == "EC2 Instance":
            with open("../commit/ec2.json", "r") as file:
                instances = json.load(file)

            question_ec2_to_delete[0]["choices"] = [
                {"name": f"{i}, ({instances[i]['name']})"} for i in instances.keys()
            ]

            answer = prompt(question_ec2_to_delete)

            if len(answer["ec2"]) == 0:
                print(f"{FAIL}No instances selected, please try again.{ENDC} \n")
                continue

            for i in answer["ec2"]:
                instances.pop(i.split(",")[0])

            dict_to_file(instances, "../commit/ec2.json")
            print(
                f"{OKGREEN}File saved to commit/ec2.json, please commit changes to apply.{ENDC} \n"
            )

        elif answer["resource_type"] == "IAM User":
            with open("../commit/user.json", "r") as file:
                users = json.load(file)

            question_user_to_delete[0]["choices"] = [
                {"name": f"{i}, ({users[i]['name']})"} for i in users.keys()
            ]

            answer = prompt(question_user_to_delete)

            if len(answer["user"]) == 0:
                print(f"{FAIL}No users selected, please try again.{ENDC} \n")
                continue

            for i in answer["user"]:
                users.pop(i.split(",")[0])

            dict_to_file(users, "../commit/user.json")
            print(
                f"{OKGREEN}File saved to commit/user.json, please commit changes to apply.{ENDC} \n"
            )

        elif answer["resource_type"] == "Go back to menu":
            return


def commit():
    answer = prompt(question_commit)

    if answer["commit"] == "Yes":
        question_files_to_commit[0]["choices"] = [
            {"name": i} for i in verify_files_to_commit()
        ]
        if len(question_files_to_commit[0]["choices"]) == 0:
            print(f"{FAIL}No files to commit.{ENDC} \n")
            return

        answer = prompt(question_files_to_commit)
        if len(answer["files"]) == 0:
            print(f"{FAIL}No files to commit.{ENDC} \n")
            return

        for file in answer["files"]:
            with open(file, "r") as f:
                data = json.load(f)

            dict_to_file(data, source_destination[file])

        print(f"{OKGREEN}Changes committed successfully.{ENDC}")
        print(
            f"{OKGREEN}Please run 'terraform apply' to apply changes or use the Execute Command function in the menu.{ENDC} \n"
        )

    elif answer["commit"] == "No":
        return


def stash():
    for i in source_destination:
        with open(source_destination[i], "r") as f:
            data = json.load(f)

        dict_to_file(data, i)

    print(f"{OKGREEN}Changes stashed.{ENDC} \n")


def edit_plan():
    while True:
        answer = prompt(question_plan)

        if answer["action_type"] == "Create":
            create()

        elif answer["action_type"] == "Update":
            update()

        elif answer["action_type"] == "Delete":
            delete()

        elif answer["action_type"] == "Commit Changes":
            commit()

        elif answer["action_type"] == "Stash":
            stash()

        elif answer["action_type"] == "Go back to menu":
            return
