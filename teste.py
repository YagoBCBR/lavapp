idade = input(str("Qual é a sua idade?"))

anoNascimento = idade - 2024

if anoNascimento < 2004:
    print("Você é menor de idade")
else:
    print("Você é elegível")
print(anoNascimento)