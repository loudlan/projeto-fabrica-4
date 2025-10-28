nome_boi1 = input("Digite o nome do primeiro boi :")
peso1 = float (input(f"Digite o peso do primeiro boi :"))

nome_boi2 = input("Digite o nome do segundo boi:")
peso2 = float (input(f"Digite o peso do segundo boi:"))

nome_boi3 = input("Digite o nome do terceiro boi:")
peso3 = float (input(f"Digite o preço do terceiro boi:"))

print("---------------------------------------")
print("| LISTA DOS BOIS MAIS PESADOS :" )

if numero1 > numero2 and numero1 > numero3:
    print(f"1){nome_boi1}; - {peso1:.2f} kg")
    if numero2 > numero3:
        print(f"2){nome_boi2}; - {peso2:.2f} kg")
        print(f"3){nome_boi3}; - {peso3:.2f} kg")
    else:
        print(f"3){nome_boi3}; - {peso3:.2f} kg")
        print(f"2){nome_boi2}; - {peso2:.2f} kg")

print("---------------------------------------")
