import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()
window.title("Calculator")

# Create a text box for displaying the input and output
input_box = tk.Entry(window, width=30)
input_box.grid(row=0, column=0, columnspan=4)

# Define a function for adding buttons to the calculator
def create_button(text, row, column, function=None):
    button = tk.Button(window, text=text, padx=10, pady=5, command=function)
    button.grid(row=row, column=column)
    return button

# Define a function for handling button clicks
def handle_click(button_text):
    current_input = input_box.get()
    if button_text == "=":
        try:
            result = eval(current_input)
            input_box.delete(0, tk.END)
            input_box.insert(0, result)
        except Exception as e:
            input_box.delete(0, tk.END)
            input_box.insert(0, "Error")
    elif button_text == "C":
        input_box.delete(0, tk.END)
    else:
        input_box.insert(tk.END, button_text)

# Add number buttons to the calculator
create_button("1", 1, 0, lambda: handle_click("1"))
create_button("2", 1, 1, lambda: handle_click("2"))
create_button("3", 1, 2, lambda: handle_click("3"))
create_button("4", 2, 0, lambda: handle_click("4"))
create_button("5", 2, 1, lambda: handle_click("5"))
create_button("6", 2, 2, lambda: handle_click("6"))
create_button("7", 3, 0, lambda: handle_click("7"))
create_button("8", 3, 1, lambda: handle_click("8"))
create_button("9", 3, 2, lambda: handle_click("9"))
create_button("0", 4, 1, lambda: handle_click("0"))

# Add operator buttons to the calculator
create_button("+", 1, 3, lambda: handle_click("+"))
create_button("-", 2, 3, lambda: handle_click("-"))
create_button("*", 3, 3, lambda: handle_click("*"))
create_button("/", 4, 3, lambda: handle_click("/"))

# Add clear and equals buttons to the calculator
create_button("C", 4, 0, lambda: handle_click("C"))
create_button("=", 4, 2, lambda: handle_click("="))

# Run the Tkinter event loop
window.mainloop()
