import tkinter as tk

root = tk.Tk()
root.geometry("200x200")
lb1 = tk.Label(root, text="Red", bg="red", fg="white")
lb1.pack(side=tk.BOTTOM)
lb2 = tk.Label(root, text="Green", bg="green", fg="white")
lb2.pack(side=tk.BOTTOM)
lb3 = tk.Label(root, text="Purple", bg="purple", fg="white")
lb3.pack(side=tk.BOTTOM)
root.mainloop()

#
#
# def processOK():
#     print("OK button is clicked")
#
#
# def processCancel():
#     print("Cancel button is clicked")
#
#
# window = Tk()  # Create a window
# btOK = Button(window, text="OK", fg="red", command=processOK)
# btCancel = Button(window, text="Cancel", bg="yellow",
#                   command=processCancel)
# btOK.pack()  # Place the OK button in the window
# btCancel.pack()  # Place the Cancel button in the window
# window.mainloop()
