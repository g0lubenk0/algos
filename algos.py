array1 = [5, 2, 7, 2, 1]
array2 = [1, 7, 4, 2, 3, 7, 2, 13, 15, 17]


# Сортировка вставками


def insertion_sort(a):
    """
    Переносит элемент до его позиции меняя местами с элементами слева.

    :param a: Неотсортированный массив

    :return: Отсортированный массив
    """
    for i in range(len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    return a


# Cлияние


def merge(a, b):
    """
    Слияние двух отсортированных массивов.

    :param a: Отсортированный массив
    :param b: Отсортированный массив

    :returns: Слияние двух отсортированных массивов
    """
    n, m = len(a), len(b)
    i = j = 0
    c = []
    while i < n or j < m:
        if j == m or i < n and a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c


# Сортировка слиянием


def merge_sort(a):
    """
    Изначальный массив рекурсивно разбивается на подмассивы, которые отдельно сортируются,
    затем соединяются в общий массив.

    :param a: Неотсортированный массив
    :return: Отсортированный массив
    """
    n = len(a)
    if n <= 1:
        return a
    left = a[:n // 2]
    right = a[n // 2:]
    merge_sort(left)
    merge_sort(right)
    return merge(left, right)




print(insertion_sort(array1))

print(merge(insertion_sort(array1), insertion_sort(array2)))

print(merge_sort(array1))
print(merge_sort(array2))
print(merge_sort(array1 + array2))
