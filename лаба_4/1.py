def prime_generator():
    """Замыкание для генерации простых чисел по одному."""
    primes = []  # уже найденные простые числа (запоминается между вызовами)
    num = 2
    
    def is_prime(n):
        """Проверка простоты числа на основе уже найденных простых."""
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True
    
    def get_next():
        nonlocal num
        while True:
            if is_prime(num):
                primes.append(num)
                result = num
                num += 1
                return result
            num += 1
    
    return get_next


# Пример использования
next_prime = prime_generator()

print(next_prime())  # 2
print(next_prime())  # 3
print(next_prime())  # 5
print(next_prime())  # 7
print(next_prime())  # 11
print(next_prime())  # 13
