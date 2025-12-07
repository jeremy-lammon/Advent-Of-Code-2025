
banks = []
with open('day3_battery.txt') as file:
    line = file.readline()
    while line:
        banks.append(line)
        line = file.readline()


def part1():
    total = 0
    for bank in banks:
        bank = str(int(bank))
        Highest_Index = 0
        Next_Highest_Index = 1
        for i in range(len(bank)-1):
            if bank[i] > bank[Highest_Index]:
                Highest_Index = i
        Next_Highest_Index = i + 1
        for i in range(Highest_Index+1, len(bank)):
            if bank[i] > bank[Next_Highest_Index]:
                Next_Highest_Index = i
        number = int(bank[Highest_Index] + bank[Next_Highest_Index])
        total += number
    print("TOTAL:",total)


def SearchBank(Bank: str, Start:int, End:int) -> int:
    Highest_Index = Start
    print("SEARCHING HIGHEST INDEX [LOW, HIGH]", Start, End)
    for i in range(Start, End):
        if Bank[i] > Bank[Highest_Index]:
            Highest_Index = i
    return Highest_Index
def part2():
    total = 0
    for bank in banks:
        bank = str(int(bank))
        print(len(bank))
        numberstring: str = ""
        Last_Highest_Index = -1
        while len(numberstring) < 12:
            Last_Highest_Index = SearchBank(bank, Last_Highest_Index+1, len(bank)-(11-len(numberstring)))
            numberstring = numberstring + bank[Last_Highest_Index]
        number = int(numberstring)
        total += number
        print(bank)
        print(number)
    print("TOTAL:", number)
        






if __name__ == "__main__":
    part2()