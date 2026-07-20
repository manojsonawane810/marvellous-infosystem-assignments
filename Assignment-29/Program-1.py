import os

# give filename as NewDemo1.txt or Demo1.txt or NewDemo.txt

def main():
    fileName = input("Enter a file name with extension to count the lines: ")
    
    if os.path.exists(fileName):
        print(f"File {fileName} exist")
    else:
        print(f"File {fileName} does not exist")

if __name__ == "__main__":
    main()