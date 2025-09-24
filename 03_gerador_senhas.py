import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for i in range(tamanho))
    return senha

print("=== Gerador de Senhas ===")
tamanho = int(input("Digite o tamanho da senha: "))
print("Senha gerada:", gerar_senha(tamanho))
