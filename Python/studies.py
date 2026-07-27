"""DOCSTRING"""
#-----------------------------------------------------------------PRINTS-----------------------------------------------------#
print("Hello World") #Hello

print(12, 34)
print(12, 34, sep="-")
print(12, 34, sep="-", end="\r\n")
print(12, 34, sep="-", end="\n")
print(12, 34, sep="-", end="#")
#-----------------------------------------------------------------VARIABLES-----------------------------------------------------#
var = 2 + 2
adicao = 10+10
modulo = 55 % 2
divisao = 10/2.2
subtracao = 10-5
exponenciacao = 2 ** 10
multiplicacao = 10 * 10
divisao_inteira = 10//2.2
integer = int("1")
string = "hello"
complexo = 3j
a_dez_vezes = "A" * 10
concatenacao = "A" + "B" + "C"
trez_vezes_letter = 3 * "Letter"
endereco_memoria_v1 = "a"
endereco_memoria_v2 = "a"
endereco_memoria_v3 = "a"
#-----------------------------------------------------------------PRINT, FUNCTIONS AND VARS-----------------------------------------------------#
print(var)
print(adicao)
print(subtracao)
print(divisao)
print(modulo)
print(len(string))
print(a_dez_vezes)
print(concatenacao)
print(multiplicacao)
print(exponenciacao)
print(divisao_inteira)
print(trez_vezes_letter)
print(f"String invertida {string[::-1]}")
print(12, 34, adicao, "hello", sep="-", end="\n")

print(int("1"),type(int("1")))
print(type(float("1")+1))
print(bool(" "))
print(str(11) + "b")
print(id(endereco_memoria_v1), id(endereco_memoria_v2), id(endereco_memoria_v3))
#-----------------------------------------------------------------INPUTS-----------------------------------------------------#
valor_um = int(input("Digite um valor: "))
valor_dois = int(input("Digite outro valor: "))
#-----------------------------------------------------------------CONDITIONALS-----------------------------------------------------#
if " " in input("Digite algo: "):
    print("O que digitou contem espaços")

if input("Digite um numero: ").isdigit():
    print("Você digitou um numero")
else:
    print("Não é um numero")

if valor_um > valor_dois:
    print(f"{valor_um} maior que {valor_dois}")
elif valor_dois > valor_um:
    print(
        f"{valor_dois} maior "
        f"que {valor_um}"
    )
else:
    print("Valores iguais")
#-----------------------------------------------------------------LISTS, TUPLES, SETS AND DICTS-----------------------------------------------------#
lists = [1, 2, 3, 3]
print("Lists:", lists)

tuples = (1, 2, 3, 4, 5)
print("Tuples:", tuples)

sets = {1, 2, 3, 3}
print("Sets:", sets)

dicts = {"chave": "valor"}
print("Dicts:", dicts)