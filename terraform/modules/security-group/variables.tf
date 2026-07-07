variable "project_name" {
  description = "Project name used for tagging resources"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID where the security group will be created"
  type        = string
}