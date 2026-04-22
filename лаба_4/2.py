import time
import functools
from threading import Thread


def timeout(seconds):
    """
    Декоратор, который прерывает выполнение функции,
    если она работает дольше seconds секунд.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = [None]
            error = [None]
            
            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    error[0] = e
            
            thread = Thread(target=target)
            thread.daemon = True
            thread.start()
            thread.join(seconds)
            
            if thread.is_alive():
                raise TimeoutError(f"Функция '{func.__name__}' выполнялась дольше {seconds} секунд(ы)")
            
            if error[0]:
                raise error[0]
            
            return result[0]
        
        return wrapper
    return decorator


# Пример использования
@timeout(2)
def slow_function():
    """Функция, которая выполняется 5 секунд."""
    time.sleep(5)
    return "Готово!"


@timeout(3)
def fast_function():
    """Функция, которая выполняется 1 секунду."""
    time.sleep(1)
    return "Успешно!"


# Проверка
try:
    print(slow_function())
except TimeoutError as e:
    print(f"Ошибка: {e}")

try:
    print(fast_function())
except TimeoutError as e:
    print(f"Ошибка: {e}")