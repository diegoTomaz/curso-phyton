texto = input("Digite á um texto:\n")
print ("helooá world"+texto)
soma = 3 + 3
print (soma) 
x = 3
y = 15

if x == y:
    print("igual")
elif x != y:
    print("!igual")


while x < 10:
    print(x)
    x = x + 1
print("SIM\n")

array1 = ["ola",1,2,3,4,5]

for i in array1:
    print(i)

string = "Diego Silva"
print(len(string))

string.lower()
string.upper()

print(string[0:5])

#string.strip()
#string.split()
#string.find()
#string.replace()


#funçoes

def soma(a,b):
    return (a+b)

print(soma(10,50))

#arquivo = open("arquivo.txt")
#linha = arquivo.readlines()
#textoCompleto = arquivo.read()
#arquivo.close()

lista = [1,2,3]

lista.append(4)
if 100 not in lista:
    print("Nao ESTA")
del lista[2]
del lista[1:]

del lista[:]

lista2 = []
lista2.insert(2,600)
print(lista2)
#print(lista2[1])

lista.sort(reverse=True)

lista.sort()
lista.reverse()


dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com", "Udemy": "udemy.com"}
 
for chave in dicionario_sites:
    print(dicionario_sites[chave])

a = 2
b = 0
try:
    print(a/b)
except:
    print("Erro divisao")


#lista.count()
#lista.index()
#lista.remove()















