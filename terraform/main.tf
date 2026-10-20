
resource "aws_security_group" "demo" {
  name        = "lab3-demo-security-group"
  description = "Intentionally insecure Lab 3 example"

  ingress {
    description = "SSH open to the internet"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_s3_bucket" "demo" {
  bucket = "femin-lab3-demo-bucket-change-me"
}
