NOME = input()
n_datas = int(input())

#indices que vão ser acumulados
contagem = 0

#total
total_views = 0
n_datas_uteis = 0

#___2018____
total_views_2018 = 0
datas_2018 = 0

#___2019____
total_views_2019 = 0
datas_2019 = 0

#___2020____
total_views_2020 = 0
datas_2020 = 0


while contagem < n_datas:

    data = input().split("-")
    views = int(input())
    contagem += 1

    #separar as datas do trienio
    if data[0] in "2018,2019,2020":
        total_views += views
        n_datas_uteis += 1
    
    # Contagem por ano
    if data[0] in "2018":
        total_views_2018 += views
        datas_2018 += 1
    
    if data[0] in "2019":
        total_views_2019 += views
        datas_2019 += 1

    if data[0] in "2020":
        total_views_2020 += views
        datas_2020 += 1

# Saida
        
print("Canal:",NOME)
print("Total de views do trienio:",total_views)

media_trienio = total_views / n_datas_uteis

print("Media de views do trienio:", format(media_trienio,".2f"))

print()

#___2018___

print(2018)
print("Total:", total_views_2018)

if total_views == 0:
    print("Porcentagem das views do trienio: indeterminada")

else:
    porcentagem_2018 = (total_views_2018 / total_views )*100
    print("Porcentagem das views do trienio:", format(porcentagem_2018,".2f"))

media_2018 = total_views_2018 / datas_2018
print("Media:", format(media_2018, ".2f"))


print()

#___2019____

print(2019)
print("Total:", total_views_2019)

if total_views == 0:
    print("Porcentagem das views do trienio: indeterminada")
else:
    porcentagem_2019 = (total_views_2019 / total_views )*100
    print("Porcentagem das views do trienio:", format(porcentagem_2019,".2f"))

media_2019 = total_views_2019 / datas_2019
print("Media:", format(media_2019, ".2f"))


print()

#___2020____

print(2020)
print("Total:", total_views_2020)

if total_views == 0:
    print("Porcentagem das views do trienio: indeterminada")
else:
    porcentagem_2020 = (total_views_2020 / total_views )*100
    print("Porcentagem das views do trienio:", format(porcentagem_2020,".2f"))

media_2020 = total_views_2020 / datas_2020
print("Media:", format(media_2020, ".2f"))
