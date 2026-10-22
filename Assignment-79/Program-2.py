import tkinter as tk

root = tk.Tk()

root.title("Find the Largest Number")
root.geometry("600x400")

tk.Label(root, text="Enter three numbers to find maximum", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(root, text="Enter first number").pack(pady=10)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number").pack(pady=10)
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Enter third number").pack(pady=10)
entry3 = tk.Entry(root)
entry3.pack()

def findMaxNumber():
    if entry1.get() != '' or entry2.get() != '' or entry3.get() != '':
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        num3 = int(entry3.get())
        maxNum = max(num1, num2, num3)
        tk.Label(root, text="Maximum number is : " + str(maxNum)).pack(pady=10)

tk.Button(root, text="Find Maximum", command=findMaxNumber).pack(pady=10)

root.mainloop()
