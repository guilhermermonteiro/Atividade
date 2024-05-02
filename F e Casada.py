import os

os.system("cls||clear")

nome = input("Digite seu nome:")
sexo = input("Digite seu sexo:")
estdcivil = str(input("Digite o estado civil:"))

print(f"nome:{nome}")
print(f"idade:{sexo}")
print(f"estado civil:{estdcivil}")

if sexo == "F" and estdcivil == "Casada":
    tempocasada = input("Digite o tempo de casada: ")
    os.system("cls||clear")
    print(f"Tempo de casada{tempocasada}")
