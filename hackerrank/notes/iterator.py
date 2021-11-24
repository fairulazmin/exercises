def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums = my_range(1, 100_000)  # [Finished in 0.991s]

# for num in nums:
#     print(num)
