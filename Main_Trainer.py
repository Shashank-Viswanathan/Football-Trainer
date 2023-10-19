import time, random
from colorama import Fore
import file1 as f1#edit
import file2 as f2#edit
import file3 as f3#edit
#You can add more files
while True:
    print(Fore.BLUE+"Sports Trainer - OXH Studios")#edit
    sections = ["file1", "file2", "file3"]#edit
    print("\nWhich ability would you like to train? (Type number...)")
    print(sections)
    ability = int(input())
    try:
        print("\n" + str(sections[ability - 1]))
        print(Fore.YELLOW+"\nDrills:")
        if ability == 1:#edit
            for drill in f1.drills_f1:
                print("\t" + str(drill) + " : " + str(f1.drills_f1[drill]))
                drill_choice = int(input("\nWhich drill would you like to do (#)?\t"))
                f1.drills_f1_func[drill_choice-1]()
        elif f2 == 2:#edit
            for drill in f2.drills_m:
                print("\t" + str(drill) + " : " + str(f2.drills_f2[drill]))
                drill_choice = int(input("\nWhich drill would you like to do (#)?\t"))
                f2.drills_f2_func[drill_choice-1]()
        elif ability == 3:#edit
            for drill in f3.drills_f3:
                print("\t" + str(drill) + " : " + str(f3.drills_f3[drill]))
                drill_choice = int(input("\nWhich drill would you like to do (#)?\t"))
                f3.drills_f3_func[drill_choice-1]()
    except:
        print(Fore.RED+"\nInvalid Input\n")
        continue #restarts program
