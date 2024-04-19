#!/bin/bash
# Salva o conteudo de um diretorio

data=$(date +%F)
dir=$1
destino=$HOME/GoogleDrive/repos/DSBD/infraestrutura-computacional/exemplos/backups/

if [ $# != 1 ]; then
	echo "Uso: um argumento que eh o diretorio a ser salvo"
	exit
fi

if [ ! -d $dir ]; then
	echo "O diretorio $dir nao existe"
	exit
fi

mkdir -p $destino
cp -R $dir $destino/$dir-$data
echo "Backup do diretorio $dir completo"
