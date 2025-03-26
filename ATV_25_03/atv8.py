salario_bruto = float(input("Salario bruto: "))
valor_vendas = float(input("Valor bruto das vendas: "))

comissao = round(valor_vendas * 0.03, 2)
salario_esperado = comissao + salario_bruto

print("O salario bruto do vendedor é de: ", salario_esperado)

desconto_inss = round(salario_esperado * 0.09, 1)
print("O desconto do INSS é de: ", desconto_inss)

print("O salario liquido do funcionario é de: ", salario_esperado - desconto_inss )