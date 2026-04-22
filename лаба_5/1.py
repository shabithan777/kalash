def prime_generator():
    """Генератор простых чисел (бесконечный)."""
    primes = []
    num = 2
    
    def is_prime(n):
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True
    
    while True:
        if is_prime(num):
            primes.append(num)
            yield num
        num += 1


# Суммируем первые N простых чисел
N = 10

gen = prime_generator()
total = 0

print(f"Первые {N} простых чисел:")
for i in range(N):
    prime = next(gen)
    total += prime
    print(f"{i+1}: {prime}")

print(f"\nСумма первых {N} простых чисел: {total}")