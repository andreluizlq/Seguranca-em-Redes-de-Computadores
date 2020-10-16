## ESSE CODIGO É RESPONSÁVEL APENAS PELA ENCRIPTAÇÃO DA FRASE
f=input("DIGITE A FRASE: ") ## PS: TUDO JUNTO E SEM CARACTERE ESPECIAL PQ NA
##                                 MOEDA TBM N TINHA

p=int(input("QUANTAS LETRAS QUER PULAR? "))

f1= f.upper() ##DEIXA A MENSAGEM MAIUSCULA

## CRIA O VETOR COM A MENSAGEM
novo=[]
for i in range(len(f1)):
    novo.append(ord(f1[i]))
##=========================================


##CRIA O VETOR COM A MENSAGEM JA CRIPTOGRAFADA
cript=[]

## PERCORRE O VETOR 'NOVO', AONDE ESTÁ ARMAZENADA A FRASE, E ADICIONA
## AS LETRAS MODIFICADAS COM O DEVIDO NÚMERO DE PULOS PEDIDOS ANTERIORMENTE
for i in range(len(novo)):
    t=novo[i]+p
    if t>90:
        t-=26
        cript.append(chr(t))
    else:
        cript.append(chr(t))
#======================================================

## PARA PRINTAR A MENSAGEM EM EXTENSO NO FORMATO DE STRING        
mcript= ' '
for i in range(len(cript)):
    mcript +=cript[i]

print("A mensagem criptografada:", mcript)
## ======================================================
