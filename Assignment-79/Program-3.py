import tkinter as tk

root = tk.Tk()
root.geometry("500x300")

root.title("Area of Circle calulations")

tk.Label(root, text="Calculate area of circle", font=("Arial", 18, 'bold')).pack(pady=10)

tk.Label(root, text="Enter radius of circle").pack(pady=10)
entry = tk.Entry()
entry.pack()

def calculateArea():
    if entry.get() != '':
        radius = int(entry.get())
        area = 3.14 * radius * radius
        tk.Label(root, text= f"Area of circle is : {area:.2f}").pack(pady=10)

tk.Button(root, text="Calculate Area", command=calculateArea).pack(pady=10)
root.mainloop()