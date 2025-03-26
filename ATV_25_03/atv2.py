salario = float(input("Salario atual: "))
aumento = int(input("Percentual do aumento: "))

aumentoPorcento = aumento / 100
aumento_valor = salario * aumentoPorcento

valor_total = aumento_valor + salario

print("Salario final: ", valor_total, "R$")