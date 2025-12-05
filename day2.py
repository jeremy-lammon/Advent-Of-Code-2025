
def Part2isInvalid(num: int) -> bool:
    text_version = str(num)
    for i in range(len(text_version)):
        if i * text_version.count(text_version[0:i]) == len(text_version):
            return True
    return False


def Part1isInvalid(num: int) ->  bool:
    
    stringver = str(num)
    if len(stringver) % 2 == 1:
        return False
    
    half_mark = (len(stringver)//2)

    first_half = stringver[0:half_mark]
    second_half = stringver[half_mark:]

    return first_half == second_half


numset = ""

with open('day2_ranges.txt') as file:
    numset = file.read()
num_ranges = numset.split(',')

total = 0

for rng in num_ranges:
    this_range = rng.split('-')
    bottom = int(this_range[0])
    top = int(this_range[1])

    for i in range(bottom, top):
        if Part2isInvalid(i):
            total += i
       
print(total)

