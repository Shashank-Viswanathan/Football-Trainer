import time, random
from colorama import Fore
drills_t = dict()
drills_t_func = list()
# Difficulty; Materials; position; amount of people
drills_t["1. Skill Goal"] = "Medium; Ball, Marked Goal; Striker, Winger; 1 person minimum"
def Skill_Goal():
  print(Fore.YELLOW+"\nStart from differnt positions outside the box. Perform 3-5 skills moves while dribbling in and shoot on goal while not too close to the goal. Do this 10 times.")
drills_t_func.append(Skill_Goal)