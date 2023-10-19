import time, random
from colorama import Fore
drills_t = dict()
drills_t_func = list()
# Difficulty; Materials; position; amount of people
#start
drills_t["1. Skill Goal"] = "Medium; Ball, Marked Goal; Striker, Winger; 1 person minimum"
def Skill_Goal():
  print(Fore.YELLOW+"\nStart from differnt positions outside the box. Perform 3-5 skills moves while dribbling in and shoot on goal while not too close to the goal. Do this 10 times.")
drills_t_func.append(Skill_Goal)
#end
#start
drills_t["2. Goal Points"] = "Medium; Ball, Marked Goal; Striker; 1 person minimum"
def Goal_Points():
  print(Fore.YELLOW+"\nShoot at goal from the PK line, with or without keeper(With keeper is harder). If you score in any of the corners, you get 5 points. If you score on the left or right side, you get 3 points. If you miss or if it is saved it is -2 points. If you score in the center of the goal, it is -3. If you hit the post it is +1. If you score at the top of the goal, it is +2. You must try to get 50 points.")
  shots = 0
  points = 0
  while points <= 50:
    shots = shots + 1
    value = int(input("Where did your shot go? 1. Corner, 2. Side(L or R), 3. Center, 4. Miss or Save, 5. Post, 6. Top"))
    if value == 1:
      points = points + 5
    elif value == 2:
      points = points + 3
    elif value == 3:
      points = points - 3
    elif value == 4:
      points = points - 2
    elif value == 5:
      points = points + 1
    elif value == 6:
      points = points + 2
  print(Fore.GREEN+"\nYou took " + shots + " shots to reach 50 points!")
drills_t_func.append(Goal_Points)
#end
