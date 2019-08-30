import random
import sys
import time

# Helper Functions
def get_int_from_user(question, error_count=0):
    if error_count < 5:
        try:
            user_input = int(input(question))
        except ValueError:
            print("Please enter an integer.")
            user_input = get_int_from_user(question, error_count + 1)
        return user_input
    else:
        print("You have exceeded input error threshold!")
        sys.exit(1)


def reverse_bubble_sort(sort_me, sort_me_len):
    stop = sort_me_len - 1
    while stop > 0:
        for i in range(stop):
            if sort_me[i] > sort_me[i + 1]:
                tmp = sort_me[i]
                sort_me[i] = sort_me[i + 1]
                sort_me[i + 1] = tmp
        stop = stop - 1

def bubble_sort(sort_me, sort_me_len):
    for j in range(sort_me_len, 0, -1):
        for i in range(1, j):
            if sort_me[i-1] > sort_me[i]:
                tmp = sort_me[i]
                sort_me[i] = sort_me[i-1]
                sort_me[i-1] = tmp


def swap(a, pos1, pos2):
    tmp = a[pos1]
    a[pos1] = a[pos2]
    a[pos2] = tmp


def selection_sort(sort_me, sort_me_len):
    start = 0
    while start < sort_me_len:
        low = sort_me[start]
        low_index = start
        for i in range(start, sort_me_len):
            if low > sort_me[i]:
                low = sort_me[i]
                low_index = i

        tmp = sort_me[start]
        sort_me[start] = low
        sort_me[low_index] = tmp
        start = start + 1


# Input
list_size = get_int_from_user(
    "How large would you like the unsorted set of numbers to be: "
)

# Process
# Create random list
x = random.sample(range(0, list_size * 10), list_size)

print(f"Pre-Sort list: {x}")

start_time = time.time()
bubble_sort(x, list_size)
# reverse_bubble_sort(x, list_size)
# selection_sort(x, list_size)
stop_time = time.time()

# Output
print(f"Post-Sort list: {x}\n\n")
print(f"Elapsed Time: {stop_time - start_time}\n")
