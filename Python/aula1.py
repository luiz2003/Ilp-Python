from math import * # importa todas as funções matemáticas (seno, cos, tg etc etc)

num1 = 10 #atribui o valor a variável
num2 = 20

soma = num1 + num2 #soma das duas variáveis

# operações são  + soma, - diferença, * multiplicação, / divisão  // divisão inteira,  % resto de divisão
# ** potenciação

print (soma)
print("Ola mundo")
# precedência: ordem de execução das operações 1- Parênteses 2- Multiplicações/Divisões 3-Soma/Subtração
# duas operações do mesmo nível : da ordem esquerda para direita

#entrada = lê dados
#saida = mostra os dados processados função : print ()
#para formatar as casas decimais usando a função format(var,".xf"), em que x é o número de casas decimais
print("A sua soma é",soma) #usamos isso pra incorporar variáveis no resultado

print("Oi, ")
print("pessoal") # o print quebra a linha

print("Oi ",end="") #use ,end="" para evitar a quebra
print("pessoal")

#res = float(input()) #pega um float do input e atribui a res

#split() separa o input em cada espaço em branco e atribui cada uma a uma variavel diferente
a, b, c = input().split()
a =int(a)
b = int(b)
c = int(c) # converta as variáveis pra int pois o split() pega pra string por padrão
print(a+b+c)