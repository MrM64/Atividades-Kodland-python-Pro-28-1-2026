games={"foi de F":"Algo ou alguém que morreu",
"Ruchar":"Ir atráz de alguém",
"GG":"God Game/Bom jogo", 
"Farmar":"conseguir uma quantidade consideravel de recursos"}
print("Dicionário:")

print(games)
while True:
    print(" ")
    pergunta = input("Digite uma palavra que você gostaria de saber.")

    if pergunta in games.keys():
        print(games[pergunta])
    else:
        print("Essa palavra não está no dicionário")
