## ESSE CODIGO É RESPONSÁVEL APENAS PELA DECRIPTAÇÃO DA FRASE
f=input("DIGITE A FRASE: ")
p=int(input("QUANTOS PULOS FORAM DADOS? "))

## CRIA O VETOR COM A MENSAGEM
cript=[]
for i in range(len(f)):
    cript.append(ord(f[i]))
## =========================================================

## CRIA O VETOR COM A MENSAGEM JA DECRIPTADA
decript=[]

## PERCORRE O VETOR "CRIPT", AONDE ESTÁ ARMAZENADA A MENSAGEM CRIPTOGRAFADA
## E DIMINUI DE CADA LETRA O NÚMERO DE 'PULOS' CITADOS ANTERIORMENTE
for i in range(len(cript)):
    t=cript[i]-p
    if t<65:
        t+=26
        decript.append(chr(t))
        
    else:
        decript.append(chr(t))
## =======================================================

## PARA PRINTAR A MENSAGEM EM EXTENSO NO FORMATO DE STRING       
mdecript= ' '
for i in range(len(decript)):
    mdecript +=decript[i]

print("A mensagem decriptada:", mdecript)
## ======================================================
