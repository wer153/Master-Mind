import random
color_list=["grey","white","green","red","yellow","blue","pink","orange"]
round=0
max_round=9
the_code = [] # computer generates random code
for i in range(4):
    the_code.append(random.choice(color_list))

instruction = "Guess the code\nex)green green black white\nthe code:"
print("There are 8 colors in this game")
print("color list:",color_list)
while True:
    round+=1
    if round>max_round:
        print("You failed :( Try again!")
        break
    else:
        print("round {}/{}".format(round,max_round+1))
        round_color=0
        round_position=0
        round_list = list(input(instruction).split())
        round_set = list(set(round_list))
        if round_list == the_code:
            print("You won! Congratulations! :)")
            break
        for i in range(len(the_code)):
            if round_list[i]==the_code[i]:
                round_position+=1
            
        for color in round_set:
            if the_code.count(color)>=1:
                round_color+=1
        print("colors matching:",round_color)
        print("positions matching:",round_position)
		
		