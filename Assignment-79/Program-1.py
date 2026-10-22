import tkinter as tk

root = tk.Tk()

root.title("Addition of numbers")
root.geometry("600x400")

header = tk.Label(root, text="Summation application", font=("Arial", 18, "bold"))
header.pack(pady=10)

tk.Label(root, text="Enter first number").pack()
num1 = tk.Entry(root)
num1.pack()

tk.Label(root, text="Enter second number").pack()
num2 = tk.Entry(root)
num2.pack()

def addition():
    no1 = int(num1.get())
    no2 = int(num2.get())
    sum = no1 + no2

    tk.Label(root, text="Addition of number is : " + str(sum)).pack()

tk.Button(root, text="Addition", command=addition).pack(pady=10)

root.mainloop()


