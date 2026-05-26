import sys
import bubble_sort_demo

numbers = [int(value) for value in sys.argv[1:]]

result = bubble_sort_demo.bubble_sort(numbers)
print("Sorted array is:", result)