#!/bin/bash
# Escreva um script que recebe o nome de um arquivo como parametro e copia-o para o diretório /tmp

base=$HOME/GoogleDrive/repos/DSBD/infraestrutura-computacional/exercicios/exercicio1
arq=$1

mkdir -p $base/tmp
cp -r $arq $base/tmp/ 
