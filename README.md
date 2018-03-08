@author: lUciano marqueto
@python version: 2.5
Created on 03/09/2013

-UTILIZACAO DO PROGRAMA

A Etiqueta deve ser colocada na pasta ”etiquetas”
Caso o computador não tenha python instalado rodar o instalador python-2.5
Executar PrintZpl.py
 - Caso seja executado com linha de comando o nome da etiqueta pode ser passada  como parâmetro
Caso não seja enviado por parâmetro o programa ira solicitar o nome da etiqueta. 
 - Não é necessário informar a pasta apenas o nome e a extenção (ex: etiqueta.txt)
Serão solicitados todos os campos fixos
O programa deve perguntar, caso encontre campos variáveis, se serão utilizados todos os campos
 - caso não serão todos utilizados deve ser informado quais serão e quais não serão utilizados
Serão solicitados todos os campos variáveis interação 

-CONFIGURACAO DA ETIQUETA

Programa para imprimir etiquetas ZPL
Configurar a etiqueta da seguinte forma
Campos fixos (serão solicitados apenas uma vez no inicio do programa)
[FIX_Z] sendo que Z deve ser substituído pelo nome do campo

Campos variáveis serão solicitados a cada impressão
[VAR_Z-Y] sendo que Z deve ser substituído pelo nome do campo e Y pela sequencia

Linhas variáveis (quando uma variável não for utilizada e sua linha não deve ser impressa)
[LZ-Y] sendo que Z deve ser substituído pelo nome do campo e Y pela sequencia
