# Ex31. MAKING DECISIONS

# A program allowing user to make decisions, nesting if statements within if statements

print("""You enter a dark room with 2 doors.
Do you go through door #1 or #2?""")

door = input('> ')

if door == '1':
    print("There is a giant bear eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake")
    print("2. Scream at the bear.")

    bear = input('> ')

    if bear == '1':
        print("The bear eats your face off. Good job!")
    elif bear == '2':
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs off.")

elif door == '2':
    print("You stare into endless abyss at Chtulhu's retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input('> ')

    if insanity == '1' or insanity == '2':
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("Instanity rots your eyes into a pool of muck.")

else:
    print("You stumble around and fall on a knife and die. Good Job!")
