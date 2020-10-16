## ESSE CODIGO É RESPONSÁVEL APENAS PELA ENCRIPTAÇÃO DA FRASE
## CRIA A TABELA PARA A ADIÇÃO DA FRASE E CHAVE POSTERIORMENTE
tabela=[]
for i in range(26):
    linha=[]
    cont=65+i
    for j in range(26):
        if cont>90:
            cont-=26
        linha.append(chr(cont))
        cont+=1
    tabela.append(linha)

#==========================================================================
## A ENTRADA DA FRASE E CHAVE
## CRIAÇÃO DE SUAS TABELAS E VETORES
f=input("Digite a mensagem em MAIUSCULO: ")
c=input("Digite a chave em MAIUSCULO: ")

frase=[]
chave=[]
novafrase=[]
cript=[]
descript=[]

#===========================================================================
# CONJUNTO DE LAÇOS RESPONSÁVEIS PELA ADIÇÃO DA FRASE E CHAVE EM SUAS RESPECTIVAS
# VETORES
for i in f:
    frase.append(i)
    novafrase.append(i)
for i in c:
    chave.append(i)
#=============================================================================

#CRIAÇÃO DA TABELA E COMPARAÇÃO ENTRE A TABELA E A CHAVE PARA A CRIAÇÃO DA CHAVE
#CRIPTOGRAFADA
for i in range(len(chave)):
    novafrase.insert(i,chave[i])
    novafrase.pop()

for i in range(len(frase)):
    l=ord(novafrase[i])
    l-=65
    c=ord(frase[i])
    c-=65
    cript.append(tabela[l][c])
#===============================================================================
# CRIA UMA VARIAVEL STR TCRIPT PARA APRESENTAR A FRASE CRIPTOGRAFADA PARA O
# USUÁRIO
tcript=''
for i in range(len(frase)):
    tcript+=cript[i]


print("Sua Auto-Key:",tcript)
#===============================================================================


    
    
























