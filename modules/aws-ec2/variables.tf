# variable "instance_count" {
#   description = "The number of instances to start"
#   type        = number
#   default     = 1
# }

variable "ami" {
  description = "The AMI to use for the instance"
  type        = string
  default     = "ami-08c40ec9ead489470"
}

variable "instance_type" {
  description = "The type of instance to start"
  type        = string
  default     = "t2.micro"
}

variable "subnet_id" {
  description = "The subnet ID to launch in"
  type        = string
}

variable "security_group_ids" {
  description = "List of security group IDs to associate"
  type        = list(string)
}

variable "instance_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "Machine"
}

variable "instance_az" {
  description = "The availability zone to start the instance in"
  type        = string
}
