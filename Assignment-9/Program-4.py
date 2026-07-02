def CubeNumber(no1):
    cube = no1 * no1 * no1
    print("Cube of Number is: ", cube)

def main():
    no1 = int(input("Enter a number to calculate cube:"))
    CubeNumber(no1)

if __name__ == "__main__":
    main()