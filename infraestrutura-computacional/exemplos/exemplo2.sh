#!/bin/bash
# Salva o conteudo de um diretorio

data=$(date +%F)
dir=$1
destino=$HOME/GoogleDrive/repos/DSBD/infraestrutura-computacional/exemplos/backups/

mkdir -p $destino
cp -R $dir $destino/$dir-$data
echo "Backup do diretorio $dir completo"
