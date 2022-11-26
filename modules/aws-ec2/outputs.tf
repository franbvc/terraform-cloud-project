output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.my_instance.*.id
}

# output "instance_public_ip" {
#   description = "Public IP address of the EC2 instance"
#   value       = aws_instance.my_instance.*.public_ip
# }

output "instance_az" {
  description = "Availability Zone of the EC2 instance"
  value       = aws_instance.my_instance.*.availability_zone
}
