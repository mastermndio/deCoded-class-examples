import random
#doodoo = "shark, doo doo doo doo doo doo"
def doodoo():
    return "doo " * 6

def chooseDance():
    dances = ["dab", "woah", "shoot shoot"]
    print(random.choice(dances))

def stanza(lyrics, label):
    if label == "shark":
        placeholder = "Shark"
    else:
        placeholder = ""
        
    for num in range(3):
        print(f"{lyrics} {placeholder}, {doodoo()}")

    print(f"{lyrics} {placeholder}!")

def sing():
    sharks = ["Baby", "Mommy", "Daddy", "Grandma", "Grandpa"]
    actions = ["Let's Go Hunt", "Run Away", "Safe At Last", "It's the End"]

    for shark in sharks:
        stanza(shark, "shark")
        chooseDance()
    for action in actions:
        stanza(action, "action")
        chooseDance()


sing()


