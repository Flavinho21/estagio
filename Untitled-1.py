def fibonacci_sequence(n):
    """
    Retorna a sequência de Fibonacci até o número n.
    """
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def is_fibonacci_number(n):
    """
    Retorna True se o número n pertence à sequência de Fibonacci, False caso contrário.
    """
    fib = fibonacci_sequence(n)
    return n in fib

# Exemplo de uso
n = int(input("Digite um número: "))
fib = fibonacci_sequence(n)
if is_fibonacci_number(n):
    print(f"O número {n} pertence à sequência de Fibonacci: {fib}")
else:
    print(f"O número {n} não pertence à sequência de Fibonacci: {fib}")
