# Lê o preço do usuário
preco = float(input("Digite o preço do produto: R$ "))

# Calcula o desconto (Preço original * 0.95)
# Multiplicar por 0.95 é um atalho matemático para tirar 5%
novo_preco = preco * 0.95

print(f"O preço com 5% de desconto é: R$ {novo_preco:.2f}")
