def bubble_sort(arr):
    """
    冒泡排序
    每一轮把最大的元素「冒泡」到数组末尾。
    时间复杂度 O(n²)，空间复杂度 O(1)，稳定排序。
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    data = [5, 3, 8, 4, 2]
    print(f"排序前: {data}")
    print(f"排序后: {bubble_sort(data)}")
