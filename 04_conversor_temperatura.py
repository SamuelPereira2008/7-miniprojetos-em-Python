def converter_temp():
    print("=== Conversor de Temperatura ===")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Celsius para Kelvin")

    opcao = int(input("Escolha uma opção: "))
    valor = float(input("Digite a temperatura: "))

    if opcao == 1:
        print("Resultado:", (valor * 9/5) + 32, "°F")
    elif opcao == 2:
        print("Resultado:", (valor - 32) * 5/9, "°C")
    elif opcao == 3:
        print("Resultado:", valor + 273.15, "K")
    else:
        print("Opção inválida!")

converter_temp()
