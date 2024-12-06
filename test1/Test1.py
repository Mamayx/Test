
def circular_array_path(n, m):
    # Создаем круговой массив
    circular_array = list(range(1, n + 1))

    # Начальная позиция
    start_index = 0
    path = []

    # Пока не вернемся к началу
    while True:
        # Добавляем текущий элемент в путь
        path.append(circular_array[start_index])

        # Вычисляем новый индекс
        start_index = (start_index + m - 1) % n

        # Если вернулись к началу, выходим из цикла
        if start_index == 0:
            break

    return ''.join(map(str, path))

# Пример использования функции
n = 5
m = 4
result = circular_array_path(n, m)
print(result)  # Ожидаемый вывод: 14253

