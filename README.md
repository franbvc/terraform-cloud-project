---
title: Application User Guide
author: Francisco Costa
---

# TerraPy
TerraPy is a CLI application that allows users to quickly and easily create cloud infrastructure on AWS using Terraform.

## Overview
First of all, it should be noted that the application was developed to be used in conjunction with [Terraform](https://www.terraform.io/). Terraform is an infrastructure automation tool that allows the user to create, change and destroy cloud resources in a declarative way. The app was developed to facilitate the creation of Terraform configuration files, written in JSON.

### IMPORTANT
For the application to work correctly, it is necessary that the user has Terraform installed on his machine. For more information, access the official Terraform website. In addition, it is also necessary to have python3 with the requirements of the `requirements.txt` file installed in a virtual environment.

## How it works
The heart of the application is the `main.tf` file. This file is responsible for creating cloud resources on AWS. It accesses the JSON configuration files, present in the `terraform/config` folder and creates the resources according to the information contained in them. The `main.tf` file and all other `.tf` files do not need to/should not be changed by the user, unless he wants to add or remove resource types from the standard structure.

As the organization and structure of the JSON configuration files is relatively simple, if the user wants to configure the resources manually, he can simply change the JSON files and run the `terraform apply` command so that the resources are created in AWS. For examples, the user can check the configuration templates available in the `terraform/config-template` folder.

Finally, if the user wants to change the AWS region, he can change the value of the `region` variable in the `terraform/config/config.json` file.


## Setp by step for using the application
### 1. Create a virtual environment with python3
```bash
python3 -m venv ./venv
```

#### 1.1 If you are using python3.10 or higher
Change line in file: 
```
...\.venv\Lib\site-packages\prompt_toolkit\styles\from_dict.py
```
From:
```python
from collections import Mapping
```
To:
```python
from collections.abc import Mapping
```

### 2. Create a .env file in the root of the project
```bash
touch .env
```
#### 2.1. Add the environment variables to the `.env` file based on the `.env.template` file

### 3. Activate the virtual environment
```bash
source ./venv/Scripts/activate
```

### 4. Install the requirements
```bash
pip install -r requirements.txt
```

### 5. Run the app
```bash
python main.py
```

## Workflow
The workflow of the app takes inspiration from the git workflow. The user creates resource configurations, with the `Create` function (present in the `Edit Plan` tab of the app), which are saved in JSON files in the `commit` folder. After that, the user must use the `Commit Changes` function (present in the `Edit Plan` tab of the app) so that the created configurations are copied to the `terraform/config` folder (which the `main.tf` file uses as a base to apply the plan). Finally, the user must use the `apply` function (present in the `Execute Command` tab of the app) so that the configurations are sent to AWS.

To undo changes saved in the `commit` folder, the user can use the `Stash` function, which copies the configurations from the `terraform/config` folder to the `commit` folder.

### Workflow diagram:
Create -> copy file from terraform/config folder -> add resources to file -> save to commit folder

Update -> access file from commit folder -> change resources in the file -> save to commit folder

Delete -> access file from commit folder -> delete resources in the file -> save to commit folder

Commit Changes -> check which files in the commit folder are different from the terraform/config folder -> ask the user which files he wants to commit -> copy the files from the commit folder to the terraform/config folder

Stash -> copy the files from the terraform/config folder to the commit folder

### Important
* The user should not create a resource (Create) of the same type, before performing a Commit Changes. Otherwise, the Terraform configuration file will be overwritten and the created resources will be lost.

* Example: The user creates a resource of type `EC2 Instance` using Create. Then, he decides another resource of type `EC2 Instance` using Create. In this case, the Terraform configuration file, present in the commit folder, will be overwritten and the first created resource will be lost.

* Before using Update and Delete it is suggested that the user use Stash or Commit Changes, to ensure that the files in the commit folder are synchronized with those in the terraform/config folder.

