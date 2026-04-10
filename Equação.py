print("=== Cálculo da equação do 1º grau (ax + b = 0) ===")

while True:
    try:
        valor_a = float(input("\nDigite o valor de a: "))
        valor_b = float(input("Digite o valor de b: "))

        if valor_a != 0:
            x = -valor_b / valor_a
            print(f"\nResultado: x = {x: .2f}")

        else:
            if valor_b == 0:
                print("\nA equação é indeterminada (infinitas soluções)")
            else:
                print("\nA equação é impossível (não existe solução)")

    except ValueError:
        print("\nErro: digite apenas números válidos!")

    continuar = input("\nDeseja calcular outra equação? (s/n): ").lower()

    if continuar != "s":
        print("\nPrograma encerrado.")
        break