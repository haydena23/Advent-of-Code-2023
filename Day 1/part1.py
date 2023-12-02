import re

# Open input
f = open('./input.txt','r')

# Define array to store nums
arr = []

# For each line
for line in f:
    # Find all of the numbers in line
    num = re.findall(r'\d',line)
    # print(num)
    # If only one number, just use that twice
    if len(num) == 1:
        arr.append(int(num[0] + num[0]))
    # If multiple numbers, grab the first, last, add them
    else:
        arr.append(int(num[0] + num.pop()))

print(sum(arr))
