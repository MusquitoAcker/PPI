valor_venda = float(input("Valor da venda: "))
percentual_desconto = int(input("Percentual de desconto: "))

desconto_porcentagem = percentual_desconto / 100

valor_desconto = desconto_porcentagem * valor_venda

valor_final = valor_venda - valor_desconto

print(f"Valor final: {valor_final:.2f} R$")

valor_dado = float(input("Dinheiro dado na hora do paamento: "))

troco = valor_dado - valor_final

print(f"Troco: {troco} R$")