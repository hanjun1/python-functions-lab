# Part 1
# Task 1
def pokemon_contains(incoming_letter):
    if incoming_letter in "pokemon":
        return True
    else:
        return False


result1 = pokemon_contains('k')
print(result1)
result1 = pokemon_contains('o')
print(result1)

# # Task 2


def sum_two(a, b):
    answer = a + b
    return answer


result3 = sum_two(2, 3)
print(result3)
result4 = sum_two(5, 6)
print(result4)

# # Task 3


def multiply(num1, num2):
    answer = num1*num2
    return answer


result5 = multiply(10, 10)
print(result5)
result6 = multiply(5, 6)
print(result6)

# # Task 4


def multiplication(a, b):
    my_answer = a*b
    print("Calculating...")
    return my_answer


print("Let's Multiply stuff...")
answer = multiplication(5, 6)
answer = str(answer)
print("The answer is..." + answer)

# # 1. Let's Multuply stuff...
# # 2. Calculating...
# # 3. The answer is ... + answer

# # Task 5


def subtract(num1, num2):
    return num2 - num1


answer1 = subtract(1, 3)
answer2 = subtract(1, 10)
print("Answer 1:", answer1)
print("Answer 2:", answer2)

# # Task 6


def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False


answer1 = greater_than_5(10)
answer2 = greater_than_5(2)
print("Answer 1:", answer1)
print("Answer 2:", answer2)

# Part 2
# # Task 1


def sum_to(num):
    total = 0
    for i in range(1, num+1):
        total += i
    return total


answer1 = sum_to(6)
answer2 = sum_to(10)
print("Answer 1:", answer1)
print("Answer 2:", answer2)

# Task 2


def largest(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


answer1 = largest([1, 2, 3, 4, 0])
answer2 = largest([10, 4, 2, 231, 91, 54])
print("Answer 1:", answer1)
print("Answer 2:", answer2)

# Task 3


def occurances(str1, rep):
    count = 0
    len_repeated = len(rep)
    skipTo = -1
    for i in range(0, len(str1)):
        if skipTo >= i:
            continue
        if str1[i:i+len_repeated] == rep:
            count += 1
            skipTo = i + len_repeated - 1

    return count


result1 = occurances('fleep floop', 'e')   # returns 2
result2 = occurances('fleep floop', 'p')   # returns 2
result3 = occurances('fleep floop', 'ee')  # returns 1
result4 = occurances('fleep floop', 'fe')  # returns 0

print(result1, result2, result3, result4)

# Task 4


def product(*args):
    answer = 1
    for num in args:
        answer *= num
    return answer


result1 = product(-1, 4)  # returns -4
result2 = product(2, 5, 5)  # returns 50
result3 = product(4, 0.5, 5)  # returns 10.0

print(result1, result2, result3)
