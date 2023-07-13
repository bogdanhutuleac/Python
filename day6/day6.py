with open ("C:\\Users\\Bogdan Madalina\\Desktop\\Python\\Advent\\day6\\input_data.txt") as input_data:
# with open ("C:\\Users\\Bogdan Madalina\\Desktop\\Python\\Advent\\day6\\test_data.txt") as input_data:
    string = input_data.read()

# print (string)

# will find duplicates in a specific group
def find_duplicate(letter_group):
    for every_letter in letter_group:
        #count every letter inside the group of letter if more than 1 than we have duplicates
        counts = letter_group.count(every_letter)
        if(counts > 1):
            return True
    if(counts == 1):
        return False
    
def find_marker(string):
    start_index = 0
    # position_marker = 4 #this will be range aswell
    position_marker = 14 #this will be range aswell
    while(True):
        # print(start_index,position_marker)
        letter_group = []
        for iteration in range(start_index, position_marker):
            letter_group.append(string[iteration])
        duplicate_result = find_duplicate(letter_group)
        # print(letter_group)
        # print (duplicate_result)
        if(not duplicate_result):
            print(position_marker)
            return position_marker
        start_index += 1
        position_marker += 1 

find_marker(string)