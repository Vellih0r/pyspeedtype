#I want to create speedtype CLI for linux, just for fun.
#I want to start it when I bored and practice my typing :)

import sys

level = "medium"
flags = ["-h","-help","-f","-file", "-e","-easy", "-m", "-medium", "-H", "-hard"]

def flag_help():
    print("\nHELP:")
    print(" -h -help          Print this Help message")
    print("\nDIFFICULTY LEVEL:")
    print(f"current = {level}")
    print(" -e -easy          Easy level")
    print(" -m -medium        Medium level")
    print(" -H -hard          Hard level")


def set_level(input_level):
    level = input_level
    print('-'*27)
    print(f"Level set to {input_level}")
    print('-'*27)

def use_flag(flag):
        match flag:
            case "-h":
                flag_help()
            case "-help":
                flag_help()
            case "-e":
                set_level("easy")
            case "-easy":
                set_level("easy")
            case "-m":
                set_level("medium")
            case "medium":
                set_level("medium")
            case "-H":
                set_level("hard")
            case "-hard":
                set_level("hard")


def main(argv):
    if len(argv) == 1:
        print("Hello world")
    else:
        for flag in flags:
            if flag in argv:
                use_flag(flag)

if __name__ == "__main__":
    main(sys.argv)
