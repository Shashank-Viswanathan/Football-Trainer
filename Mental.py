import time, random
from colorama import Fore
drills_m = dict()
drills_m_func = list()
# Difficulty; Materials; position; amount of people
drills_m["1. Timed Wall Pass"] = "Easy; Ball, Wall(s), Timer; Midfield; 1 person minimum"
def Timed_Wall_Pass():
    print(Fore.YELLOW+"\nIn this drill, you set a timer for 1 minute and pass the ball to a wall, let it bounce back and pass to a different part or a different wall. Try to quickly decide what you are passing to increase how many passes you can complete. Don't randomly pass!")
    start = input("Type enter to start...")
    for second in range(60):
      print(second)
      time.sleep(1)
    score = input("How many passes did you complete? (Try to beat your score!)\t")
    print(Fore.GREEN+"\nYou completed " + score + " passes in 1 minute!")
drills_m_func.append(Timed_Wall_Pass)
#
