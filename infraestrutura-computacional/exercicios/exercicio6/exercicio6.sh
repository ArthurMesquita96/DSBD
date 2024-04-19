#!/bin/bash

# Ativado o modo depuração
# set -x

#pegando hora do dia
temph=$(date | cut -c16-17)
# pegando data formatada
dat=$(date +"%A %d de %B de %Y (%r)")

#condição se é manhã, tarde ou noite
if [ $temph -lt 12 ]; then
	mess="Bom dia $LOGNAME, tenha um bom dia!"
elif [ $temph -gt 12 -a $temph -le 18 ]; then
	mess="Boa tarde $LOGNAME"
elif [ $temph -gt 18 ]; then
	mess="Boa noite $LOGNAME"
fi

echo -e "$mess\nHoje é $dat"
