import random
import math
print("**************** HAND CRICKET**********************")

choose = input("ODD or EVEN :  ")

system = math.ceil(random.random()*6)
user2 = int(input(" Start The GAME by TOSS"))

print("TOSS : user : " + str(user2))
print("TOSS : system : " + str(system))

status = ""
if (choose == "EVEN" or choose == "even"):
    if((system + int(user2)) %2 ==0):
        status = input("BOWLING OR BATTING : ")
    else:
        choice = random.random()
        if(choice < 0.5):
            print("System  WON the TOSS")
            print("CHOOSE TO BATTING")
            status = "BOWLING"
        else:
            print("System WON the TOSS ")
            print(" CHOOSE TO BOWLING")
            status = "BATTING"

if (choose == "ODD" or choose =="odd"):
    if((system + int(user2)) % 2 ==1):
        status = input(" BATTING or BOWLING :")
    else:
        choice = random.random()
        if(choice < 0.5):
            print("System  WON the TOSS")
            print("CHOOSE TO BATTING")
            status = "BOWLING"
        else:
            print("System WON the TOSS ")
            print(" CHOOSE TO BOWLING")
            status = "BATTING"


score = 0
target = 1
innings = 1

while True:
    player_input = int(input("you : " + status +  " innings " + str(innings)))
    cpu_input = math.ceil(random.random() * 6)
    print("USER : " + str(player_input))
    print("SYSTEM : " + str(cpu_input))

    if(player_input == cpu_input):
        if(status == "BATTING" and innings == 1):
            status = "BOWLING"
            innings = 2
            print("***It's OUT***")
            print("TO DEFEND : " + str(score))
        elif(status == "BOWLING" and innings == 1):
            status = "BATTING"
            innings = 2
            print("***It's OUT***")
            print("TO GET : " + str(target))
        elif(status == "BATTING" and innings == 2):
            print("***It's OUT***")
            print("--**--**-- SYSTEM WON THE MATCH --**--**--")
            print(" ********* MATCH FINISHED **********")
            break
        elif(status == "BOWLING" and innings == 2):
            print("***It's OUT***")
            print("^^^^^^^^^^^^^ USER WON the MATCH ^^^^^^^^")
            print(" ********* MATCH FINISHED **********")
            break
    else:
        if(status == "BATTING" and innings == 1):
            score = score + player_input
            print("SCORE : " + str(score))
        elif(status == "BATTING" and innings == 2):
            if(target - player_input > 0):
                target = target - player_input
                print("TO GET : " + str(target))
            else:
                print("....USER WON the MATCH....")
                break
        elif(status == "BOWLING" and innings == 1):
            target = target + cpu_input
            print("SCORE : " + str(target))
        elif(status == "BOWLING" and innings == 2):
            if(score - cpu_input > 0):
                score = score - cpu_input
                print("TO DEFEND : " + str(score))
            else:
                print("...USER LOST the MATCH .....")
                break
