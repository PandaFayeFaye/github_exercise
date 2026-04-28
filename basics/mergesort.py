def merge(left, right):
    print("Merging...")
    print(f"left: {left}")
    print(f"right: {right}")
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    print(f"merged: {merged}")
    return merged


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    print(f"array: {arr}")
    m = len(arr) // 2
    print(f"m: {m}")
    left = mergesort(arr[:m])
    right = mergesort(arr[m:])
    return merge(left, right)


if __name__ == "__main__":
    print("Enter numbers, separated by ',':", end=" ")
    s = input().strip()
    input_list = s.split(",")
    input_list = [x.strip() for x in input_list]
    print(f"input_list: {input_list}")

    value_list = [int(x) for x in input_list]
    print(f"value_list: {value_list}")

    result = mergesort(value_list)
    print(result)