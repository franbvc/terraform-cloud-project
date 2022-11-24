variable "sg_name" {
  description = "Name of the security group"
  type        = string
}

variable "sg_description" {
  description = "Description of the security group"
  type        = string
  default     = "empty"
}

variable "vpc_id" {
  description = "VPC ID"
  type        = string
}

