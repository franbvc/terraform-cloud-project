from PyInquirer import Separator

question_vpc = [
    {
        "type": "input",
        "name": "vpc_name",
        "message": "What is the name of the VPC?",
    },
    {
        "type": "input",
        "name": "vpc_cidr",
        "message": "What's the VPC CIDR block?",
        "default": "10.0.0.0/16",
    },
]

question_subnet = [
    {
        "type": "input",
        "name": "subnet_name",
        "message": "What is the name of the subnet?",
    },
    {
        "type": "input",
        "name": "subnet_cidr",
        "message": "What's the subnet CIDR block?",
        "default": "10.0.1.0/24",
    },
    {
        "type": "list",
        "name": "subnet_az",
        "message": "What availability zone do you want to use?",
        "choices": [
            "us-east-1a",
            "us-east-1b",
            "us-east-1c",
            "us-east-1d",
        ],
        "default": "us-east-1a",
    },
]

question_subnet_create_more = [
    {
        "type": "list",
        "name": "create_more",
        "message": "Do you want to create more subnets?",
        "choices": [
            "Yes",
            "No",
        ],
    }
]

question_security_group = [
    {
        "type": "input",
        "name": "sg_name",
        "message": "What is the name of the security group?",
    },
    {
        "type": "input",
        "name": "sg_description",
        "message": "What is the description of the security group?",
    },
]

question_security_group_create_more = [
    {
        "type": "list",
        "name": "create_more",
        "message": "Do you want to create more security groups?",
        "choices": [
            "Yes",
            "No",
        ],
    }
]

question_sg_rule = [
    {
        "type": "checkbox",
        "name": "sg",
        "message": "Select security groups to add the rule to",
        "choices": [],
    },
    {
        "type": "input",
        "name": "from_port",
        "message": "What is the port range start?",
        "default": "22",
    },
    {
        "type": "input",
        "name": "to_port",
        "message": "What is the port range end?",
        "default": "22",
    },
    {
        "type": "input",
        "name": "protocol",
        "message": "What is the protocol?",
        "default": "tcp",
    },
    {
        "type": "input",
        "name": "cidr_blocks",
        "message": "What are the CIDR blocks? (separate by comma)",
        "default": "10.0.0.0/16",
    },
]

question_sg_rule_create_more = [
    {
        "type": "list",
        "name": "create_more",
        "message": "Do you want to create more security group rules?",
        "choices": [
            "Yes",
            "No",
        ],
    }
]

question_ec2 = [
    {
        "type": "input",
        "name": "name",
        "message": "What is the name of the EC2 instance?",
    },
    {
        "type": "list",
        "name": "ami",
        "message": "What is the image of the EC2 instance?",
        "choices": [
            "Ubuntu 22.04",
            "Ubuntu 20.04",
        ],
    },
    {
        "type": "list",
        "name": "instance_type",
        "message": "What is the instance type of the EC2 instance?",
        "choices": [
            "T2 Micro",
            "T2 Small",
        ],
    },
    {
        "type": "list",
        "name": "subnet",
        "message": "What is the subnet of the EC2 instance?",
        "choices": [],
    },
    {
        "type": "checkbox",
        "name": "security_group_ids",
        "message": "What are the security groups of the EC2 instance?",
        "choices": [],
    },
]

question_ec2_create_more = [
    {
        "type": "list",
        "name": "create_more",
        "message": "Do you want to create more EC2 instances?",
        "choices": [
            "Yes",
            "No",
        ],
    }
]

question_user = [
    {
        "type": "input",
        "name": "name",
        "message": "What is the name of the user?",
    }
]

question_user_add_policy = [
    {
        "type": "list",
        "name": "add_policy",
        "message": "Do you want to add a policy to the user?",
        "choices": [
            "Yes",
            "No",
        ],
    }
]

question_user_policy = [
    {
        "type": "input",
        "name": "policy_actions",
        "message": "What are the actions of the policy? (separate by comma)",
    },
    {
        "type": "input",
        "name": "policy_resource",
        "message": "What is the resource of the policy?",
    },
    {
        "type": "list",
        "name": "policy_effect",
        "message": "What is the effect of the policy?",
        "choices": [
            "Allow",
            "Deny",
        ],
    },
]

question_user_create_more = [
    {
        "type": "list",
        "name": "create_more",
        "message": "Do you want to create more users?",
        "choices": [
            "Yes",
            "No",
        ],
    }
]

question_commit = [
    {
        "type": "list",
        "name": "commit",
        "message": "Do you want to commit the changes?",
        "choices": [
            "Yes",
            "No",
        ],
    }
]

question_files_to_commit = [
    {
        "type": "checkbox",
        "name": "files",
        "message": "The current files have been modified. Select the ones you want to commit.",
        "choices": [],
    }
]

question_sg_to_delete = [
    {
        "type": "checkbox",
        "name": "sg",
        "message": "Select security groups to delete",
        "choices": [],
    }
]

question_ec2_to_delete = [
    {
        "type": "checkbox",
        "name": "ec2",
        "message": "Select EC2 instances to delete",
        "choices": [],
    }
]

question_user_to_delete = [
    {
        "type": "checkbox",
        "name": "user",
        "message": "Select users to delete",
        "choices": [],
    }
]

question_update_vpc = [
    {
        "type": "list",
        "name": "vpc_field",
        "message": "What field do you want to update?",
        "choices": [
            "vpc_name",
            "vpc_cidr",
        ],
    }
]

question_sg_rule_update = [
    {
        "type": "list",
        "name": "sg_rule",
        "message": "What rule do you want to update?",
        "choices": [],
    }
]

question_sg_rule_update_field = [
    {
        "type": "list",
        "name": "sg_rule_field",
        "message": "What field do you want to update?",
        "choices": [
            "from_port",
            "to_port",
            "protocol",
            "cidr_blocks",
        ],
    }
]

question_sg_rule_update_value = [
    {
        "type": "input",
        "name": "sg_rule_value",
        "message": "What is the new value?",
        "default": "",
    }
]

question_ec2_update = [
    {
        "type": "list",
        "name": "ec2",
        "message": "What EC2 instance do you want to update?",
        "choices": [],
    }
]


question_ec2_update_sg = [
    {
        "type": "checkbox",
        "name": "security_group_ids",
        "message": "What are the security groups of the EC2 instance?",
        "choices": [],
    },
]
