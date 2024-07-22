#mad libs game

framework=("It was a (adjective), cold November day. \nI woke up to the (adjective) smell of (type of bird) roasting in the (room in a house) downstairs. \nI (verb in the past tense) down the stairs to see if I could help (verb) the dinner. \nMy mom said, \"See if (relative's name) needs a fresh (noun).\" \nSo I carried a tray of glasses full of (a liquid) into the (verb ending in -ing) room. \nWhen I got there, I couldn't belive my (part of the body in plural)! \nThere were (plural noun) (verb ending in -ing) on the (noun)!") 
print(framework)

def game_play():
    while True:
        ad1=input("\nType an adjective: ")
        ad2=input("\nType another adjective: ")
        bird=input("\nType a type of bird: ")
        room=input("\nType a room in a house: ")
        pastverb=input("\nType a verb in the past tense.")
        verb=input("\nType a verb: ")
        relative=input("\nType a relative's name: ")
        noun=input("\nType a noun: ")
        liquid=input("\nType any kind of liquid: ")
        verbing=input("\nType a verb ending in -ing: ")
        pluralbody=input("\nType a part of the body that's plural: ")
        pluralnoun=input("\nType a plural noun: ")
        verbing2=input("\nType another verb ending in -ing: ")
        noun2=input("\nType another noun: ")

        print("It was a " +ad1 + ", cold November day. \nI woke up to the " + ad2 + " smell of " + bird + " roasting in the " + room + " downstairs. \nI " + pastverb + " down the stairs to see if I could help " + verb + " the dinner. \nMy mom said, \"See if " + relative + " needs a fresh " + noun + ".\" \nSo I carried a tray of glasses full of " + liquid + " into the " + verbing + " room. \nWhen I got there, I couldn't belive my " + pluralbody + "! \nThere were " + pluralnoun + " " + verbing2 + " on the " + noun2 + "!") 
                
        again = input("\nWould you like to attempt this ad libs game again? Type yes to play again or anything else to stop: ")
        if again.lower() != "yes":
            print("Thanks for playing this fun game!")
            break


def okk():
    while True:
        ok=input("\nThis is your ad libs framework. The parantheses are what you are going to fill out. I will ask you to type in the according words in order. Type \"ok\" and enter when you are ready (in lowercase letters): ")
        if ok=="ok":
            game_play()
            break
        else:
            print("\nI'm sorry. What you may have entered was invalid. Try again.")

okk()







