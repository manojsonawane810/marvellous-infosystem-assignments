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

    print("Datafram is : ", dataframe)
    print(border)

    print("Shape of dataframe is : ", dataframe.shape)
    print(border)

    print("Columns of dataframe is : ")
    print(dataframe.columns.tolist())
    print(border)

    print("Datatypes of columns are : ")
    print(dataframe.dtypes)
    print(border)

    for df in dataframe:
        print("Datatype of ", df, " is ", dataframe[df].dtype)

    print(border)

if __name__ == "__main__":
    main()