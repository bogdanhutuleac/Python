import re

# with open ("C:\\Users\\Bogdan Madalina\\Desktop\\Python\\Advent\\day7\\test_data.txt") as input_data:
with open ("C:\\Users\\Bogdan Madalina\\Desktop\\Python\\Advent\\day7\\input_data.txt") as input_data:
    line_of_interest = []
    for line in input_data:
        new_line = (line.rstrip("\n"))
        line_of_interest.append(new_line)

my_list = []
for element in line_of_interest:
    my_list.append(element.split())

# Initializing 
path = "/home"
dirs = {"/home": 0}

#process every comand
for comand in my_list:
    
    #Comands that starts with $
    if comand[0] =="$":
        
        #Do nothing when listing directorys or files
        if comand[1] == "ls":
            pass
        
        #Manage changing paths
        elif comand[1] == "cd":
            
            # Go back to root
            if comand[2] =="/":
                path = "/home"
            
            #Go back in the path
            elif comand[2] == "..":
                #rfind will return the index of the last "/"
                #so it will take the path up to the last / wich will be 1 step back from the shown path
                path = path[:path.rfind("/")]
            #Change path
            #elif comand[2] not in ["/",".."]:
            else:
                dir_name = comand[2]          #name of new directory
                path = path + "/" + dir_name  #geting the path
                # .update will append to the dictionary
                dirs.update({path:0})
                
    # DO nothing if the line starts with "dir":
    elif(comand[0] == "dir"):
        pass
    # Get the file size and change directory in wich it was sized
    # elif(comand[0].isdigit()):
    else:
        
        size = int(comand[0])                 #get the size of the file
        directory = path
        for i in range(path.count("/")):
            # Dictionary dirs at the key of the path update size
            dirs[directory] += size 
            # with every count of "/" wil be updated with the previous path
            directory = directory[:directory.rfind("/")]
            
# for direc in dirs:
#     print(direc, dirs[direc])

total = 0

# space required - space unused(total space - space used)
limit = 30000000 - (70000000-dirs["/home"])

valid_dirs = []
print(limit)

for directory in dirs:
  
  # part 1
  if dirs[directory] < 100000:
    # print(dirs[directory])
    total += dirs[directory]
    
  # Part2
  if limit <= dirs[directory]:
    valid_dirs.append(dirs[directory])
  smallest = min(valid_dirs)
    
print(f"Answer for part 2 will be: {smallest}")
print(f"Answer to part 1 is: {total}")