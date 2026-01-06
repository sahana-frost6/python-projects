# bmr_full_app.py

import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_bmr():
    try:
        gender = gender_var.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        activity_level = activity_var.get()

        if gender == "Male":
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

        activity_factors = {
            "Sedentary": 1.2,
            "Lightly active": 1.375,
            "Moderately active": 1.55,
            "Very active": 1.725,
            "Extra active": 1.9
        }

        maintenance_calories = bmr * activity_factors[activity_level]
        calories_to_lose = maintenance_calories - 500
        calories_to_gain = maintenance_calories + 500

        height_m = height / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            bmi_category = "Underweight"
        elif bmi < 24.9:
            bmi_category = "Normal weight"
        elif bmi < 29.9:
            bmi_category = "Overweight"
        else:
            bmi_category = "Obesity"

        result = (
            f"BMR: {int(bmr)} kcal/day\n"
            f"Maintenance Calories: {int(maintenance_calories)} kcal/day\n"
            f"To Lose Weight: {int(calories_to_lose)} kcal/day\n"
            f"To Gain Weight: {int(calories_to_gain)} kcal/day\n"
            f"BMI: {bmi:.1f} ({bmi_category})"
        )

        result_text.set(result)
        draw_pie_chart(maintenance_calories, calories_to_lose, calories_to_gain)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def draw_pie_chart(maintain, lose, gain):
    figure.clear()
    ax = figure.add_subplot(111)
    labels = ['Maintain', 'Lose', 'Gain']
    values = [maintain, lose, gain]
    colors = ['#66b3ff', '#ff9999', '#99ff99']
    ax.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    ax.set_title('Calories Distribution')
    canvas.draw()

# GUI Setup
root = tk.Tk()
root.title("BMR Calculator with Pie Chart")
root.geometry("650x650")

ttk.Label(root, text="Gender:").pack()
gender_var = tk.StringVar(value="Male")
ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female"], state="readonly").pack()

ttk.Label(root, text="Age (years):").pack()
age_entry = ttk.Entry(root)
age_entry.pack()

ttk.Label(root, text="Height (cm):").pack()
height_entry = ttk.Entry(root)
height_entry.pack()

ttk.Label(root, text="Weight (kg):").pack()
weight_entry = ttk.Entry(root)
weight_entry.pack()

ttk.Label(root, text="Activity Level:").pack()
activity_var = tk.StringVar(value="Sedentary")
ttk.Combobox(root, textvariable=activity_var, values=[
    "Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active"
], state="readonly").pack()

ttk.Button(root, text="Calculate BMR", command=calculate_bmr).pack(pady=10)

result_text = tk.StringVar()
ttk.Label(root, textvariable=result_text, justify="center", font=("Arial", 10)).pack()

figure = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.get_tk_widget().pack()

root.mainloop()