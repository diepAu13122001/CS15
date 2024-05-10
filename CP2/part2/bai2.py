a = [5, 1, 8, 92, -1, 30]

# selection: tim item min => chuyen ra truoc
# bubble: tim item lon hon item truoc => chuyen ra sau
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]  # swap
    return arr


def selection_sort(arr):
    for i in range(len(arr)-1):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr
# ------------------------------------
print("Original list:")
for i in range(len(a)):
    print(a[i], end=" ")

print("\nSorted list:")
# for i in bubble_sort(a):
for i in selection_sort(a):
    print(i, end=" ")