#Exercício que lê um ângulo e mostre seu seno, cosseno, tangente
import math
angulo = int(input("Digite o valor do angulo: "));

print("O seno, cosseno e a tangente são respectivamente: {}, {}, {}".format(math.sin(angulo), math.cos(angulo), math.tan(angulo)));


# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

print("Digite o nome dos quatro alunos para sorte um deles: ");
aluno1 = str(input("Aluno 1: "));
aluno2 = str(input("Aluno 2: "));
aluno3 = str(input("Aluno 3: "));
aluno4 = str(input("Aluno 4: "));

lista_alunos = [aluno1, aluno2, aluno3, aluno4];

sorteio = random.choice(lista_alunos);
print('O aluno sorteado foi:', sorteio);

# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.