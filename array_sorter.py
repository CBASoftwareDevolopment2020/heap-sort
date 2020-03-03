import util


class ArraySorter:
    def __init__(self, items: list, size: int):
        self.items = items
        self.size = size

        for i in range(self.size, -1, -1):
            util.max_heapify(self.items, self.size, i)

    def enqueue(self, item: object):
        self.items.append(item)
        self.size += 1

        for i in range(self.size, -1, -1):
            util.max_heapify(self.items, self.size, i)

    def dequeue(self) -> object:
        item = self.items.pop(0)
        self.size -= 1

        for i in range(self.size, -1, -1):
            util.max_heapify(self.items, self.size, i)

        return item

    def sort_ascending(self) -> list:
        data = self.items.copy()
        n = len(data)
        if n < 2:
            return data

        for i in range(n, -1, -1):
            util.max_heapify(data, n, i)

        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            util.max_heapify(data, i, 0)

        return data

    def sort_descending(self) -> list:
        data = self.items.copy()
        n = len(data)
        if n < 2:
            return data

        for i in range(n, -1, -1):
            util.min_heapify(data, n, i)

        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            util.min_heapify(data, i, 0)

        return data

    def sort(self, comparator: callable) -> list:
        def heapify(data: list, n: int, i: int, comparator: callable):
            prioritised = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and comparator(data[left], data[prioritised]):
                prioritised = left
            if right < n and comparator(data[right], data[prioritised]):
                prioritised = right

            if prioritised != i:
                data[i], data[prioritised] = data[prioritised], data[i]
                heapify(data, n, prioritised, comparator)

        data = self.items.copy()
        n = len(data)
        if n < 2:
            return data

        for i in range(n, -1, -1):
            heapify(data, n, i, comparator)

        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            heapify(data, i, 0, comparator)

        return data


if __name__ == '__main__':
    import random

    n = 10
    items = random.choices(range(10, 100), k=n)
    array_sorter = ArraySorter(items, n)

    # print(array_sorter.items)
    # print(util.is_max_heap(array_sorter.items))
    #
    # for i in range(20):
    #     item = round((i + 1) * random.random())
    #     array_sorter.enqueue(item)
    # print(array_sorter.items)
    # print(util.is_max_heap(array_sorter.items))
    #
    # print(array_sorter.dequeue())
    # print(util.is_max_heap(array_sorter.items))

    # util.print_heap(array_sorter.items)

    # print(array_sorter.sort_ascending())
    # print(array_sorter.sort_descending())

    print(array_sorter.sort(lambda x, y: x > y))
