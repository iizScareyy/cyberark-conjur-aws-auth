module "network" {
  source = "./modules/network"

  project_name       = var.project_name
  vpc_cidr           = var.vpc_cidr
  public_subnet_cidr = var.public_subnet_cidr
  availability_zone  = var.availability_zone
}

module "iam" {
  source = "./modules/iam"

  project_name = var.project_name
}

module "security_group" {
  source = "./modules/security-group"

  project_name = var.project_name
  vpc_id       = module.network.vpc_id
}

module "ec2" {
  source = "./modules/ec2"

  project_name  = var.project_name
  instance_type = "t3.micro"

  public_subnet_id      = module.network.public_subnet_id
  security_group_id     = module.security_group.security_group_id
  instance_profile_name = module.iam.instance_profile_name
}