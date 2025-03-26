bone = 10.00
camiseta = 20.00

quantidade_bone = int(input("Quantidade de boné(s): "))
quantidade_camiseta = int(input("Quantidade de camiseta(s): "))

bone_valor = quantidade_bone * bone
camiseta_valor = quantidade_camiseta * camiseta

valor_total = bone_valor + camiseta_valor

print ("Opçoes de pagamento:")
print("")
print("À vista com desconto de 10%: ", round(valor_total * 0.9, 2), "R$")
print("Em 3x sem juros: ", round(valor_total / 3, 2), "R$ cada parcela")
print("Em 6x com acréscimo de 5%: ", round(((valor_total * 1.05) / 6) , 2), "por parcela, e o total das seis parcelas é de:", round(((valor_total * 1.05) / 6) * 6, 2), "R$")