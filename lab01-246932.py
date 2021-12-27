#INPUTS
Material = input()
PF = float(input())
PE = float(input())
Temp_Atual_Farenheit = float(input())

#Farenheit para Celsius
Temp_Atual_Celsius = (Temp_Atual_Farenheit-32)*5/9
Temp_Atual = round(Temp_Atual_Celsius,2)

#Printar as informações antees do  estado
print("Material:", Material)
print("Ponto de fusao (Celsius):", format(PF, ".2f"))
print("Ponto de ebulicao (Celsius):", format(PE, ".2f"))
print("Temperatura atual (Celsius):", format(Temp_Atual, ".2f"))

#Analisar o estado

if Temp_Atual < PF:
    print("Estado fisico do material: Solido")

elif PE > Temp_Atual >= PF:
    print("Estado fisico do material: Liquido")

else:
    print("Estado fisico do material:  Gasoso")




