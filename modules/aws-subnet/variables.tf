variable "vpc_id" {
  description = "The VPC ID"
  type        = string
}

variable "subnet_cidr" {
  description = "The CIDR block for the subnet"
  type        = string
}

variable "subnet_az" {
  description = "The availability zone for the subnet"
  type        = string
  default     = "us-east-1a"
}

variable "subnet_name" {
  description = "The name of the subnet"
  type        = string
  default     = "my-subnet"
}