
def classificar_heroi(nome, xp):
    if xp <= 1000:
        nivel = "Ferro"
    elif 1001 <= xp <= 2000:
        nivel = "Bronze"
    elif 2001 <= xp <= 5000:
        nivel = "Prata"
    elif 5001 <= xp <= 7000:
        nivel = "Ouro"
    elif 7001 <= xp <= 8000:
        nivel = "Platina"
    elif 8001 <= xp <= 9000:
        nivel = "Ascendente"
    elif 9001 <= xp <= 10000:
        nivel = "Imortal"
    else:  
        nivel = "Radiante"
    
    return f"O Herói de nome {nome} está no nível de {nivel}"

def efeitoJanela(mensagem):
    borda = '*' * (len(mensagem) + 4)
    print(borda)
    print(f"* {mensagem} *")
    print(borda)


print("***********************************")
print("* Classificador de nível de Herói *")
print("***********************************")

nome_heroi = input("Digite o nome do herói: ")
xp_heroi = int(input("Digite a quantidade de experiência (XP) do herói: "))


mensagem = classificar_heroi(nome_heroi, xp_heroi)


efeitoJanela(mensagem)
