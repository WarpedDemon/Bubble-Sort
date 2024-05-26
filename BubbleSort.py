#Internet source / insperation: https://www.programiz.com/dsa/bubble-sort

# To sort a[left. ..right]:
#1. For i = 0, ..., right-left-I, repeat:
#1.1. For j = left+1, ..., right-i, repeat:
#1.1.1. If a[j-1] is greater than a[j], swap a[j-1] and a[j].

# Test Vars: a = [4,3,4,5,2,3,4,6,8,9,10]  # O(1)

# Test Vars: 
a = ["fox", "cow", "pig", "cat", "rat", "lion", "tiger", "goat", "dog"]  # O(1)
# Test Vars: a = [23, 56, 7, 44, 768, 90, 107, 22, 45, 66, 99, 1, 12]  # O(1)

arr = a  # O(1)

def bubble_sort(arr):
    n = len(arr)  # O(1)
    copies = -6
    for i in range(n):  # O(n)
        for j in range(1, n - i):  # O(n - i)
            print(arr[j - 1], arr[j])
            copies += 2
            if arr[j - 1] > arr[j]:  # O(1)
                arr[j - 1], arr[j] = arr[j], arr[j - 1]  # O(1)
    print(copies)
    return arr

print(bubble_sort(arr)) # O(1)