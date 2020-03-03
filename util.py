def max_heapify(data: list, n: int, i: int):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left
    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        max_heapify(data, n, largest)


def min_heapify(data: list, n: int, i: int):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] <= data[smallest]:
        smallest = left
    if right < n and data[right] <= data[smallest]:
        smallest = right

    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        min_heapify(data, n, smallest)


def is_max_heap(a: list):
    return all(a[i] <= a[(i - 1) // 2] for i in range(1, len(a)))


def is_min_heap(a: list):
    return all(a[i] >= a[(i - 1) // 2] for i in range(1, len(a)))


def print_heap(a: list):
    items_per_line = [1]
    x = 0
    acc = 0
    while acc < len(a):
        n = 2 ** (x + 1)
        items_per_line.append(n)
        x += 1
        acc += n

    i = 1
    idx = 0
    for line in items_per_line:
        string = '  '.join([str(x) for x in a[idx:idx + line]])
        idx += line
        print(string)
        i += 1
