from word2number import w2n

f = open('./input.txt','r')

arr = []

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] + [str(i) for i in range(10)]

def find_numbers(string, terms):
    found = []
    for i in range(len(string)):
        for term in terms:
            if string.startswith(term, i):
                found.append(term)
    return found

for line in f:
    num_array = find_numbers(line,numbers)

    if len(num_array) == 1:
        try:
            arr.append(int(num_array[0]*2))
        except:
            arr.append(str(w2n.word_to_num(num_array[0]))*2)
    else:
        first_last = [num_array[0], num_array.pop()]
        converted = []
        for number in first_last:
            try:
                converted.append(str(int(number)))
            except:
                converted.append(str(w2n.word_to_num(number)))
        joined = converted[0] + converted[1]
        arr.append(int(joined))
print(sum(arr))