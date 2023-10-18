import time, random
from colorama import Fore
drills_p = dict()
drills_p_func = list()
# Difficulty; Materials; position; amount of people
drills_p["1. Pushup - Sprint"] = "Easy; No ball; All positions; 2 people minimum"
def Pushup_Sprint():
  print(Fore.YELLOW+"\nYou must have two people. One person in front of the other. Both do 5 push ups and the person in front must sprint to the 50 on the football field as fast as they can. The person behind must try to catch the person in front. Once you reach the end, both people switch positions and do the same back. Repeat 10 times.")
drills_p_func.append(Pushup_Sprint)