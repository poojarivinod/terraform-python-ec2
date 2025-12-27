terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.26.0"
    }
  }

  backend "s3" {
    bucket         = "vinod-tf-remote-state-dev"
    key            = "python-ec2"
    region         = "us-east-1"
    dynamodb_table = "vinod-tf-remote-state-dev"
  }
}

provider "aws" {
  region = "us-east-1"
}