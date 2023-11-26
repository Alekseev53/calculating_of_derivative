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

def higher_order_method_new(f, x, h):
    # Первоначальное приближение с шагом h
    D1 = (f(x + h) - f(x - h)) / (2 * h)

    # Второе приближение с шагом h/2
    h2 = h / 2
    D2 = (f(x + h2) - f(x - h2)) / (2 * h2)

    # Экстраполяция Ричардсона для D1 и D2
    D2_extrapolated = D2 + (D2 - D1) / 3

    # Третье приближение с шагом h/4
    h4 = h / 4
    D3 = (f(x + h4) - f(x - h4)) / (2 * h4)

    # Финальная экстраполяция Ричардсона с D2_extrapolated и D3
    D3_extrapolated = D3 + (D3 - D2_extrapolated) / 3

    return D3_extrapolated
