def max_heapify(a, heap_size, i):
    l = 2* i
    r = 2 * i + 1

    largest = i

    if l < heap_size and a[l] > a[i]:
        largest = l

    if r < heap_size and a[r] > a[largest]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)

def buid_max_heap(a):
    heap_size = len(a)

    for i in range(heap_size // 2, 0, -1):
        max_heapify(a, heap_size, i)