import math


def bhaskara():
    
    while(True):
        # coeficientes da fórmula
        # tentiva de input de coeficientes ↓↓
        try:
            a = input("digite um valor para 'a' \n" )
            b = input("digite um valor para 'b' \n" )
            c = input("digite um valor para 'c' \n" )
            # transformar os valores em float
            a = float(a)
            b = float(b)
            c = float(c)

            break
        # se os valores não forem float ↓↓
        except ValueError or TypeError:
            print("\n Deve ser somente números")

    # equação para delta
    delta = b*b - 4*a*c
    print(f"a={a}; b={b};  c={c}")

    # caso de delta <0
    if(delta < 0):
        print("x1 e x2 nao estao no conjunto dos numeros Reais")

    # caso de delta >0
    elif(delta > 0):
        x1 = (-b + delta**(1/2))/(2*a)
        x2 = (-b - delta**(1/2))/(2*a)
        print(f"delta = {delta}")
        print(f"x' = {x1} ")
        print(f"x'' = {x2} ")

    # caso de delta == 0
    elif(delta == 0):
        x1 = (-b + (delta**1/2))/(2*a)
        print(f"x1 e x2 sao iguais, sendo ambos os valores iguais a {x1}")

def numeroTriangular():
    # valor necessário para começar a sequencia
    n = 1
    print("Você deseja uma sequencia até uma posição (1), ou até atingir um valor? (2)")
    escolhaSeq = input()
    while(escolhaSeq != "1" and escolhaSeq != "2" and escolhaSeq != "/sair"):
        print("escolha somente 1 ou 2")
        escolhaSeq = input()

    # escolha do usuario pro limite da sequencia
    match escolhaSeq:
        case "1": 
            while(True):
                try:
                    valorSeq = input("até qual posição você deseja (números apenas)")
                    valorSeq = int(valorSeq)
                    break
                except (TypeError, ValueError):
                    print("Digite somente números")
        case "2": 
            while(True):
                try:
                    valorSeq = input("até qual valor voce quer que atinja? (numeros apenas)")
                    valorSeq = int(valorSeq)
                    break
                except (TypeError, ValueError):
                    print("Digite somente números")
                    
        case "/sair": escolhaFuncao()
            

    # caso 1 de sequencia (até posição)
    if(escolhaSeq =="1"):
        for i in range(1,valorSeq +1):
            print(f"{i}ª posição- {n}")
            n+= 1+i 

    # caso 2 de sequencia (até valor)
    if(escolhaSeq =="2"):
        for i in range(1, 2**64):
            print(f"{i}ª posição- {n}")
            n+= 1+i 
            if(n>valorSeq): break

def trianguloDeBolas():
    while(True):
        try:
            bolinhas = input("digite um numero inteiro \n")
            bolinhas = int(bolinhas)
            break
        except (TypeError,ValueError):
            print("input inválido")

    # Loop para cada nível conforme solicitado pelo usuario
    for i in range(1,bolinhas+1):
        espaco = " "

        # "bolinhas*2-(i-1)" é responsável por definir a margem em cada nivel
        # bolinhas é o tanto de niveis determinado; 2 é um valor fixo;
        # i é o nivel correspondente da seleção
        margem = (bolinhas*2-i)*espaco

        # imprime as bolinhas com o devido espaço
        print(margem+i*("O"+espaco))

def primos():
    contadorDeDivisores = 0
    primo = True
    index = 0
    divisores = []
    while(True):
        # tente pegar o input do usuario e transformar em int ↓↓
        try: 
            numeroEscolhido = input("Digite um numero inteiro \n") 
            numeroEscolhido = int(numeroEscolhido)
            if(numeroEscolhido < 0):
                raise ValueError
            # se der certo, saia do while ↓↓
            break
        # se não, mostre a mensagem e retorne ao inicio pelo while ↓↑
        except (TypeError, ValueError):
            print("Digite somente números inteiros")



    for i in range(1,numeroEscolhido):
        if(numeroEscolhido%i==0 and i !=1 and i != numeroEscolhido):
            primo = False
            contadorDeDivisores+=1
            divisores.append(i)
            index+=1
        i+=1
        if(i> numeroEscolhido/2):
            # print("atingiu metade")
            break

    # se for primo ↓↓
    if(primo == True or contadorDeDivisores==0):
        print(f"o número {numeroEscolhido} é primo. Portanto, só pode ser divido por 1 e por ele mesmo")

    # se não for primo ↓↓
    elif(primo == False):
        print(f"o número {numeroEscolhido} não é primo e tem {contadorDeDivisores} divisores além de 1 e ele mesmo")
        print(divisores)

        # input de escolha para mostrar as divisões ↓↓
        escolhaMostrarDivisoes = input("\ndeseja mostrar o resultado das divisões? (s/n) \n")
        # caso o input ↑↑ seja afirmativo ↓↓
        if(escolhaMostrarDivisoes == "s"):
            for index in range(0, contadorDeDivisores):
                print(f"{numeroEscolhido}/{divisores[index]} = {int(numeroEscolhido/divisores[index])}")
                index+=1

def analiseCombinatoria():
    while(True):
        escolhaAnalise = input("deseja fazer uma analise de arranjo (1) ou combinação? (2) \n")
        if(escolhaAnalise == "1"):
            break
        elif(escolhaAnalise == "2"):
            break
        else: 
            print("isso não é uma escolha, digite novamente")
    nElementos =0
    pElementos =0


    # pegar os valor de nElementos e pElementos enquanto não seguirem os critérios
    while(True):
        try:
            nElementos = input("Quantos elementos existem na analise?\n")
            nElementos = int(nElementos)
            pElementos = input("Quantos desses elementos são escolhidos?\n")
            pElementos = int(pElementos)
            # pegar pElementos (grupo de nElementos) enquanto for maior que nElementos
            while(pElementos>nElementos):
                print("O número de elementos escolhidos não pode ser maior que os que existem")
                pElementos = int(input("Quantos desses elementos são escolhidos? \n"))
            break
        except ValueError:
            print("Digite somente números inteiros \n")

    # após o while fazer realmente a conta
    i = nElementos
    k = pElementos
    for i in range(nElementos, nElementos-pElementos+1, -1):
        nElementos*=(i-1)
    # caso a escolha seja "arranjo" (1)
    if(escolhaAnalise == "1"):
        print(f"Há {nElementos} maneiras de orgarnizar esse arranjo")

    if(escolhaAnalise =="2"):
        for k in range(pElementos, 1, -1):
            pElementos*=(k-1)
        print(f"Há {nElementos/pElementos} combinações")

def pitagoras():
    # loop de escolha
    while(True):
        escolhaAnalise = input("Deseja encontrar hipotenusa (1) ou cateto (2)? \n")
        if(escolhaAnalise == "1"):
            break
        elif(escolhaAnalise == "2"):
            break
        else: 
            print("isso não é uma escolha, digite novamente")

    # caso escolha 1 (cateto²+cateto²)
    if(escolhaAnalise == "1"):
        cateto1 = float(input("Digite o valor do cateto 1 \n"))
        cateto2 = float(input("Digite o valor do cateto 2 \n"))
        print(cateto1, cateto2)
        # se os catetos forem menores q 1
        if(cateto1 < 1 or cateto2 <1):
            raise ValueError("Somente numeros positivos maiores que 1")
        print("A hipotenusa é ", round((cateto1**2+cateto2**2)**(1/2),2))

    # caso escolha 2 (hipotenusa²-cateto²)
    else:
        hipotenusa = float(input("Digite o valor da hipotenusa **maior que o cateto\n"))
        cateto1 = float(input("Digite o valor do cateto \n"))
        # se hipotenusa for menor que cateto
        if(hipotenusa<cateto1):
            raise ValueError ("Hipotenusa não pode ser menor que o cateto")
        print("O outro cateto é", round((hipotenusa**2-cateto1**2)**(1/2),2))

def trianguloPascal():
    while(True):
        try:
            escolhaDoUsuario = int(input("quantas linhas vc quer? \n"))
            break
        except (TypeError, ValueError):
            print("Digite somente numeros")
    # pegar input do usuário e declarar variaveis 
    mapaTrianguloPascal = []
    linhaTriangulo = []
    linhaTrianguloTemp = []

    # criar primeira linha do triângulo
    for x in range(0, escolhaDoUsuario+2):
        linhaTriangulo.append(0)
        if(x == escolhaDoUsuario):
            linhaTriangulo[x] = 1

    # transformar mapaTrianguloPascal[] em array bidimensional como triangulo retangulo
    # for loop para cada linha
    for y in range(0, escolhaDoUsuario + 1):
        linhaTrianguloTemp = linhaTriangulo
        mapaTrianguloPascal.insert(y, linhaTriangulo.copy())

        # for loop para cada elemento
        for x in range(0, escolhaDoUsuario + 1):
            if(x == escolhaDoUsuario):
                continue
            linhaTriangulo[x] = linhaTrianguloTemp[x] + linhaTrianguloTemp[x+1]

    # for loop para imprimir o triângulo de pascal como desejado
    for y in range(0, len(mapaTrianguloPascal)):
        print(f"linha {y}: ", end="")
        for x in range(0, len(mapaTrianguloPascal[0])):
            print("  ", end="")
            if(mapaTrianguloPascal[y][x] == 0):
                print("", end="")
                continue
            else:
                print(mapaTrianguloPascal[y][x], end="")
        print("\n")



# função de outras funções:
def escolhaFuncao():
    # opções ↓
    print()
    print("escolha uma função para rodar: (digite o número)")
    print("1 - bhaskara()")
    print("2 - numeroTriangular()")
    print("3 - trianguloDeBolas()")
    print("4 - primos()")
    print("5 - analiseCombinatoria() (arranjo e combinação simples)")
    print("6 - pitagoras()")
    print("7 - trianguloPascal()")
    
    while(True):
        try:
            escolha = input()
            escolha = int(escolha)
            break
        except ValueError:
            print("Tente somente o número")

    # casos de funções para o usuário escolher
    match escolha:
        case 1: bhaskara()
        case 2: numeroTriangular()
        case 3: trianguloDeBolas()
        case 4: primos()
        case 5: analiseCombinatoria()
        case 6: pitagoras()
        case 7: trianguloPascal()

# rodar a programação infinitamente
while(True):
    escolhaFuncao()

