import os 

os.system("cls||clear")


print("||Escolha a quantidade de kg:||")
quantdmaca = float(input("Digite a quantidade de maça:" ))
quantdmorango = float(input("Digite a quantidade de morango:"))

if quantdmorango > 25:
    precomorango = 2.50
     
else :
    precomorango = 2.20
if quantdmaca > 5:
        precomaca = 1.80

else :
   precomaca = 1.50
            
pesototal = quantdmorango + quantdmaca
subtotal = (quantdmaca * quantdmorango)+(precomaca * precomorango)

if pesototal > 8 or subtotal > 25:
    desconto = subtotal * 0.10

    totalpagar = subtotal - desconto

    print(f"Peso em morangos: {quantdmorango}")
    print(f"Peso da maça: {quantdmaca}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Desconto: {desconto:.2f}")
    print(f"Total a pagar:{totalpagar:.2f}")