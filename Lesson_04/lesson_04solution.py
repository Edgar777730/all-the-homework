"""Домашнее задание № 4. Две задачи на изученные приёмы."""


def boats_needed(weights, limit):
    """Минимум лодок грузоподъёмности limit; исходный список не меняется."""
    # Сортируем копию, чтобы не портить входной список.
    ordered = sorted(weights)

    lo, hi = 0, len(ordered) - 1
    count = 0

    while lo <= hi:
        # Пробуем посадить самого лёгкого к самому тяжёлому.
        # Если вдвоём не влезают — лёгкий остаётся на следующий круг,
        # а тяжёлый уезжает один.
        if lo < hi and ordered[lo] + ordered[hi] <= limit:
            lo += 1

        # Тяжёлый занимает лодку в любом случае.
        hi -= 1
        count += 1

    return count


def evens_first(nums):
    """Чётные — влево, нечётные — вправо; перестановка на месте."""
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        # Двигаем lo, пока слева стоит чётное.
        while lo < hi and nums[lo] % 2 == 0:
            lo += 1

        # Двигаем hi, пока справа стоит нечётное.
        while lo < hi and nums[hi] % 2 != 0:
            hi -= 1

        # Нашли пару «нечётное слева, чётное справа» — меняем.
        if lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1