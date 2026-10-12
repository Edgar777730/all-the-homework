"""Домашнее задание № 5. Скользящее окно фиксированного размера."""


def step_score(steps, k, lower, upper):
    """Очки фитнес-браслета: сумма очков по всем окнам длины k."""
    n = len(steps)

    # Первое окно собираем напрямую, дальше — двигаем границы.
    acc = sum(steps[:k])
    score = 0

    if acc < lower:
        score = -1
    elif acc > upper:
        score = 1

    # На каждом шаге добавляем вошедший элемент и убираем вышедший.
    for i in range(k, n):
        acc = acc + steps[i] - steps[i - k]
        if acc < lower:
            score = score - 1
        elif acc > upper:
            score = score + 1

    return score


def decrypt(code, k):
    """Расшифровать круговой код: сумма k соседних чисел для каждой позиции."""
    n = len(code)

    if k == 0:
        return [0] * n

    answer = [0] * n

    if k < 0:
        # Предыдущие числа: смотрим на |k| позиций назад.
        size = -k
        acc = 0
        for j in range(1, size + 1):
            acc += code[(n - j) % n]

        answer[0] = acc
        for i in range(1, n):
            # Уходит число на расстоянии size, приходит предыдущее.
            acc -= code[(i - size - 1) % n]
            acc += code[(i - 1) % n]
            answer[i] = acc

    else:
        # Следующие числа: смотрим вперёд на k позиций.
        acc = 0
        for j in range(1, k + 1):
            acc += code[j % n]

        answer[0] = acc
        for i in range(1, n):
            # Уходит первое из окна, приходит следующее по кругу.
            acc -= code[i % n]
            acc += code[(i + k) % n]
            answer[i] = acc

    return answer