output "sg_id" {
  description = "The ID of the security group"
  value       = aws_security_group.my_sg.id
}

output "sg_name" {
  description = "The name of the security group"
  value       = aws_security_group.my_sg.name
}

output "sg_ingress" {
  description = "The ingress rules of the security group"
  value       = aws_security_group.my_sg.ingress
}

output "sg_egress"  {
  description = "The egress rules of the security group"
  value       = aws_security_group.my_sg.egress
}