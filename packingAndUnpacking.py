#unpack to iterable elements // works in strings as well
nums = [1,2,3,5,6,4]
print(nums)
#gives [1, 2, 3, 5, 6, 4]
print(*nums)
#gives 1 2 3 5 6 4

str = "abcdef"
print(str)
#gives abcdef
print(*str)
#gives a b c d e f
################################

def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total
