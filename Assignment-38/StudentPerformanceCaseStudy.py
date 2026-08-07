import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

border = "-"*50

#########################################################################
# Step1 : Load the dataset
#########################################################################

print(border)
print("Step1 : Load the dataset")
print(border)

datasetFile = "student_performance_ml.csv"

df = pd.read_csv(datasetFile)

print("Dataset loaded successfully")

#########################################################################
# Assignment Question 1 implmentation
#########################################################################

print(border)
print("Assignment Question 1 implmentation")
print(border)

print("First 5 records from dataset :")
print(df.head())

print("Last 5 records from dataset :")
print(df.tail())

print("Total number of rows in dataset are : ", df.shape[0])
print("Total number of columns in dataset are : ", df.shape[1])
print("Column names in dataset are : ")
print(list(df.columns))

for col in list(df.columns):
    print("Datatype of column ", col ," is: ", df[col].dtype)

#########################################################################
# Assignment Question 2 implmentation
#########################################################################

print(border)
print("Assignment Question 2 implmentation")
print(border)

print("Total number of students in the dataset are : ", df["FinalResult"].size)

passCount = 0
failCount = 0

for result in df["FinalResult"]:
    if result == 0:
        failCount = failCount + 1
    elif result == 1:
        passCount = passCount + 1

print("Total student passed : " , passCount)
print("Total student failed : " , failCount)

#########################################################################
# Assignment Question 3 implmentation
#########################################################################

print(border)
print("Assignment Question 3 implmentation")
print(border)

averageStudyHours = df.agg({"StudyHours":["mean"]})
print("Average study hours are : " , averageStudyHours)

averageAttendance = df.agg({"Attendance":["mean"]})
print("Average attendance is : ", averageAttendance)

print("Maximum previous score is : ", df.agg({"PreviousScore": ["max"]}))

print("Minimum sleep hours are : ", df.agg({"SleepHours":["min"]}))


#########################################################################
# Assignment Question 4 implmentation
#########################################################################

print(border)
print("Assignment Question 4 implmentation")
print(border)

distributionOfLabels = df["FinalResult"].value_counts()
print("Total number of pass and fail students are :")
print(distributionOfLabels)

passPercentage = (distributionOfLabels[1] / df["FinalResult"].size ) * 100

failPercentage = (distributionOfLabels[0] / df["FinalResult"].size ) * 100

print("Passed student percentage : ", passPercentage)
print("Failed student percentage : ", failPercentage)
print("Dataset is not balance as pass student are more than failed student.")

#########################################################################
# Assignment Question 5 implmentation
#########################################################################

print(border)
print("Assignment Question 5 implmentation")
print(border)

plt.figure(figsize=(8,6))

plt.scatter(data=df, x="StudyHours", y="FinalResult")

plt.title("Student Performance Stats")

plt.xlabel("StudyHours")
plt.ylabel("FinalResult")    

plt.grid()
plt.show()

print("Graph shows thats more study hours increases the chance of passing.")
print("We can see if study hours are more than 4 hours then students are passed.")


plt.figure(figsize=(8,6))

plt.scatter(data=df, x="Attendance", y="FinalResult")

plt.title("Student Performance Stats")

plt.xlabel("Attendance")
plt.ylabel("FinalResult")    

plt.grid()
plt.show()

print("Graph shows thats more attendence improves the finalresult.")
print("We can see if attendence is  more than 75 then students are passed.")

#########################################################################
# Assignment Question 6 implmentation
#########################################################################

print(border)
print("Assignment Question 6 implmentation")
print(border)

df["StudyHours"].hist()
plt.title("Histogram of study hours")
plt.show()

print("Histogram of StudyHours is shown")
#########################################################################
# Assignment Question 7 implmentation
#########################################################################

print(border)
print("Assignment Question 7 implmentation")
print(border)

plt.figure(figsize=(7,5))

for result in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == result]
    plt.scatter(temp["StudyHours"], temp["PreviousScore"], label = result)

    plt.title("Student Performance Stats")

    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")

plt.legend()
plt.grid()
plt.show()

print("Scatter plot of StudyHours and PreviousScore is shown")
#########################################################################
# Assignment Question 8 implmentation
#########################################################################

print(border)
print("Assignment Question 8 implmentation")
print(border)

#df.boxplot("Attendance")
plt.boxplot(df["Attendance"])
plt.title("Attendence boxplot")
plt.ylabel("Attendance")
plt.show()

print("We can see in boxplot, that there are outliers in the data which are outside the normal range")

#########################################################################
# Assignment Question 9 implmentation
#########################################################################

print(border)
print("Assignment Question 9 implmentation")
print(border)

plt.figure(figsize=(8,6))

plt.scatter(data=df, x="AssignmentsCompleted", y="FinalResult")

plt.title("Student Performance Stats")

plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult")    

plt.grid()
plt.show()

print("By looking at plot, we can say that student who have completed the less than 5 assignments are failed.")
print("And student who have completed more than 5 assignments are Passed.")

#########################################################################
# Assignment Question 10 implmentation
#########################################################################

print(border)
print("Assignment Question 10 implmentation")
print(border)

plt.figure(figsize=(8,6))

plt.scatter(data=df, x="SleepHours", y="FinalResult")

plt.title("Student Performance Stats")

plt.xlabel("SleepHours")
plt.ylabel("FinalResult")    

plt.grid()
plt.show()

print("Plot diagram shows that sleeping more than or equal to 6 hours guarantees success.")

print("Assignment 38 is completed!")