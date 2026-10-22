import tkinter as tk

root = tk.Tk()

root.title("Voting eligibility Checker System")
root.geometry("400x300")

tk.Label(root, text="Check voting eligibility", font=("Arial", 18, "bold")).pack()

tk.Label(root, text="Enter your full name").pack(pady=10)
entryName = tk.Entry()
entryName.pack()

tk.Label(root, text="Enter your age").pack(pady=10)
ageEntry = tk.Entry()
ageEntry.pack()

nameErr = tk.Label(root, text="Name is not entered", font=("Arial", 12, "bold"), fg="red")
ageErr = tk.Label(root, text="Age is not entered", font=("Arial", 12, "bold"), fg="red")

def checkEligibility():    
    nameErr.pack_forget()
    ageErr.pack_forget()

    if entryName.get() == "":    
        nameErr.pack(pady=10)
        return
    if ageEntry.get() == "":
        ageErr.pack(pady=10)
        return

    name = entryName.get()
    age = int(ageEntry.get())

    if age >= 18:
        tk.Label(root, text=f"Person {name} is eligible for voting", fg="green").pack(pady=10)
    else:
        tk.Label(root, text=f"Person {name} is not eligible for voting", fg="red").pack(pady=10)

tk.Button(root, text="Check Eligibility", command=checkEligibility).pack(pady=10)
root.mainloop()