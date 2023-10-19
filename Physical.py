import time, random
from colorama import Fore
drills_p = dict()
drills_p_func = list()
# Difficulty; Materials; position; amount of people
#start
drills_p["1. Pushup - Sprint"] = "Easy; No ball; All positions; 2 people minimum"
def Pushup_Sprint():
  print(Fore.YELLOW+"\nYou must have two people. One person in front of the other. Both do 5 push ups and the person in front must sprint to the 50 on the football field as fast as they can. The person behind must try to catch the person in front. Once you reach the end, both people switch positions and do the same back. Repeat 10 times.")
drills_p_func.append(Pushup_Sprint)
#end
#start
drills_p["2. Fitness Test"] = "Hard; No ball, Full Field; All positions; 1 person minimum"
def Fitness_Test():
  print(Fore.YELLOW+"\nRun to the end of the field and back twice on the long side. Do this in 2 minutes for easiest, 1:30 for normal, and 1 minute for hard.")
  ready = input("Type e,m,h to start based on your difficulty...")
  if ready == "e":
    for second in range(120):
      print(second)
      time.sleep(1)
  elif ready == "m":
    for second in range(90):
      print(second)
      time.sleep(1)
  elif ready == "h":
    for second in range(60):
      print(second)
      time.sleep(1)
  survey = input(Fore.YELLOW+"Did you complete it? y/n\t")
  if survey == "n":
    print(Fore.LIGHTRED_EX+"\nYou must get into form...")
  elif survey == "y":
    if ready == "e" or ready == "m":
      print(Fore.GREEN+"\nGood, now try to increase the difficulty!")
    elif ready == "h":
      print(Fore.GREEN+"\nGreat! Now keep your form for your season!")
drills_p_func.append(Fitness_Test)
#end
