print("Digite o cpf")
variavel = input()
cpfN = "0123456789"
cpfVerificado = ""
for i in variavel:
    if i in cpfN:
        cpfVerificado += i

print(cpfVerificado)    