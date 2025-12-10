import argparse
import sys

def main():
    print("Welcome to the revise app ")
    print("press -h for help")
    while True:
        try:
            user_input=input("> ").strip()
            if user_input in ["exit", "quit","q"]:
                print("\nThanks for using the revise app")
                break
        except:
            print("\nThanks for using the revise app")
            break
if __name__ == "__main__":
    main()

