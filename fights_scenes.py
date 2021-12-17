
import termcolor
answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]
throw = ["Throw", "T", "t", "throw"]
leave_it = ["leave", "leave", "leave", "leave"]

#Fight scene 1
def fight():
    print("Are you ready to Fight ?. (Yes / No)")
    ans1 = input(">>")

    if ans1 in answer_yes:
        print("\nHe is hiiting you with heavey punches and kicks, do you want knock him with special attacks (Yes / No)\n")
        ans2 = input(">>")
        if ans2 in answer_yes:
            termcolor.cprint("\nYou are a Hero !! he is almost dead",'green')

        elif ans2 in answer_no:
            termcolor.cprint("\nYou helped the oponent to win the fight. You're a COWARD..",'red')

        else:
            termcolor.cprint("\nYou typed the wrong input. Let me automate it for you", 'red')

    elif ans1 in answer_no:
        print("\nNow, he is trying to kill you. Will, you knock him down? (Yes / No)\n")
        ans3 = input(">>")

        if ans3 in answer_yes:
            termcolor.cprint("\nCongrats! He was a tough fight & You helped to save the lives.",'green')

        elif ans3 in answer_no:
            termcolor.cprint("\nYou helped the oponent to win the fight. You're a COWARD...", 'red')

        else:
            print("\nYou typed the wrong input. Let me automate it for you")

    else:
        print("\nYou typed the wrong input. Let me automate it for you")

#Fight scene 2
def fight_scene():
    print("Are you ready to Fight ?. (Throw / Leave)")
    ans1 = input(">>")

    if ans1 in throw:
        print("\nHe is hit you with a flying knee, do you want to throw a upper cut ? (Throw / Leave)\n")
        ans2 = input(">>")
        if ans2 in throw:
            print("\nNice shott !! He was almost knocked out from that shot..")
            
        elif ans2 in leave_it:
            print("\nYou helped the oponent to win, you can do much better against others. Better luck next time")
        else:
            print("\nYou typed the wrong input. Let me choose an option for you")
            print("\nHe is hit you with a flying knee, do you want to throw a upper cut ? (Throw / Leave)\n")
            ans2 = input(">>")
            if ans2 in throw:
                print("\nNice shott !! He was almost knocked out from that shot..")

    elif ans1 in leave_it:
        print("\nNow, he is trying to kill you. Are you going to defend yourself? (Throw / Leave)\n")
        ans3 = input(">>")

        if ans3 in throw:
            print("\nCongrats! It was a tough fight.")

        elif ans3 in leave_it:
            termcolor.cprint("\nYou helped the oponent to win the fight. You're a COWARD...")

        else:
            print("\nYou typed the wrong input. Let me choose an option for you")
        
    else:
        print("\nYou typed the wrong input. Let me choose an option for you!")
   