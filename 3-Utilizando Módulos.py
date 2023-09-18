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

import pygame

pygame.init();
pygame.mixer.music.load("caminho do arquivo mp3 que desejar");
pygame.mixer.music.play();
pygame.event.wait();


#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas, Quantas letras ao todo (sem considerar espaços), Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: "));

print("Nome completo: {}".format(nome));
print("Seu nome em minúsculas é: {}".format(nome.lower()));
print("Seu nome em maiúsculas é: {}".format(nome.upper()));
print("Seu nome tem {} letras".format(len(nome) - nome.count(' ')));

separa_nome = nome.split();
print("Seu primeiro nome é {} e tem {} letras".format(separa_nome[0], len(separa_nome[0])));

