# with open ("C:\\Users\\Bogdan Madalina\\Desktop\\test_data.txt") as input_data:
with open ("C:\\Users\\Bogdan Madalina\\Desktop\\input_data_elf.txt") as input_data:
    numbers= []
    for line in input_data:
        numbers.append(line.rstrip("\n"))
    numbers.append("")


# print(numbers)


added_number = 0
added_list = []
for item in numbers:
    if item != "":
        added_number  += int(item)
    else:
        added_list.append(added_number)
        added_number = 0

# check_number(added_number,biggest_number)
# if added_number  > biggest_number:
#     print(f"{added_number} added vs {biggest_number} biggest")       
#     biggest_number = added_number

added_list.sort()
print(max(added_list)) 
print(added_list[-1])
# print(added_list) 
print(added_list[-1] + added_list[-2] + added_list[-3])