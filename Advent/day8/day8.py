import re

# with open ("C:\\Users\\Bogdan Madalina\\Desktop\\Python\\Advent\\day8\\test_data.txt") as input_data:
with open ("C:\\Users\\Bogdan Madalina\\Desktop\\Python\\Advent\\day8\\input_data.txt") as input_data:
    line_of_interest = []
    for line in input_data:
        new_line = (line.rstrip("\n"))
        individual_num = []        
        for num in new_line:
            individual_num.append(int(num))
        line_of_interest.append(individual_num)

# print(len(line_of_interest))
# print(len(line_of_interest[0]))
# print(line_of_interest)

def column_list(matrix, i):
    return [row[i] for row in matrix]
  
def check_distance(new_list,number):          
    score = 0
    for elements in new_list:
        if number <= elements:
            score = new_list.index(elements) + 1
            break
        # elif(number == elements):
        #     break
        else:
            score = len(new_list)
            
    return score
# for part 2
def visibility(value,column,row):
    # if the value is the smallest, there is no visibility
    # up list needs to be reverted
    up = column_list(value, row)[:column]
    up = up[::-1]
    down = column_list(value, row)[column+1:]
    # left list needs to be reverted
    left = value[column][:row]
    left = left[::-1]
    right = value[column][row+1:]

    # print(value[column][row])
    # print(up)
    # print(left)
    # print(right)
    # print(down)
    # print("\n")
    
    up_score = check_distance(up,value[column][row])
    down_score = check_distance(down,value[column][row])
    left_score = check_distance(left,value[column][row])
    right_score = check_distance(right,value[column][row])
    # print(up_score)
    # print(left_score)
    # print(down_score)
    # print(right_score)
    # print("\n")
    return up_score * down_score * left_score * right_score
# For part 1
# def visibility(value,column,row):
#     # if the value is the smallest, there is no visibility
#     # up list needs to be reverted
#     up = max(column_list(value, row)[:column])
#     down = max(column_list(value, row)[column+1:])
#     # left list needs to be reverted
#     left = max(value[column][:row])
#     right = max(value[column][row+1:])
# #     print(f"Raw max value: {row_check}")
# #     print(f"Colomn max value: {colomn_check}")
# #     print(value[column][row])
#     if value[column][row] <= min(up, down, left, right):
# #         print(False ,value[column][row])
#         return False
#     else:
# #         print(True,value[column][row])
#         return True
      
total = 0
for lists in range(len(line_of_interest)):
    for num in range(len(line_of_interest[lists])):
        colomn = lists
        row = num 
        number = line_of_interest[colomn][row]
#         print(f"The  row is{row}")
        # to remove the margins
        # if (lists in [0,4] or num in [0,4]):
        if (lists in [0,98] or num in [0,98]):
#         print(line_of_interest[lists][num])
#             print(number)
#             print("\n")
            # total +=1
            continue
        # elif(visibility(line_of_interest,colomn,row)):
        else:
          scenic_score = visibility(line_of_interest,colomn,row)
          if scenic_score > total:
            total = scenic_score
          # print(f"For number {number} scenic score is {scenic_score} \n")

print(f"the total is:{total}")