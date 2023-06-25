import random
from time import sleep
from pyfiglet import figlet_format


perguntas = {"pergunta1": {"pergunta":"Qual é o significado de 'cat' em português?", "certa":"a",
                "opc": ["a) Gato", "b) Cachorro", "c) Pássaro", "d) Rato"]},
                "pergunta2":  {"pergunta":"Qual é a tradução de 'book' em português?", "certa":"c",
                "opc": ["a) Caderno", "b) Lápis", "c) Livro", "d) Caneta"]},
                "pergunta3":  {"pergunta":"O que significa 'goodbye' em português?","certa":"b",
                "opc": ["a) Bom dia", "b) Tchau", "c) Obrigado", "d) Desculpe"]}}

def fazer_pergunta(pergunta, opcoes):
    print(pergunta)
    for opcao in opcoes:
        print(opcao)
    print()
    print("Digite a letra da opção correta")
    resposta = input(">>>").lower()
    return resposta

def jogar_jogo():
    titulo = figlet_format("Jogo Educativo")
    print(titulo)
    pontos = 0
    perguntas_lista = list(perguntas.keys())
    random.choice(perguntas_lista)

    for pergunta in perguntas_lista:
        resposta_correta = perguntas[pergunta]["certa"].lower()
        opcoes = perguntas[pergunta]["opc"]
        perguntar = perguntas[pergunta]["pergunta"]

        resposta_jogador = fazer_pergunta(perguntar, opcoes)

        if resposta_jogador == resposta_correta:
            print("Resposta correta!")
            pontos += 1

        else:
            print("Resposta incorreta!")
        print()
        print(titulo)

    print(f"Fim do jogo! Pontuação final: {pontos} pontos de {len(perguntas)} perguntas.")
    print()
    print("Deseja continuar o jogo? [s/n]")
    continuar = input(">>> ")
    if continuar == "s".lower():
        print("Recomeçando...")
        sleep(2)
        jogar_jogo()


jogar_jogo()












