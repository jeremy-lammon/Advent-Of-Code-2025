
banks = []
with open('day3_battery.txt') as file:
    line = file.readline()
    while line:
        banks.append(line)
        line = file.readline()


def main():
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





if __name__ == "__main__":
    main()