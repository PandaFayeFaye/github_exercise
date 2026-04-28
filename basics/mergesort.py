def merge(a, b):
    print("Merging...")
    print("left:", a)
    print("right:", b)
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    c += a
    c += b
    print("merged:", c)
    return c


def msort(arr):
    print("array:", arr)
    if len(arr) <= 1:
        return arr
    m = len(arr) // 2
    print("m:", m)
    left = msort(arr[:m])
    right = msort(arr[m:])
    return merge(left, right)


if __name__ == "__main__":
    print("Enter numbers, separated by ',':", end=" ")
    s = input()
    input_list = s.split(",")
    input_list = [x.strip() for x in input_list]
    print("input_list:", input_list)

    value_list = [int(x) for x in input_list]
    print("value_list:", value_list)

    result = msort(value_list)
    print(result)