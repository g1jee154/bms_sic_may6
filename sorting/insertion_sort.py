import sys
import insertion_sort_demo

numbers = [int(value) for value in sys.argv[1:]]

result = insertion_sort_demo.insertion(numbers)
print("sorted result: ",result)