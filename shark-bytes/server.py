def main():
    #Define constants
    PASSWORD = "ILoveBroncoSec<3"
    FLAG = "broncosec{n3tc47_15n'7_3ncryp73d}"
    
    print("*opens slit in door*")
    guess = input("What's the password?")
    
    if guess == PASSWORD:
        print("Welcome to Shark Bytes, here's a flag: " + FLAG)
        return
    else:
        print("*slams slit shut*")
        return

if __name__ == "__main__":
    main()