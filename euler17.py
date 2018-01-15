# Euler Problem 17 #

# Functions
def len_numbword(lett_str):
    if len(lett_str) == 1:  # if one digit
        return cypher[''.join(lett_str)]
    elif len(lett_str) == 2:  # if two digit
        if lett_str[0] == '1':  # if *teen
            return cypher[''.join(lett_str)]
        else:  # if >19 and <100
            return cypher[''.join(lett_str[0] + '0')] + cypher[''.join(lett_str[1])]
    elif len(lett_str) == 3:  # if three digit
        return len_numbword(lett_str[0]) + lhund + len_numbword(lett_str[1:2])
    else:  # if 1000
        return lonethous


# Conversion Data
cypher = dict()
cypher['0'] =
cypher['1'] = 3  # one
cypher['2'] = 3  # two
cypher['3'] = 5  # three
cypher['4'] = 4  # four
cypher['5'] = 4  # five
cypher['6'] = 3  # six
cypher['7'] = 5  # seven
cypher['8'] = 5  # eight
cypher['9'] = 4  # nine

cypher['10'] = 3  # ten
cypher['11'] = 6  # eleven
cypher['12'] = 6  # twelve
cypher['13'] = 8  # thirteen
cypher['14'] = 8  # fourteen
cypher['15'] = 7  # fifteen
cypher['16'] = 7  # sixteen
cypher['17'] = 9  # seventeen
cypher['18'] = 8  # eighteen
cypher['19'] = 8  # nineteen

cypher['20'] = 6  # twenty
cypher['30'] = 6  # thirty
cypher['40'] = 5  # forty
cypher['50'] = 5  # fifty
cypher['60'] = 5  # sixty
cypher['70'] = 7  # seventy
cypher['80'] = 6  # eighty
cypher['90'] = 6  # ninety

lhund = 7  # hundred
lonethous = 11  # one thousand

# Main
count = 0
for j in range(1, 1000 + 1):
    lett_str = list(str(j))
    count += len_numbword(lett_str)

print(count)





