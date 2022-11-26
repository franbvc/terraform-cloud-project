output "user_arn" {
  description = "ARN assigned by AWS for the user (id)"
  value       = aws_iam_user.my_user.arn
}

output "user_name" {
  description = "The login of the user"
  value       = aws_iam_user.my_user.name
}
