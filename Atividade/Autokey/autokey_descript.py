# ESSE CÓDIGO É RESPONSAVEL APENAS PELA DESCRIPTAÇÃO DA MENSAGEM JÁ CRIPTOGRAFADA
## CRIAÇÃO DA TABELA PARA INSERÇÃO DOS VALORES
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
#==============================================================================
##ENTRADA DO USUÁRIO E CRIAÇÃO DAS RESPECTIVAS TABELAS E VETORES NECESSÁRIOS
f_cript=input("Digite a frase criptografada: ")
f_chave=input("Digite a chave: ")
cript=[]
chave=[]
descript=[]
#=============================================================================
#INSERÇÃO DOS VALORES DE CHAVE E DA MENSAGEM CRIPTOGRAFADA NOS VETORES
##RESPECTIVOS
for i in f_cript:
    cript.append(i)
for i in f_chave:
    chave.append(i)
#=============================================================================
##FAZ A COMPARAÇÃO NA TABELA PARA GERAR A MENSAGEM DESCRIPTADA E ARMAZENA
## EM UM VETOR CHAMADO "DESCRIPT"
for i in range(len(cript)):
    l=ord(chave[i])-65
    x=tabela[l].index(cript[i])
    descript.append(chr(x+65))
    chave.append(chr(x+65))
#=============================================================================

#CRIA UMA VARIÁVEL STR "TEXTO" PARA APRESENTAR A MENSAGEM DESCRIPTADA PARA
#O USUÁRIO
texto=''
for i in range(len(cript)):
    texto+=descript[i]

print(texto)
#===============================================================================
