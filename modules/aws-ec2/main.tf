resource "aws_instance" "my_instance" {
  ami           = var.ami
  instance_type = var.instance_type

  subnet_id         = var.subnet_id
  security_groups   = var.security_group_ids
  availability_zone = var.instance_az

  tags = {
    Name = var.instance_name
  }
}
