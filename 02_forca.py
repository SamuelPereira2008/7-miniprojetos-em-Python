import random

palavras = ["python", "programacao", "desenvolvedor", "algoritmo", "computador"]
palavra = random.choice(palavras)
tentativas = 6
letras_adivinhadas = []

print("=== Jogo da Forca ===")

while tentativas > 0:
    palavra_oculta = "".join([letra if letra in letras_adivinhadas else "_" for letra in palavra])
    print("Palavra:", palavra_oculta)

    if palavra_oculta == palavra:
        print("Parabéns, você venceu! 🎉")
        break

    tentativa = input("Digite uma letra: ").lower()
    if tentativa in palavra:
        letras_adivinhadas.append(tentativa)
    else:
        tentativas -= 1
        print(f"Letra errada. Tentativas restantes: {tentativas}")

if tentativas == 0:
    print(f"Você perdeu! A palavra era: {palavra}")
