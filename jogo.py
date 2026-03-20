import random
from abc import ABC, abstractmethod

# Classe principal do jogo que poderá ser reutilizada.
class Jogo(ABC):

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def jogar(self):
        pass

# Classe que define o jogador, armazenando o input que contém o nome.
class Jogador:
    def __init__(self):
        self.__nome = ""
    def obter_nome(self):
        if not self.__nome:
            self.__nome = input("Digite seu nome: ")
        return self.__nome

# Classe que define o ranking que atualiza ao longo das iterações do laço while True.
class Ranking:

    def __init__(self):
        self.__resultados = []

    def adicionar_resultado(self, nome, tentativas):
        self.__resultados.append((nome, tentativas))

    def mostrar_ranking(self):

        if not self.__resultados:
            print("\nRanking vazio")
            return

        ranking_ordenado = sorted(self.__resultados, key=lambda x: x[1])

        print("\nRANKING")
        for pos, (nome, tentativas) in enumerate(ranking_ordenado, start=1):
            print(f"{pos}º lugar - {nome} ({tentativas} tentativas)")

# Classe que estrutura a estrutura do jogo em si, demostrando as tentativas e exibindo as instruções de adivinhação de forma visual.
class JogoAdivinhacao(Jogo, Jogador):

    def __init__(self, ranking):
        super().__init__()
        self.__numero_secreto = random.randint(1, 100)
        self.__tentativas = 0
        self.__limite = 10
        self.__ranking = ranking

    def iniciar(self):
        nome = self.obter_nome()

        print(f"\nBem-vindo(a) {nome}!\n")
        print("JOGO DA ADIVINHAÇÃO")
        print("Tente adivinhar o número secreto entre 1 e 100")
        print("Você tem", self.__limite, "tentativas")

    def jogar(self):
        nome = self.obter_nome()

        while self.__tentativas < self.__limite:

            try:
                palpite = int(input("Digite seu palpite: "))
            except ValueError:
                print("Digite apenas números!")
                continue

            self.__tentativas += 1

            if palpite == self.__numero_secreto:
                print(f"Parabéns {nome}! Você acertou!")
                print("Tentativas usadas:", self.__tentativas)

                self.__ranking.adicionar_resultado(nome, self.__tentativas)
                return

            elif palpite < self.__numero_secreto:
                print("O número secreto é MAIOR")

            else:
                print("O número secreto é MENOR")

        print("Suas tentativas acabaram!")
        print("O número secreto era:", self.__numero_secreto)

# Execução do jogo.
def executar_jogo(jogo: Jogo):
    jogo.iniciar()
    jogo.jogar()

# MAIN

# Chama a classe Ranking armazenando-a na variável ranking para atualizá-lo a cada jogada nova.
ranking = Ranking()

# Iteração que garante a continuidade de um jogo mesmo se um jogador ganha ou perde.
while True:

    jogo = JogoAdivinhacao(ranking)
    executar_jogo(jogo)

    continuar = input("\nDeseja jogar novamente? (s/n): ").lower()

    if continuar != "s":
        break
ranking.mostrar_ranking()
