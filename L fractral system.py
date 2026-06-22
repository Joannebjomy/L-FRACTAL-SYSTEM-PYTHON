import tkinter as tk
from tkinter import messagebox
import turtle


def expand(axiom, rules, iterations):
    current = axiom
    for i in range(iterations):
        new_string = ""
        for char in current:
            if char in rules:
                new_string += rules[char]
            else:
                new_string += char
        current = new_string
    return current


def draw(commands, length, angle, t, gradient_choice):
    total_f = commands.count("F")
    if total_f == 0:
        return
    
    step = 255 / total_f
    current_f = 0
    stack = []    
    
    for char in commands:
        if char == "F":
            progress = current_f / total_f
            if gradient_choice == "Blue to Red":
                red = int(progress * 255)
                blue = int((1 - progress) * 255)
                green = 0
            elif gradient_choice == "Rainbow":
                import math
                red = int(127.5 * (1 + math.sin(progress * 2 * math.pi)))
                green = int(127.5 * (1 + math.sin(progress * 2 * math.pi + 2 * math.pi / 3)))
                blue = int(127.5 * (1 + math.sin(progress * 2 * math.pi + 4 * math.pi / 3)))
            elif gradient_choice == "Green to Yellow":
                red = int(progress * 255)
                green = 255
                blue = 0
            elif gradient_choice == "Black to White":
                value = int(progress * 255)
                red = green = blue = value
            elif gradient_choice == "Purple to Pink":
                red = int(128 + progress * 127)
                green = int(progress * 192)
                blue = int(128 + progress * 75)
            else:
                red = int(progress * 255)
                blue = int((1 - progress) * 255)
                green = 0
            
            t.pencolor(red, green, blue)
            t.forward(length)
            current_f += 1
        elif char == "+":
            t.right(angle)
        elif char == "-":
            t.left(angle)
        elif char == "[":
            stack.append((t.position(), t.heading()))
        elif char == "]":
            pos, heading = stack.pop()
            t.penup()
            t.setposition(pos)
            t.setheading(heading)
            t.pendown()


def generate():
    try:
        axiom = axiom_entry.get().strip()
        rules_text = rules_entry.get().strip()
        angle = float(angle_entry.get())
        iterations = int(iter_entry.get())
        gradient_choice = gradient_var.get()

        if not axiom:
            messagebox.showerror("Input Error", "Axiom cannot be empty.")
            return

        rules = {}
        if rules_text:
            for rule in rules_text.split(","):
                rule = rule.strip()
                if not rule:
                    continue
                symbol, replacement = rule.split(":")
                rules[symbol.strip()] = replacement.strip()

        t.clear()
        t.penup()
        t.home()
        t.left(90)           
        t.penup()            
        t.setposition(0, -200)  
        t.pendown() 

        final_string = expand(axiom, rules, iterations)
        draw(final_string, 5, angle, t, gradient_choice)

        screen.update()

    except ValueError as e:
        messagebox.showerror("Input Error", f"Check your inputs: {e}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("L-System Fractal Architect")
root.geometry("900x600")

canvas = tk.Canvas(root, width=600, height=550, bg="white")
canvas.pack(side="left")

controls = tk.Frame(root, width=280, height=550, bg="lightgrey")
controls.pack(side="right", fill="both", padx=10, pady=10)

tk.Label(controls, text="Axiom:", bg="lightgrey").pack(anchor="w", pady=5)
axiom_entry = tk.Entry(controls, width=25)
axiom_entry.pack(anchor="w")
axiom_entry.insert(0, "F")

tk.Label(controls, text="Rules (e.g. F:F+F-F):", bg="lightgrey").pack(anchor="w", pady=5)
rules_entry = tk.Entry(controls, width=25)
rules_entry.pack(anchor="w")
rules_entry.insert(0, "F:F+F--F+F")

tk.Label(controls, text="Angle:", bg="lightgrey").pack(anchor="w", pady=5)
angle_entry = tk.Entry(controls, width=25)
angle_entry.pack(anchor="w")
angle_entry.insert(0, "60")

tk.Label(controls, text="Iterations:", bg="lightgrey").pack(anchor="w", pady=5)
iter_entry = tk.Entry(controls, width=25)
iter_entry.pack(anchor="w")
iter_entry.insert(0, "4")

tk.Label(controls, text="Color Gradient:", bg="lightgrey").pack(anchor="w", pady=5)

gradient_var = tk.StringVar()
gradient_var.set("Blue to Red")  


gradient_options = [
    "Blue to Red",
    "Rainbow",
    "Green to Yellow",
    "Black to White",
    "Purple to Pink"
]

gradient_dropdown = tk.OptionMenu(controls, gradient_var, *gradient_options)
gradient_dropdown.config(width=20)
gradient_dropdown.pack(anchor="w", pady=5)

tk.Button(controls, text="Generate", command=generate).pack(pady=20)

t = turtle.RawTurtle(canvas)
t.speed(0)
screen = t.getscreen()
screen.tracer(0)
screen.colormode(255)

root.mainloop()

