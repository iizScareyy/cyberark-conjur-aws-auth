resource "aws_security_group" "app_sg" {
  name        = "${var.project_name}-app-sg"
  description = "Security group for application EC2"
  vpc_id      = var.vpc_id

  tags = {
    Name = "${var.project_name}-app-sg"
  }
}


