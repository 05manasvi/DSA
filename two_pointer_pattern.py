def two_sum(arr, target):
    l, r = 0, len(arr) - 1

    while l < r:
        s = arr[l] + arr[r]

        if s == target:
            return [l, r]
        elif s < target:
            l += 1
        else:
            r -= 1

    return []

arr = [1, 2, 3, 4, 5]
target = 7

print(two_sum(arr, target))