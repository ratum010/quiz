import json
import re
import random
import os

def menu():
    print("1 - Jogar")
    print("2 - Sair")
    escolha_inicial = input("Escolha uma opção: ")
    return escolha_inicial

i = 0
pontuacao = 0
jogo = False

escolha_inicial = menu()

nome = input("Digite seu nome de usuário: ").casefold()

if os.path.exists("ranking.json"):
    with open("ranking.json", "r") as ranking:
        dados_jogo = json.load(ranking)

    if nome in dados_jogo.keys():
        pontuacao_salva = dados_jogo[nome]
        print(f"Bem-vindo de volta, {nome}! Sua pontuação atual é: {pontuacao_salva} pontos.")
        pontuacao = 0
    else:
        print("Bem-vindo ao Quiz! Vamos começar a jogar!")

else:
    print("Bem-vindo ao Quiz! Vamos começar a jogar!")

while jogo == False:

    if escolha_inicial == "1":

        with open('perguntas_quiz_50.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

            lista = [i for i in range(len(dados))]
            random.shuffle(lista)

            perguntas = dados[lista[i]]["pergunta"]
            print(perguntas)

            alternativas = dados[lista[i]]["alternativas"]
            for item in alternativas:
                print(f"{item["letra"]}) {item["texto"]}")

            numero = dados[lista[i]]["numero"]

            escolha = input("escolha a alternativa correta: ").casefold()


        with open("Gabarito.txt", "r") as gabarito:
            linhas = gabarito.readlines()

            lista = "".join(linhas)

            letra = re.findall(r"[A-Z]",lista)

            acerto = letra[numero -1].casefold()

        if escolha == acerto:
            print("Parabens!!! você acertou")
            pontuacao += 5
            i += 1

        else:
            print(f"Resposta errada, a resposta era {acerto.upper()}")
            print(f"Sua pontuação foi de {pontuacao} Pontos")
            jogo = True

            escolha = input("Deseja jogar novamente(S/n): ").casefold()

            if escolha == "s":
                jogo = False
                i = 0
                pontuacao = 0

            elif escolha == "n":
                print(f"Obrigado por jogar {nome}, sua pontuação final foi de {pontuacao} Pontos")
                jogo = True

                if pontuacao_salva > pontuacao:
                    print(f"Você não superou sua pontuação anterior de {pontuacao_salva} Pontos.")

                else:
                    print(f"Parabéns! Você superou sua pontuação anterior de {pontuacao_salva} Pontos.")
                    salvar = input("Deseja salvar seu progresso(S/n): ").casefold()

                    if salvar == "s":
                        descricao = {nome: pontuacao}
                        if os.path.exists("ranking.json"):
                            with open("ranking.json", "r") as ranking:
                                dados_jogo = json.load(ranking)

                            for chave, valor in descricao.items():
                                dados_jogo[chave] = valor

                            with open("ranking.json", "w") as ranking:
                                json.dump(dados_jogo, ranking)
                                print("Progresso salvo com sucesso!")

                    elif salvar == "n":
                        print("Progresso não salvo.")

                    else:
                        print("Opção inválida. Progresso será salvo.")

            else:
                print("Escolha inválida. Escolha entre 's' para sim ou 'n' para não.")
                continue

    elif escolha_inicial == "2":
        print("Obrigado por jogar!")
        jogo = True

    else:
        print("Escolha inválida. Por favor, selecione uma opção válida.")
        escolha_inicial = menu()