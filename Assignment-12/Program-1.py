def checkCharType(char):
    vowels = "aeiouAEIOU"
    for c in vowels:
        print(vowels.find(char))
        if vowels.find(char) != -1:
            print(char, " is a vowel")
            break
        else:
            print(char, " is a consonent")
            break


def main():
    char = input("Enter a character: ")
    
    checkCharType(char)

if __name__ == "__main__":
    main()