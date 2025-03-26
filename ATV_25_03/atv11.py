valor = int(input("Valor: "))
nota200 = 0
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0 
nota2 = 0
nota1 = 0

while valor > 0:

    if (valor >= 200):
        valor - 200
        nota200 = nota200 + 1

    elif (valor >= 100):
        valor - 100
        nota100 = nota100 +1

    elif (valor >= 50):
        valor - 50
        nota50 = nota50 +1

    elif(valor >= 20):
        valor - 20
        nota20 = nota20 +1

    elif (valor >= 10):
        valor - 10
        nota10 = nota10 +1

    elif (valor >= 5):
        valor - 5
        nota5 = nota5 +1

    elif (valor >= 2):
        valor - 2
        nota2 = nota2 +1

    elif (valor >= 1):
        valor - 1
        nota1 = nota1 +1
    else: 
        break


print(f"{nota200} nota(s) de 200")
print(f"{nota100} nota(s) de 100")
print(f"{nota50} nota(s) de 50")
print(f"{nota20} nota(s) de 20")
print(f"{nota10} nota(s) de 10")
print(f"{nota5} nota(s) de 5")
print(f"{nota2} nota(s) de 2")
print(f"{nota1} moeda(s) de 1")