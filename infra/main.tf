# 1. Definimos quem é o provedor (A loja onde compramos o servidor)
provider "aws" {
  region = "us-east-1"
}

# 2. Pedimos uma instância (O servidor propriamente dito)
resource "aws_instance" "gold_validator_server" {
  ami           = "ami-0c55b1adcbfafe1f0" # Id de um sistema Linux
  instance_type = "t2.micro"             # O tamanho (esse é o gratuito)

  tags = {
    Name = "Server-Validador-Ouro"
  }
}