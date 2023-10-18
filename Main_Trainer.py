import time, random
from colorama import Fore
import Mental as m
import Physical as p
import Technical as t
print(Fore.BLUE+"Football Trainer - OXH Studios")
sections = ["Physical", "Mental", "Technical"]
print("\nWhich ability would you like to train? (Type number...)")
print(sections)
ability = int(input())
try:
    print("\n" + str(sections[ability - 1]))
    print(Fore.YELLOW+"\nDrills:")
    if ability == 1:
        for drill in p.drills_p:
            print("\t" + str(drill) + " : " + str(p.drills_p[drill]))
            drill_choice = int(input("\nWhich drill would you like to do (#)?\t"))
            p.drills_p_func[drill_choice-1]()
    elif ability == 2:
        for drill in m.drills_m:
            print("\t" + str(drill) + " : " + str(m.drills_m[drill]))
            drill_choice = int(input("\nWhich drill would you like to do (#)?\t"))
            m.drills_m_func[drill_choice-1]()
    elif ability == 3:
        for drill in t.drills_t:
            print("\t" + str(drill) + " : " + str(t.drills_t[drill]))
            drill_choice = int(input("\nWhich drill would you like to do (#)?\t"))
            t.drills_t_func[drill_choice-1]()
except:
    print(Fore.RED+"\nInvalid Input\n")
    exit() #end of program