terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

locals {
  config_map     = jsondecode(file("./config/config.json"))
  vpc_map        = jsondecode(file("./config/vpc.json"))
  subnet_map     = jsondecode(file("./config/subnet.json"))
  sg_map         = jsondecode(file("./config/sg.json"))
  sg_ingress_map = jsondecode(file("./config/sg_ingress.json"))
  sg_egress_map  = jsondecode(file("./config/sg_egress.json"))
  ec2_map        = jsondecode(file("./config/ec2.json"))
  user_map       = jsondecode(file("./config/user.json"))
  user_policy_map = {
    for user in local.user_map : user.name => user.policy
    if user.policy != {}
  }
}

provider "aws" {
  region = local.config_map.region
}


module "vpc" {
  source = "../modules/aws-vpc"

  vpc_cidr = local.vpc_map.vpc_cidr
  vpc_name = local.vpc_map.vpc_name
}

module "subnet" {
  source     = "../modules/aws-subnet"
  depends_on = [module.vpc]

  for_each = local.subnet_map

  vpc_id      = module.vpc.vpc_id
  subnet_cidr = each.value.subnet_cidr
  subnet_az   = each.value.subnet_az
  subnet_name = each.value.subnet_name
}

module "security_group" {
  source     = "../modules/aws-sg"
  depends_on = [module.vpc]

  for_each = local.sg_map

  vpc_id         = module.vpc.vpc_id
  sg_name        = each.value.sg_name
  sg_description = each.value.sg_description
}

resource "aws_security_group_rule" "ingress_rules" {
  depends_on = [
    module.security_group
  ]

  for_each = local.sg_ingress_map

  type              = "ingress"
  from_port         = each.value.from_port
  to_port           = each.value.to_port
  protocol          = each.value.protocol
  cidr_blocks       = each.value.cidr_blocks
  security_group_id = module.security_group[each.value.sg].sg_id
}

resource "aws_security_group_rule" "egress_rules" {
  depends_on = [
    module.security_group
  ]

  for_each = local.sg_egress_map

  type              = "egress"
  from_port         = each.value.from_port
  to_port           = each.value.to_port
  protocol          = each.value.protocol
  cidr_blocks       = each.value.cidr_blocks
  security_group_id = module.security_group[each.value.sg].sg_id
}

module "ec2_instance" {
  source     = "../modules/aws-ec2"
  depends_on = [module.vpc, module.subnet, module.security_group]

  for_each = local.ec2_map

  ami           = each.value.ami
  instance_type = each.value.instance_type

  subnet_id          = module.subnet[each.value.subnet].subnet_id
  security_group_ids = [for sg in each.value.security_group_ids : module.security_group[sg].sg_id]

  instance_name = each.value.name
}

module "iam_user" {
  source = "../modules/aws-iam-user"

  for_each = local.user_map

  username = each.value.name
}

resource "aws_iam_user_policy" "user_policies" {
  depends_on = [
    module.iam_user
  ]

  for_each = local.user_policy_map

  user = each.key

  policy = jsonencode(each.value)
}
