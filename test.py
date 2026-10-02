import json

with open("ranking.json", "r") as ranking:
        dados_jogo = json.load(ranking)

nome = "wesley"
if nome in dados_jogo.keys():
    print(nome)