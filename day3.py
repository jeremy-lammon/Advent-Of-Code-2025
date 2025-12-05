
banks = []
with open('day3_battery.txt') as file:
    line = file.readline()
    while line:
        banks.append(line)
        line = file.readline()


def main():
    total = 0
    for bank in banks:
        Highest_Index = 0
        Next_Highest_Index = 1
        for i in range(len(bank)):
            if bank[i] > bank[Highest_Index] and i != len(bank)-1:
                Highest_Index = i
            if i > Highest_Index and Next_Highest_Index < Highest_Index:
                Next_Highest_Index = i
            elif bank[i] > bank[Next_Highest_Index] and i > Highest_Index:
                Next_Highest_Index = i
        if Next_Highest_Index <= Highest_Index:
            print("WARNING IMPROPER NUMBER!")
            print(Highest_Index, Next_Highest_Index)
            print(bank)
        number = int(bank[Highest_Index] + bank[Next_Highest_Index])
        print(number)
        total += number
    print(total)





if __name__ == "__main__":
    main()