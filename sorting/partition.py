import partition_demo as ptd
import sys

numbers = [int(value) for value in sys.argv[1:]]

result = ptd.partition(numbers)

print("Before partition elements are: ",numbers)
print("after partition elements are: ",result)
