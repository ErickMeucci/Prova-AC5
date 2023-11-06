carrinho = []

# Ler produtos iniciais, se houver
produtos_iniciais = input().split()
carrinho.extend(map(int, produtos_iniciais))

while True:
    comando = input()
    if comando == "encerrar":
        break
    elif comando.startswith("adicionar"):
        _, codigo = comando.split()
        carrinho.append(int(codigo))
    elif comando.startswith("remover"):
        _, codigo = comando.split()
        codigo = int(codigo)
        if codigo in carrinho:
            carrinho.remove(codigo)
        else:
            print(f"código {codigo} não encontrado")
    elif comando == "exibir":
        carrinho.sort()
        print(" ".join(map(str, carrinho)))

# Exibir o carrinho no final
carrinho.sort()
print(" ".join(map(str, carrinho)))
