def is_fibonacci_number(number):
    # Inicializa os dois primeiros números da sequência de Fibonacci
    fib1, fib2 = 0, 1
    
    # Itera até que o número de Fibonacci atual seja menor ou igual ao número informado
    while fib2 <= number:
        if fib2 == number:
            return True
        fib1, fib2 = fib2, fib1 + fib2
    
    return False

try:
    user_input = int(input("Informe um número: "))
    if is_fibonacci_number(user_input):
        print(f"{user_input} pertence à sequência de Fibonacci.")
    else:
        print(f"{user_input} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Entrada inválida. Por favor, informe um número inteiro válido.")
