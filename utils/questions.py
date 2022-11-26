question_1 = [
    {
        "type": "list",
        "name": "action_type",
        "message": "What do you want to do?",
        "choices": [
            "Edit Plan",
            "Execute Command",
            "Query Data",
            "Destroy Plan",
            "Exit",
        ],
    }
]

question_plan = [
    {
        "type": "list",
        "name": "action_type",
        "message": "What do you want to do?",
        "choices": [
            "Create",
            "Update",
            "Delete",
            "Commit Changes",
            "Stash",
            "Go back to menu",
        ],
    }
]

question_execute_cmd = [
    {
        "type": "list",
        "name": "action_type",
        "message": "What command do you want to execute?",
        "choices": [
            "Init",
            "Format",
            "Validate",
            "Plan",
            "Apply",
            "Destroy",
            "Go back to menu",
        ],
    }
]

question_destroy_plan = [
    {
        "type": "list",
        "name": "action_type",
        "message": "Are you sure you want to destroy this plan?",
        "choices": [
            "Yes",
            "No",
        ],
    }
]

question_create = [
    {
        "type": "list",
        "name": "resource_type",
        "message": "What resource do you want to create?",
        "choices": [
            "VPC",
            "Subnet",
            "Security Group",
            "Security Group Rule (Ingress)",
            "Security Group Rule (Egress)",
            "EC2 Instance",
            "IAM User",
            "Go back to menu",
        ],
    }
]

question_update = [
    {
        "type": "list",
        "name": "resource_type",
        "message": "What resource do you want to update?",
        "choices": [
            "Security Group Rule (Ingress)",
            "Security Group Rule (Egress)",
            "EC2 Instance",
            "Go back to menu",
        ],
    }
]

question_delete = [
    {
        "type": "list",
        "name": "resource_type",
        "message": "What resource do you want to delete?",
        "choices": [
            "Security Group",
            "EC2 Instance",
            "IAM User",
            "Go back to menu",
        ],
    }
]

question_query = [
    {
        "type": "list",
        "name": "action_type",
        "message": "What do you want to query?",
        "choices": [
            "Query Instances",
            "Query Users",
            "Query Security Groups",
            "Query Security Groups + Rules",
            "Go back to menu",
        ],
    }
]
