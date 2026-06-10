def pega_sobrenome():
    while True:
        sobrenome = input('Digite seu sobrenome: ')
        if sobrenome:
            if sobrenome.isalpha():
                return sobrenome
            else:
                print('Sobrenome invalido')
        else:
            return sobrenome

def pega_idades():
    while True:
        try:
             idade = int(input('Digite sua idade: '))
        except:
            print('Digite uma idade valida')
        else:
            if idade:
                return idade
            else:
                print('idade invalida')

def pega_altura():
    while True:
        try:
             altura = int(input('Digite sua altura: '))
        except:
            print('Digite uma idade valida')
        else:
            if altura:
                return altura
            else:
                print('altura invalida')

def pega_peso():
       while True:
          try:
               peso = float(input('Digite seu peso: '))
          except:
               print('Digite um peso valido')
          else:
            if peso:
                return peso
            else:
                print('pedp invalido')

pessoas = []
n = 0

while True:
    sobrenome = pega_sobrenome()
    if sobrenome:
       n += 1
       idade = pega_idades()
       altura = pega_altura()
       peso = pega_peso()
       pessoa = [sobrenome, idade, altura, peso]
       pessoas.append(pessoa)
    else:
        break

soma_ides = 0
soma_alturas = 0
soma_pesos = 0
if n>0:

 pessoas.sort()

 print('Relação de nomes Cadastradas')
 print('____________________________')

 for i in range(0,len(pessoas)):
        print(f'{pessoas [i][0]} - {pessoas [i][1]} - {pessoas [i][2]} - {pessoas [i][3]}')
        soma_ides += pessoas[i][1]
        soma_alturas += pessoas[i][2]
        soma_pesos += pessoas [i][3]
 print("____________________________")

 media_idade = soma_ides/n
 media_altura = soma_alturas/n
 media_peso = soma_pesos/n

 print(f'Idade média: {media_idade}')
 print(f'Altura média: {media_altura}')
 print(f'Peso médio: {media_peso}')
 print("____________________________")
