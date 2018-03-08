'''

@author: lmarqueto

Created on 03/09/2013

Programa para imprimir etiquetas ZPL
Configurar a etiqueta da seguinte forma
Campos fixos (serao solicitados apenas uma vez no inicio do programa)
[FIX_Z] sendo que Z deve ser substituido pelo nome do campo

Campos variaveis serao solicitados a cada impressao
[VAR_Z-Y] sendo que Z deve ser substituido pelo nome do campo e Y pela sequencia

Linhas variaveis (quando uma variavel nao for utilizada e sua linha nao deve ser impressa
[LZ-Y] sendo que Z deve ser substituido pelo nome do campo e Y pela sequencia

'''
import os
from sre_compile import isstring

print "Imprimir etiqueta" 
qtd = 1          


#obtem arquivo modelo
# EX Config_teste34.txt
if len(os.sys.argv) == 2 :
    modeloNome = "etiquetas/"+os.sys.argv[1]
else : 
    modeloNome = "etiquetas/"
    modeloNome = modeloNome+raw_input('Informe a etiqueta: ')
try :
    modelo = open(modeloNome,"r")
except :
    print "Etiqueta nao existe"
    raw_input("...")
    os.sys.exit()      
       
campos = {}

#Rastreia campos na etiqueta
# Tipos de campos
# [VAR_X-X]
# [FIX_X]
for line in modelo:
    contem = True
    start = 0
    end = 0       
    while contem == True :        
        start = line.find('[', end)
        end = line.find(']', end+1)
        if (start != -1) and (end != -1):                                        
            if line[start+1:start+4] == 'FIX' :                #               
                if campos.has_key('FIX') != True :
                    fixo = {}
                    campos["FIX"] = fixo                                
                campos["FIX"][line[start+5:end]] = "Aguardando"                
            elif line[start+1:start+4] == 'VAR' :                
                if campos.has_key('VAR') != True :
                    var = {}
                    campos["VAR"] = var
                mark = line.find('-', start, end)
                varName = line[start+5:line.find('-', start, end)]                
                if campos['VAR'].has_key(varName) != True :
                    var = {}
                    campos['VAR'][varName] = var                                                   
                campos['VAR'][varName][line[mark+1:end]] = "Aguardando"                    
        else :            
            contem = False
            


# Verifica a existe campos fixos
if campos.has_key('FIX') :
    for key in campos['FIX']:
        campos['FIX'][key] =  raw_input('Informe o campo %s: '%key)


#config variaveis
entrada = ""
while (entrada != "0" and entrada != "1"):
    entrada = raw_input('Serao utilizados todos os campos variaveis: (1-Sim 0-Nao): ')
 
if entrada == "0" :
    if campos.has_key('VAR') :
        for key_1 in campos['VAR']:                      
            print 'Foram detectados ', len(campos['VAR'][key_1]),' campos ', key_1
            for key_2 in campos['VAR'][key_1]:
                entrada = " "
                while (entrada != "0" and entrada != "1"):
                    entrada = raw_input('Utilizar campo %s %s : (1-Sim 0-Nao): '%(key_1,key_2))            
                if entrada == '0' :
                    campos['VAR'][key_1][key_2] = 'NOT_USED'
modelo.close()

# Interacoes infinitas
while True:
    modelo = open(modeloNome,"r")
    etiqueta = open('imprimir.txt', 'w+')
    os.system("cls")
    print 'Imprimir etiqueta'
    print '-----------------------------'
     
    if campos.has_key('VAR') :
        for key_1 in campos['VAR']:                      
            for key_2 in campos['VAR'][key_1]:        
                if campos['VAR'][key_1][key_2] !=  'NOT_USED' :
                    campos['VAR'][key_1][key_2] =  raw_input('Informe o campo %s %s: '%(key_1,key_2))
                         
     
    # Substituir campos na etiqueta
    for line in modelo:    
        if campos.has_key('FIX') :
            for key in campos['FIX']:  
                line = line.replace('[FIX_%s]'%key, campos['FIX'][key])         
        if campos.has_key('VAR') :
            for key_1 in campos['VAR']:                      
                for key_2 in campos['VAR'][key_1]:                         
                    if campos['VAR'][key_1][key_2] !=  'NOT_USED' :                        
                        line = line.replace('[VAR_%s-%s]'%(key_1,key_2) , campos['VAR'][key_1][key_2])
                        line = line.replace('[L%s-%s]'%(key_1,key_2) , "")
                    else :
                        mark = "[L%s-%s"%(key_1,key_2)
                        mark = len(mark)                    
                        if line[:mark] == "[L%s-%s"%(key_1,key_2) :                        
                            line = ""                  
        etiqueta.write(line)
    etiqueta.seek(0)                  
#     print 'fim'
#     print etiqueta.read()
    modelo.close()
    etiqueta.close()
    os.system("copy imprimir.txt lpt1")
    os.system("cls")
