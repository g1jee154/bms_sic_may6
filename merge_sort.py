import merge_sort_demo as mrgsrt
import sys

numbers = [int(value) for value in sys.argv[1:]]

result = mrgsrt.divide_array(numbers,numbers[0],numbers[len(numbers)-1])

print("After sorting answer is: ",result)
