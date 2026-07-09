resource "aws_security_group" "app_sg" {
  name        = "${var.project_name}-app-sg"
  description = "Security group for application EC2"
  vpc_id      = var.vpc_id

  egress {
  description = "Allow all outbound traffic"

  from_port   = 0
  to_port     = 0
  protocol    = "-1"

  cidr_blocks = ["0.0.0.0/0"]
}

  tags = {
    Name = "${var.project_name}-app-sg"
  }
}


