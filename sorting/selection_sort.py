import sys
import selection_sort_demo

numbers = [int (value) for value in sys.argv[1:]]

result=selection_sort_demo.selection(numbers)
print("sorted list: ",result)