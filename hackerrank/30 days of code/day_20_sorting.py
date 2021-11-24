def bubble_sort(a):
    num_swap = 0
    for i in range(len(a) - 1):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                num_swap += 1
    display(num_swap, a[0], a[-1])


def display(num_swap, first_elem, last_elem):
    print(f'Array is sorted in {num_swap} swaps.')
    print(f'First Element: {first_elem}')
    print(f'Last Element: {last_elem}')


bubble_sort([1, 2, 3])   # 0
bubble_sort([3, 2, 1])   # 3
