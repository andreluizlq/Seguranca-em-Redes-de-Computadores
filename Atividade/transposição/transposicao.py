import random
#ESSE CÓDIGO APENAS CRIPTOGRAFA A MENSAGEM
##RECEBE A ENTRADA DO USUÁRIO E ARMAZENA NOS VETORES "FRASE" E "CHAVE"
c=input("CHAVE: ")
f=input("FRASE: ")
frase=[]
chave=[]
letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#===============================================================================
#IGNORA ESPAÇO E CARACTERES ESPECIAIS E ADICIONA A FRASE NO VETOR FRASE
for i in range(len(f)):
    if ord(f[i])>90 or ord(f[i])<65:
        continue
    else:
        frase.append(f[i])
#===============================================================================
##ADICIONA A CHAVE NO VETOR CHAVE
for i in range(len(c)):
    chave.append(c[i])
#===============================================================================
#VERIFICA SE SOBROU ESPAÇOS NA LINHA E PREENCHE-OS COM UMA LETRA ALEATÓRIO
#NO FIM DA FRASE, PARA POSTERIORMENTE ADICIONAR NA MATRIZ.

vc=len(chave)
vf=len(frase)

t=vc*vc-vc-vf
while t<0:
    t+=vc

if t>0:
    for i in range(t):
        frase.append(random.choice(letras))
#===============================================================================
#CRIA A MATRIZ, COM A PRIMEIRA LINHA SENDO A CHAVE E OS RESPECTIVOS CONTADORES
##QUE SERÃO USADOS PARA PREENCHE-LA
matriz=[chave]
cont=0
contwhile=0
#===============================================================================
##ADICIONA A FRASE NA MATRIZ ATÉ QUE TODAS AS LINHAS CRIADAS ESTEJAM PREENCHIDAS
while contwhile<len(frase):
    linha=[]
    for j in range(len(chave)):
        linha.append(frase[j+cont])
        contwhile+=1
    cont+=len(chave)
    matriz.append(linha)
#=============================================================================
##CRIA UMA VARIAVEL MENOR PARA UTILIZAR NA COMPARAÇÃO NA HORA DE REARRANJAR
##A MATRIZ NA ORDEM ALFABETICA
menor=1000
indice=0
cript=[] #VETOR DA MENSAGEM CRIPTOGRAFADA
#=============================================================================
#RESPOSAVEL POR REORGANIZAR A MATRIZ DE ACORDO COM A CHAVE
for j in range(vc):
    for k in range(vc):
        if matriz[0][k]==None:
            continue
        if ord(matriz[0][k])<menor:
            menor=ord(matriz[0][k])
            indice=k
    matriz[0][indice]=None
    menor=1000
    for i in range(1,len(matriz)):
        cript.append(matriz[i][indice])
#=============================================================================
##PARA PRINTAR A CHAVE COM OS ESPAÇOS E DIVIDIDA EM UM NÚMERO DE LETRAS
##PADRÃO
cont1=1
total=len(cript)//len(chave)
                      
for g in range(len(cript)):
    if cont1==total:
        print(cript[g],end=" ")
        cont1=1
    else:
        print(cript[g],end="")
        cont1+=1
#==============================================================================




