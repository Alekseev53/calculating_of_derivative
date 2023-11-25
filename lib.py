def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def higher_order_method(f, x, h):
    # Вычисляем производную с использованием центральной разностной схемы
    D1 = (f(x + h) - f(x - h)) / (2 * h)

    # Уменьшаем шаг вдвое и повторяем вычисление
    h = h / 2
    D2 = (f(x + h) - f(x - h)) / (2 * h)

    # Экстраполяция Ричардсона для улучшения точности
    return  D2 + (D2 - D1) / 3

