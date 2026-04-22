# Границы отрезка
LOWER = 400_000_000
UPPER = 600_000_000

# Список для найденных чисел
results = []

# m — чётное, значит m = 0, 2, 4, 6, ...
# Но m может быть 0? 2^0 = 1, тогда N = 3^n.
# Ограничим m разумным максимумом: 2^m <= UPPER => m <= log2(UPPER) ≈ 29.1, но m чётное → до 28.
# n — нечётное, n = 1, 3, 5, ...

for m in range(0, 30, 2):          # чётные m от 0 до 28
    power2 = 1 << m                # 2^m (битовый сдвиг)
    if power2 > UPPER:
        break
    
    n = 1                          # начнём с нечётного n=1
    while True:
        N = power2 * (3 ** n)
        if N > UPPER:
            break
        if N >= LOWER:
            results.append(N)
        n += 2                     # следующее нечётное n
        # Сортируем (хотя они уже будут в порядке возрастания из-за перебора, но на всякий случай)
results.sort()

print(f"Найдено чисел: {len(results)}")
print("Список чисел:")
for num in results:
    print(num)
