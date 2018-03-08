@author: Luciano Marqueto
@python version: 2.5
Created on 03/09/2013

-UTILIZACAO DO PROGRAMA

A Etiqueta deve ser colocada na pasta �etiquetas�
Caso o computador n�o tenha python instalado rodar o instalador python-2.5
Executar PrintZpl.py
 - Caso seja executado com linha de comando o nome da etiqueta pode ser passada  como par�metro
Caso n�o seja enviado por par�metro o programa ira solicitar o nome da etiqueta. 
 - N�o � necess�rio informar a pasta apenas o nome e a exten��o (ex: etiqueta.txt)
Ser�o solicitados todos os campos fixos
O programa deve perguntar, caso encontre campos vari�veis, se ser�o utilizados todos os campos
 - caso n�o ser�o todos utilizados deve ser informado quais ser�o e quais n�o ser�o utilizados
Ser�o solicitados todos os campos vari�veis intera��o 

-CONFIGURACAO DA ETIQUETA

Programa para imprimir etiquetas ZPL
Configurar a etiqueta da seguinte forma
Campos fixos (ser�o solicitados apenas uma vez no inicio do programa)
[FIX_Z] sendo que Z deve ser substitu�do pelo nome do campo

Campos vari�veis ser�o solicitados a cada impress�o
[VAR_Z-Y] sendo que Z deve ser substitu�do pelo nome do campo e Y pela sequencia

Linhas vari�veis (quando uma vari�vel n�o for utilizada e sua linha n�o deve ser impressa)
[LZ-Y] sendo que Z deve ser substitu�do pelo nome do campo e Y pela sequencia
