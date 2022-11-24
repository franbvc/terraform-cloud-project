resource "aws_iam_user" "my_user" {
  name = var.username

  tags = {
    Name = var.username
  }
}
