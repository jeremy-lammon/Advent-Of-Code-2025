

with open("lockcombo.txt", "r") as file:
    combo = file.readline()
    total = 50
    zero_times = 0
    while combo: 
        direction = combo[0]
        size = int(combo[1:])
        #current_remainder = total % 100
        times_passed = 0
        print(total, zero_times, direction, size)
        if direction == "R":
            for i in range(size):
                total += 1
                if total % 100 == 0:
                    zero_times += 1
                

            #times_passed = (current_remainder+size) // 100
            #total += size
        else:
            for i in range(size):
                total -= 1
                if total % 100 == 0:
                    zero_times += 1
            
            #times_passed = ((100-current_remainder) + size) // 100 
            #total -= size
        zero_times += times_passed
        #if times_passed > 0:
            #print(current_remainder, direction, size, times_passed)
        #if total % 100 == 0:
            #zero_times += 1
        combo = file.readline()
    print(zero_times)
