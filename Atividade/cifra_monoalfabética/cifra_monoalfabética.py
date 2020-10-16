## ESSE CÓDIGO É RESPONSAVEL POR AMBAS, ENCRIPTAÇÃO E DECRIPTAÇÃO
## CRIA UM VETOR COM TODAS AS SUBSTITUIÇÃOS NECESSÁRIAS
## ESTÃO NA EXATA ORDEM, SENDO O INDICE 0 DA LISTA "LETRAS" CORRESPONDENTE AO
## INDICE 0 DA LISTA "SUBS"

letras=['a','b','c','d','e','f','g','h','i','j',
        'k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z',' ']

subs=['6','%','$','!','@','¨','&','(',')','*',
      '=','-','3','º',':',';','.','2','4','{',
      '1','£','¢','§',']','5','7']

## ===========================================================================
## UM MENUZINHO PARA O USUÁRIO ESCOLHER SE QUER CRIPTOGRAFAR OU DECRIPTAR
escolha=int(input("1 para criptografar ou 2 decriptar: "))

while escolha>2:
    print("Opcao invalida, digite novamente")
    escolha=input("1 para criptografar ou 2 decriptar: ")
## CRIA VETOR PARA ARMAZENAR A FRASE CRIPTOGRAFADA
frase=input("Digite a frase: ")
novaFrase=[]
tamanho=len(frase)
# ==============================================================================
## SE ESCOLHER DECRIPTAR, FAZ AS COMPARAÇÕES E SUBSTITUI AS LETRAS POR SUAS
## CORRESPONDENTES NA OUTRA LISTA E ARMAZENA O RESULTADO NO VETOR NOVAFRASE
if escolha==2:
    for i in range(tamanho):
        indice=0
        for l in subs:
            if frase[i]==l:
                break
            else:
                indice+=1
        novaFrase.append(letras[indice])

    ##MOSTRA A MENSAGEM CRIPTOGRAFADA
    for i in range(len(novaFrase)):
        print(novaFrase[i],end="")
# ==============================================================================
## SE A ESCOLHA FOR 1 FAZ A MESMA COISA DA OUTRA OPÇÃO, SO QUE DE FORMA INVERSA,
## SUBSTITUINDO OS VALORES DAS LETRAS EM "SUBS" POR SEUS CORRESPONDENTES EM
## "LETRAS".
if escolha==1:
    for i in range(tamanho):
        indice=0
        for l in letras:
            if frase[i]==l:
                break
            else:
                indice+=1
        novaFrase.append(subs[indice])
        
## E MOSTRA A FRASE DESCRIPTADA
    for i in range(len(novaFrase)):
        print(novaFrase[i],end="")
# ================================================================================
