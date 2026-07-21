print("Hello World") #Hello

print(12, 34)
print(12, 34, sep="-")
print(12, 34, sep="-", end="\r\n")
print(12, 34, sep="-", end="\n")

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
a_dez_vezes = "A" * 10
concatenacao = "A" + "B" + "C"
trez_vezes_letter = 3 * "Letter"

print(len(string))
print(f"String invertida {string[::-1]}")
print(var)
print(adicao)
print(subtracao)
print(multiplicacao)
print(divisao)
print(divisao_inteira)
print(exponenciacao)
print(modulo)
print(concatenacao)
print(a_dez_vezes)
print(trez_vezes_letter)
print(12, 34, adicao, "hello", sep="-", end="\n")

print(int("1"),type(int("1")))
print(type(float("1")+1))
print(bool(" "))
print(str(11) + "b")

valor_um = int(input("Digite um valor: "))
valor_dois = int(input("Digite outro valor: "))

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

endereco_memoria_v1 = "a"
endereco_memoria_v2 = "a"
endereco_memoria_v3 = "a"
print(id(endereco_memoria_v1), id(endereco_memoria_v2), id(endereco_memoria_v3))