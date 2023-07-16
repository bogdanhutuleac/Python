with open ("C:\\Users\\Bogdan Madalina\\Desktop\\Python\\Advent\\day3\\test_data.txt") as input_data:
# with open ("C:\\Users\\Bogdan Madalina\\Desktop\\Python\\Advent\\day3\\input_data.txt") as input_data:
    line_of_letters = []
    for line in input_data:
        new_line = (line.rstrip("\n"))
        line_of_letters.append(new_line)

subList = [line_of_letters[n:n+3] for n in range(0, len(line_of_letters), 3)]
print(line_of_letters)
print(subList)

#to keep a track of priority order numbers
total = []

#Transform lower letter to number based on ASCI code
def lower_letter_num (letter):
    return ord(letter) - 96

#Transform upper letter to number based on ASCI code and the problem data
def upper_letter_num (letter):
    return ord(letter) - 64 + 26

#for every letter
def num_to_print(letter):
    if(letter.isupper()):
        return upper_letter_num(letter)
    else:
        return lower_letter_num(letter)
    
#will take 2 halfs of every line and compare the letters between them
def items_in_both(first_half, second_half,third_half):
    #iterate trough first line
    for item_in_first in first_half:
        # compare item from first line with every letter from second line
        for item_in_second in second_half:
            if(item_in_first == item_in_second):
                # if there is a match, compare it with the letters from the third line
                for item_in_third in third_half:
                    if(item_in_second == item_in_third):
                        return num_to_print(item_in_first)
            
for lines in subList:
    first_half = [letter for letter in lines[0]]
    second_half = [letter for letter in lines[1]]
    third_half = [letter for letter in lines[2]]
    total.append(items_in_both(first_half,second_half,third_half))

print(sum(total))