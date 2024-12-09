print("Minha Calculadora")
print("Escolha a operação matemática na qual deseja fazer a conta: ")
print("""
1 - Soma(+)
2 - Subtração(-)
3 - Multiplicação(*)
4 - Divisão(/)
""")

operação = input("Digite o número da operação desejada: ")

numero1 = float(input("Digite o primeiro número da operação: "))
numero2 = float(input("Digite o segundo número da operação: "))

if operação == "1":
    print("Resultado = ", numero1 + numero2)
elif operação == "2":
    print("Resultado = ", numero1 - numero2)
elif operação == "3":
    print("Resultado = ", numero1 * numero2)
elif operação == "4":
    print("Resultado = ", numero1 / numero2)

else:
    print("Operação inválida.")
