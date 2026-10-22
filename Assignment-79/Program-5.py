import tkinter as tk

root = tk.Tk()

root.title("Authentication cheking system")
root.geometry("400x300")

tk.Label(root, text="Enter login details").pack(pady=10)

tk.Label(root, text="Enter username").pack(pady=10)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter password").pack(pady=10)
entry2 = tk.Entry(root, show="*")
entry2.pack()

nameErr = tk.Label(root, text="UserName is not entered", font=("Arial", 12, "bold"), fg="red")
pwdErr = tk.Label(root, text="Password is not entered", font=("Arial", 12, "bold"), fg="red")

credentials = {
    "manojsonawane": "M@123$",
    "gaganShinde": "G@123$"
}

def loginToApp():
    nameErr.pack_forget()
    pwdErr.pack_forget()

    if entry1.get() == "":
        nameErr.pack(pady=10)
        return
    if entry2.get() == "":
        pwdErr.pack(pady=10)
        return
    
    username = entry1.get()
    pwd = entry2.get()

    if len(credentials) > 0:
        if credentials.get(username) == pwd:
            tk.Label(root, text="Credentials are matched, you can login", fg="green").pack(pady=10)
        else:
            tk.Label(root, text="Credentials are not matched, you can not login", fg="red").pack(pady=10)
    

tk.Button(root, text="Login", command=loginToApp).pack(pady=10)
root.mainloop()
