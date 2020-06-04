def hello():
    name = getName()
    print(f"Hello {name}")

def getName():
    return input("What is your name? ")


hello()

