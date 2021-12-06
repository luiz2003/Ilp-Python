#estruras de seleção if else determinam partes do codigo que serão rodadas ou não a depender de uma condição
#else if = elif 
#if condição:
#    bloco de codigo 
# o codigo deve estar identado pra funcionar
#preço, carteira =  input().split()
#preço = int(preço)
#carteira = int(carteira)

#if carteira>=preço: # >= é um operador relacional, a resposta é um valor booleano 0 = falso 1 = verdadeiro
#    print("Você pode assistir o filme") 
#else: 
#    print("você não pode assitir o filme")
#print("Acabou o passeio")

#problema dos flippers
p, r = input().split()

p = int(p)
r = int(r)

if p == 0:
    print("C")
else:
    if r == 0:
        print("B")
    else:
        print("A")

#not and e or são operadores lógicos 
# ordem de precedência not, and ,or