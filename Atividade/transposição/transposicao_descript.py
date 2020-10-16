## ESSE CÓDIGO É RESPONSÁVEL APENAS PELA DECRIPTAÇÃO DA MENSAGEM
## ENTRADA DO USUÁRIO E CRIAÇÃO DOS RESPECTIVOS VETORES QUE SERÃO USADOS
c=input("CHAVE: ")
f=input("FRASE: ")
frase=[str(x) for x in f.split(' ')]
chave=[]
numeros=[]
vetor=[]
#===============================================================================
##ADICIONAR OS VALORES NOS VETORES CORRESPONDENTES##
for i in range(len(c)):
    chave.append(c[i])
    vetor.append(c[i])
    numeros.append(i)
#===============================================================================
##ADICIONA NA CHAVE EM ORDEM AFALBETICA
for i in range(len(chave)):
    chave[i]=ord(chave[i])
#===============================================================================
##REORGANIZA A MATRIZ DE FORMA QUE A MENSAGEM SEJA DECRIPTADA
menor=1000
for i in range(len(chave)):
    for j in range(len(chave)):
        if chave[j]==None:
            continue
        if chave[j]<menor:
            menor=chave[j]
            indice=j
    vetor[indice]=numeros[i]
    chave[indice]=None
    menor=1000
#===============================================================================
##PRINTA A MENSAGEM DECRIPTADA EM FORMA DE MATRIZ
##LER NA HORIZONTAL!!
for i in range(len(vetor)):
    print(frase[vetor[i]])
##=============================================================================


