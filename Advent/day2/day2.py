# with open ("C:\\Users\\Bogdan Madalina\\Desktop\\Python\\Advent\\day2\\test_data.txt") as input_data:
with open ("C:\\Users\\Bogdan Madalina\\Desktop\\Python\\Advent\\day2\\input_data.txt") as input_data:
    list_of_games = []
    for line in input_data:
        new_tup = (line.rstrip("\n")[0],line.rstrip("\n")[-1])
        list_of_games.append(new_tup)

# print(list_of_games)



# Create the variables to work with
player1 = {"A": "rock","B": "paper","C":"scissor"}
player2 = {"X": "rock","Y": "paper","Z": "scissor"}
game_options = ["rock", "paper","scissor"]

# second part x (rock) - lose, y(paper) = draw, z(scissor) = win
# x = win , y  = draw, z = lost
# now we compare player1[a](where a is from deconstruct of a,b) with rock 
round_score = 0
p1_total = 0
p2_total = 0
win_points = 6
draw_points = 3
lost_points = 0

# player1[a] == game_options[0]

def lost (a,b):
        global p1_total
        global p2_total
        round_score = win_points + game_options.index(a) + 1
        p1_total += round_score
        round_score = 0
        round_score = lost_points + game_options.index(b) + 1
        p2_total += round_score
        round_score = 0
        # print(p2_total)
        # return p2_total

def win(a,b):
        global p1_total
        global p2_total
        round_score = win_points + game_options.index(b) + 1
        p2_total += round_score
        round_score = 0
        round_score = lost_points + game_options.index(a) + 1
        p1_total += round_score
        round_score = 0
        # print(p2_total)

        # return p2_total


def draw(a,b):
        global p1_total
        global p2_total
        round_score =  draw_points + game_options.index(a) + 1
        p1_total += round_score
        round_score = 0 
        round_score =  draw_points + game_options.index(b) + 1
        p2_total += round_score
        round_score = 0 
        # print(p2_total)

        # return p2_total

     

for a,b in list_of_games:
    # print(player1[a])
    # print(player2[b])

    # Rock defeat scissor
    # if player1 is rock and player2 is scissor
    # if(player1[a] == "rock" and player2[b] == "scissor"):
    if(player2[b] == "scissor"):
        # new code
        # player2  = scissor(win)
        if(player1[a] == "rock"):
          win(player1[a],"paper") 

        elif(player1[a] == "paper"):
          win(player1[a],"scissor") 

        elif(player1[a] == "scissor"):
          win(player1[a],"rock") 



        #  old code
        # round_score = win + game_options.index("rock") + 1
        # p1_total += round_score
        # round_score = 0
        # round_score = lost + game_options.index("scissor") + 1
        # p2_total += round_score
        # round_score = 0
    # if player2 is rock and player1 is scissor
    # elif(player1[a] == "scissor" and player2[b] == "rock"):
    elif(player2[b] == "rock"):
        # new code
        # player2 = rock(lose)
        if(player1[a] == "rock"):
          lost(player1[a],"scissor") 

        elif(player1[a] == "paper"):
          lost(player1[a],"rock") 

        elif(player1[a] == "scissor"):
          lost(player1[a],"paper") 
        # lost(player1[a], player2[b])


        # old code
        # round_score = lost + game_options.index("scissor") + 1
        # p1_total += round_score
        # round_score = 0
        # round_score = win + game_options.index("rock") + 1
        # p2_total += round_score
        # round_score = 0

    # Scissor defeat paper
    # if player1 is scissor and player2 is paper
    # elif(player1[a] == "scissor" and player2[b] == "paper"):
    elif(player2[b] == "paper"):
        # new code
        if(player1[a] == "rock"):
          draw(player1[a],"rock") 

        elif(player1[a] == "paper"):
          draw(player1[a],"paper") 

        elif(player1[a] == "scissor"):
          draw(player1[a],"scissor") 

        # draw(player1[a], player2[b])
        
        # old code
        # round_score =  win + game_options.index("scissor") + 1
        # p1_total += round_score
        # round_score = 0
        # round_score =  lost + game_options.index("paper") + 1
        # p2_total += round_score
        # round_score = 0
    
    # if player2 is scissor and player1 is paper
    # elif(player1[a] == "paper" and player2[b] == "scissor"):
        # new code
        # win(player1[a],player2[b])
        
        # old code
        # round_score = lost + game_options.index("paper") + 1
        # p2_total += round_score
        # round_score = 0
        # round_score =  win + game_options.index("scissor") + 1
        # p1_total += round_score
        # round_score = 0
    # Paper defeat rock
    # if player1 is paper and player2 is rock
    # elif(player1[a] == "paper" and player2[b] == "rock"):
    #     round_score =  win + game_options.index("paper") + 1
    #     p2_total += round_score
    #     round_score = 0
    #     round_score =  lost + game_options.index("rock") + 1
    #     p1_total += round_score
    #     round_score = 0

    # if player2 is paper and player1 is rock
    # elif(player1[a] == "rock" and player2[b] == "paper"):
    #     round_score =  lost + game_options.index("rock") + 1
    #     p1_total += round_score
    #     round_score = 0
    #     round_score =  win + game_options.index("paper") + 1
    #     p2_total += round_score
    #     round_score = 0 

    # if it's a draw
    # elif(player1[a] == player2[b]):
    # else:
    #     round_score =  draw + game_options.index(player1.get(a)) + 1
    #     p1_total += round_score
    #     round_score = 0 
    #     round_score =  draw + game_options.index(player2.get(b)) + 1
    #     p2_total += round_score
    #     round_score = 0 
    # print(p1_total)
    # print(p2_total)


print(p2_total)
# print(game_options.index(player1.get(a)) + 1)