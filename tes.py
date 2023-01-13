# import tkinter as tk

# def on_select(var):
#     selection = var.get()
#     if selection == "car":
#         print("User selected car")
#     elif selection == "bus":
#         print("User selected bus")

# root = tk.Tk()

# var = tk.StringVar(value="car")
# car_button = tk.Radiobutton(root, text="Car", variable=var, value="car", command=lambda: on_select(var))
# car_button.pack()
# bus_button = tk.Radiobutton(root, text="Bus", variable=var, value="bus", command=lambda: on_select(var))
# bus_button.pack()

# root.mainloop()

import tkinter as tk

def on_car():
    user_input = input_field.get()
    print("User selected car and entered: " + user_input)

def on_bus():
    user_input = input_field.get()
    print("User selected bus and entered: " + user_input)

root = tk.Tk()

input_field = tk.Entry(root)
input_field.pack()
car_button = tk.Button(root, text="Car", command=on_car)
car_button.pack()
bus_button = tk.Button(root, text="Bus", command=on_bus)
bus_button.pack()

root.mainloop()
