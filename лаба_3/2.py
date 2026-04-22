def calculate_v(n):
    """
    Вычисляет v_n по рекуррентной формуле:
    v_i = (i+1)/(i^2+1) * v_{i-1} - v_{i-2} * v_{i-3}
    
    Параметры:
    n — индекс нужного элемента (n >= 1)
    
    Возвращает:
    значение v_n
    """
    if n == 1 or n == 2:
        return 0.0
    if n == 3:
        return 1.5
    
    # Инициализация трёх последних значений
    # v_{i-3}, v_{i-2}, v_{i-1}
    v_minus_3 = 0.0   # v_1
    v_minus_2 = 0.0   # v_2
    v_minus_1 = 1.5   # v_3
    
    # Вычисляем с i = 4 до n
    for i in range(4, n + 1):
        # Вычисляем новое значение по формуле
        v_new = ((i + 1) / (i ** 2 + 1)) * v_minus_1 - v_minus_2 * v_minus_3
        
        # Сдвигаем переменные для следующей итерации
        v_minus_3 = v_minus_2
        v_minus_2 = v_minus_1
        v_minus_1 = v_new
    
    return v_minus_1


# Пример использования
for n in range(1, 11):
    print(f"v_{n} = {calculate_v(n)}")
