# output "instance_id" {
#   description = "ID of the EC2 instance"

#   value = [
#     for instance in module.ec2_instance :
#     instance.instance_id
#   ]
# }

# output "instance_availability_zone" {
#   description = "Availability zone of the EC2 instance"

#   value = [
#     for instance in module.ec2_instance :
#     instance.instance_az
#   ]
# }

output "instance_summary" {
  description = "Summary of the EC2 instance"

  value = [
    for instance in module.ec2_instance :
    {
      instance_id = instance.instance_id
      instance_az = instance.instance_az
    }
  ]
}

output "user_summary" {
  description = "Summary of the IAM user"

  value = [
    for user in module.iam_user :
    {
      user_name = user.user_name
      user_arn  = user.user_arn
    }
  ]
}

output "security_group_summary_reduced" {
  description = "Summary of the security group (without the ingress and egress rules)"

  value = [
    for security_group in module.security_group :
    {
      security_group_name = security_group.sg_name
      security_group_id   = security_group.sg_id
    }
  ]
}

output "security_group_summary_full" {
  description = "Summary of the security group (with the ingress and egress rules)"

  value = [
    for security_group in module.security_group :
    {
      security_group_name    = security_group.sg_name
      security_group_id      = security_group.sg_id
      security_group_ingress = security_group.sg_ingress
      security_group_egress  = security_group.sg_egress
    }
  ]
}