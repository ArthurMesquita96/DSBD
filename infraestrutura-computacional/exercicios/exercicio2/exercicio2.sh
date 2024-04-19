#!/bin/bash
# Escreva um script que recebe 2 parametros. O primeiro é um diretorio e o segundo um arquivo. O script deve mover o arquivo para o diretorio

base=$HOME/GoogleDrive/repos/infraestrutura-computacional/exercicios/exercicio2

dir=$1
arq=$2

cp $arq $dir/
