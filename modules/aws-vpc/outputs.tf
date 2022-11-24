output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.my_vpc.id
}