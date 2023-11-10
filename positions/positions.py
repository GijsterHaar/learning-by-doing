
"""
write a programm that takes 12 binary numbers with 5 digits and itterate over each number per index.
So 5 itterations
With each index, when the index of all numbers is a 1 more often than a 0 we only keep those numbers
as our new positions. When it's a 0 we only keep those as our new positions. When they are
equal we keep the one with a 1 on that index. In the end we should get just one binary number: 10111
and then we want to convert it to a decimal number: 23
"""

def main():

    POSITIONS = ['00100', '11110', '10110', '10111', '10101', '01111',
                 '00111', '11100', '10000', '11001', '00010', '01010']
                 
    oxygen = get_decimal_value_from_binaries(POSITIONS, 1)
    decimal_oxygen = int(oxygen[0], 2)
    print(decimal_oxygen)

    co2_scrubber = get_decimal_value_from_binaries(POSITIONS, 2)
    decimal_co2_scrubber = int(co2_scrubber[0], 2)
    print(decimal_co2_scrubber)

    life_support_rating = get_life_support_rating(decimal_oxygen, decimal_co2_scrubber)
    print(life_support_rating)

    
def get_decimal_value_from_binaries(positions, option):
    for i in range(len(positions)):
        all_ones = [number for number in positions if number[i] == '1']
        all_zeros = [number for number in positions if number[i] == '0']
        if option == 1:
            if len(all_ones) >= len(all_zeros):
                positions = all_ones
            else:
                positions = all_zeros
        else:
            if len(all_ones) >= len(all_zeros):
                positions = all_zeros
            else:
                positions = all_ones
        if len(positions) == 1:
            break
    return positions

def get_life_support_rating(decimal_oxygen, decimal_co2_scrubber):
    return decimal_oxygen * decimal_co2_scrubber




if __name__ == '__main__':
    main()