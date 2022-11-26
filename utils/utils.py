from __future__ import print_function, unicode_literals

import json

from PyInquirer import print_json, prompt


def process_sg_rule(rules, answer, counter_value):
    answer["cidr_blocks"] = answer["cidr_blocks"].split(",")

    for sg in answer["sg"]:
        rules[f"rule_{counter_value}"] = {
            "sg": sg,
            "from_port": int(answer["from_port"]),
            "to_port": int(answer["to_port"]),
            "protocol": answer["protocol"],
            "cidr_blocks": answer["cidr_blocks"],
        }
        counter_value += 1

    return rules, counter_value


source_destination = {
    "../commit/vpc.json": "../terraform/config/vpc.json",
    "../commit/subnet.json": "../terraform/config/subnet.json",
    "../commit/sg.json": "../terraform/config/sg.json",
    "../commit/sg_ingress.json": "../terraform/config/sg_ingress.json",
    "../commit/sg_egress.json": "../terraform/config/sg_egress.json",
    "../commit/ec2.json": "../terraform/config/ec2.json",
    "../commit/user.json": "../terraform/config/user.json",
}


def verify_files_to_commit():

    files_to_commit = []

    for i in source_destination:
        with open(i, "r") as file:
            source_dict = json.load(file)

        with open(source_destination[i], "r") as file:
            destination_dict = json.load(file)

        if source_dict != destination_dict:
            files_to_commit.append(i)

    return files_to_commit


def policy_dict(answer):
    print(answer)
    policy_dict = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": answer["policy_effect"],
                "Action": answer["policy_actions"].split(","),
                "Resource": answer["policy_resource"],
            }
        ],
    }

    return policy_dict
