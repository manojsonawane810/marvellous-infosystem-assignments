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
    print(dataframe)
    print(border)

    print("Adding \"Total\" column for total of all marks in dataframe: ")
    print(border)
    dataframe["Total"] = dataframe[["Math", "Science", "English"]].sum(axis=1)
    print(border)

    print("Students who scored more than 85 in Science: ")

    dataframe = dataframe[dataframe["Science"] > 85]

    print(f"{dataframe}")
    print(border)

if __name__ == "__main__":
    main()