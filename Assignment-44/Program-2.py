import pandas as pd

def main():
    border = "-"*50
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82]
    }


    dataframe = pd.DataFrame(data)
    print("Data is : ")
    for df in dataframe:
        print(f"Values of {df} are :")
        print(f"{dataframe[df]}")
    
    print(border)

    print("Descriptive statistics of data is : ")
    print(dataframe.describe())

if __name__ == "__main__":
    main()