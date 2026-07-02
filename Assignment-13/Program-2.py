def areaOfCircle(radius, PI=3.14):
    area = radius * radius * PI
    return area

def main():
    radius = float(input("Enter radius of circle: "))

    area = areaOfCircle(radius)

    print("Area of circle is: ", area)

if __name__ == "__main__":
    main()