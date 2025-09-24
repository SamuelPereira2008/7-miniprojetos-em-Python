print("=== Chatbot Simples ===")
print("Digite 'sair' para encerrar.")

respostas = {
    "oi": "Olá! Como você está?",
    "tudo bem": "Estou bem, obrigado por perguntar! 😊",
    "qual seu nome": "Sou um chatbot simples feito em Python!",
    "python": "Python é incrível para automação e projetos rápidos!",
}

while True:
    user = input("Você: ").lower()
    if user == "sair":
        print("Chatbot: Até mais! 👋")
        break
    resposta = respostas.get(user, "Desculpe, não entendi...")
    print("Chatbot:", resposta)
