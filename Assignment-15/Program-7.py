largeName = lambda name : len(name) > 5 

def getLargeNames(names):
    return list(filter(largeName, names))

def main():
    names = ["Manoj", "Abhinandan", "Ashitosh", "Meera", "Vihaa", "Snehal", "Prashant", "Ira Bhagwat"]
    largeNameList = getLargeNames(names)
    print("Names greater than 5 characters are: ", largeNameList)

if __name__ == "__main__":
    main()