import re

# data from txt files and create a list with them 
# with open ("C:\\Users\\Bogdan Madalina\\Desktop\\Python\\Advent\\day4\\test_data.txt") as input_data:
with open ("C:\\Users\\Bogdan Madalina\\Desktop\\Python\\Advent\\day4\\input_data.txt") as input_data:
    line_of_interest = []
    for line in input_data:
        new_line = (line.rstrip("\n"))
        line_of_interest.append(new_line)

# print(line_of_interest)
print(len(line_of_interest))
def compair_pairs(pair1,pair2):
    count = 0
    for num1 in pair1:
        for num2 in pair2:
            if(num1 == num2):
                count+=1
                # print(num1,num2)
                break
    #for first part
    # if(len(pair1)==count or len(pair2)==count):

    #for second part
    if(count >= 1):
        return 1
    else:
        return 0
    
total = 0
for line in line_of_interest:
    #find all the numbers from every line in order, then use the order to create first and second pair
    new_data = [int(s) for s in re.findall(r'\b\d+\b', line)]
    pair1 = list(range(new_data[0],new_data[1]+1))
    pair2 = list(range(new_data[2],new_data[3]+1))
    total+= compair_pairs(pair1,pair2)

print(total) 