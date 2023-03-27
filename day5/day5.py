import re

# data from txt files and create a list with them 
# with open ("C:\\Users\\Bogdan Madalina\\Desktop\\Python\\Advent\\day5\\test_data.txt") as input_data:
with open ("C:\\Users\\Bogdan Madalina\\Desktop\\Python\\Advent\\day5\\input_data.txt") as input_data:
    line_of_interest = []
    for line in input_data:
        new_line = (line.rstrip("\n"))
        #will pick up only the numbers from lines
        new_data = [int(s) for s in re.findall(r'\b\d+\b', new_line)]
        line_of_interest.append(new_data)

# print(line_of_interest)

stacks ={
# "stack1" : ["Z","N"],
# "stack2" : ["M","C","D"],
# "stack3" : ["P"]
"stack1" : ["N","D","M","Q","B","P","Z"],
"stack2" : ["C","L","Z","Q","M","D","H","V"],
"stack3" : ["Q","H","R","D","V","F","Z","G"],
"stack4" : ["H","G","D","F","N"],
"stack5" : ["N","F","Q"],
"stack6" : ["D","Q","V","Z","F","B","T"],
"stack7" : ["Q","M","T","Z","D","V","S","H"],
"stack8" : ["M","G","F","P","N","Q"],
"stack9" : ["B","W","R","M"],
}

stack_keys = ["stack1","stack2","stack3","stack4","stack5","stack6","stack7","stack8","stack9"]

for lines in line_of_interest:
    #[1, 2, 1] - first el is the range, second element is stack to pop from, third is to append on

    #second element that we got from lines
    index_for_pop = lines[1] - 1

    # 3'rd element that we got from lines
    index_for_append = lines[2] - 1

    list_of_popped = []
    for moves in range(lines[0]):
      el_to_move = stacks[stack_keys[index_for_pop]].pop()
      list_of_popped.append(el_to_move)

    #to maintain the order in which they where inside every stack, I need to reverse the popped elements
    list_of_popped.reverse()
    stacks[stack_keys[index_for_append]].extend(list_of_popped)

print(stacks["stack1"][-1],stacks["stack2"][-1],stacks["stack3"][-1],stacks["stack4"][-1],stacks["stack5"][-1],stacks["stack6"][-1],stacks["stack7"][-1],stacks["stack8"][-1],stacks["stack9"][-1])
