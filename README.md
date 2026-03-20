# 🎮 Jogo de Adivinhação em Python
Projeto simples desenvolvido em Python utilizando conceitos de
Programação Orientada a Objetos (POO) e princípios SOLID.
---
## 🐢 Sumário

- [Sobre o projeto](https://github.com/FilipeVMoreira/jogo-adivinhacao/blob/main/README.md#-sobre-o-projeto-sobre-o-projeto)
- [Conceitos aplicados](https://github.com/FilipeVMoreira/jogo-adivinhacao/blob/main/README.md#-conceitos-aplicados)
- [Como executar](https://github.com/FilipeVMoreira/jogo-adivinhacao/blob/main/README.md#%EF%B8%8F-como-executar-como-executar)
- [Simulação de jogada](https://github.com/FilipeVMoreira/jogo-adivinhacao/blob/main/README.md#-simulando-uma-jogada)

## 📌 Sobre o projeto
O jogo consiste em tentar adivinhar um número aleatório entre
1 e 100 dentro de um limite de tentativas.
O sistema foi desenvolvido aplicando boas práticas de
programação, como:
- Abstração
- Encapsulamento
- Herança
- Polimorfismo
- Princípios SOLID
---
## 🧠 Conceitos aplicados 
### 🔹 Abstração
Classe base `Jogo` define métodos genéricos como `iniciar()` e
`jogar()`.
### 🔹 Encapsulamento
Uso de atributos privados como `__numero_secreto`.
### 🔹 Herança
Classe `JogoAdivinhacao` herda da classe `Jogo`.
### 🔹 Polimorfismo
Métodos `iniciar()` e `jogar()` são implementados de formas
diferentes.
### 🔹 SOLID
Aplicação de princípios como SRP, OCP, LSP, ISP e DIP.
---
## ▶️ Como executar {#como-executar}
1. Instale o Python
2. Execute o arquivo:
```bash
python jogo.py
```
## ✨ Simulando uma jogada 

Jogador digita seu nome para jogar:<br>

<img width="378" height="123" alt="image" src="https://github.com/user-attachments/assets/5e38e020-1068-4b84-8172-e2ab6293eb3a" /><br>
Vão sendo feitas tentativas e o jogo vai informando se o número secreto é menor ou maior:<br>

<img width="395" height="167" alt="image" src="https://github.com/user-attachments/assets/fe5bf1ca-cc0d-4483-b0b2-4475829811bd" /><br>

Após um acerto ou erro, é dada uma opção de continuar. Caso a resposta seja sim, é gerado um novo jogo:<br>

<img width="317" height="318" alt="image" src="https://github.com/user-attachments/assets/b93ea05f-5719-4eb0-ad86-7dcc8fbc20e3" /><br>

O novo jogador faz suas tentativas:<br>

<img width="447" height="184" alt="image" src="https://github.com/user-attachments/assets/e6d1d25c-c892-4982-884b-a1306a2a15d5" /><br>

Ao negar a opção de continuar, o ranking é gerado:<br>

<img width="280" height="71" alt="image" src="https://github.com/user-attachments/assets/e88fb9a0-1c14-493c-a736-1a32bff0284e" /><br>

## 🐱‍👤 Autor : Filipe Valle Moreira

