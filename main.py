import customtkinter as ctk
import random
import time
import subprocess

from tkinter import messagebox

from passages import (
    easy_passages,
    medium_passages,
    hard_passages
)

from utils import (
    calculate_wpm,
    calculate_accuracy,
    calculate_errors
)

from database import (
    create_database,
    save_result
)


# Theme

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# Variables

current_text = ""
start_time = None
timer_running = False
difficulty = "Easy"



# Change difficulty

def change_difficulty(value):

    global difficulty

    difficulty = value



# Start Test

def start_test():

    global current_text
    global start_time
    global timer_running


    if difficulty == "Easy":

        current_text = random.choice(
            easy_passages
        )


    elif difficulty == "Medium":

        current_text = random.choice(
            medium_passages
        )


    else:

        current_text = random.choice(
            hard_passages
        )


    paragraph_box.configure(
        state="normal"
    )


    paragraph_box.delete(
        "1.0",
        "end"
    )


    paragraph_box.insert(
        "end",
        current_text
    )


    paragraph_box.configure(
        state="disabled"
    )


    typing_box.delete(
        "1.0",
        "end"
    )


    start_time = time.time()

    timer_running = True

    update_timer()



# Timer

def update_timer():

    global timer_running


    if timer_running:

        elapsed = int(
            time.time() - start_time
        )


        timer_label.configure(
            text=f"⏱ Time: {elapsed} sec"
        )


        app.after(
            1000,
            update_timer
        )



# Submit Test

def submit_test():

    global timer_running


    if start_time is None:

        messagebox.showwarning(
            "Warning",
            "Start the test first!"
        )

        return



    timer_running = False


    typed_text = typing_box.get(
        "1.0",
        "end"
    ).strip()



    time_taken = time.time() - start_time



    wpm = calculate_wpm(
        typed_text,
        time_taken
    )


    accuracy = calculate_accuracy(
        current_text,
        typed_text
    )


    errors = calculate_errors(
        current_text,
        typed_text
    )



    save_result(
        wpm,
        accuracy,
        errors,
        time_taken,
        difficulty
    )


    result_label.configure(

        text=f"""
⚡ Speed: {wpm} WPM

🎯 Accuracy: {accuracy}%

❌ Errors: {errors}

⏱ Time: {round(time_taken,2)} sec

📌 Level: {difficulty}
"""
    )



# Open Dashboard

def open_dashboard():

    subprocess.Popen(
        [
            "python",
            "dashboard.py"
        ]
    )



# Create Database

create_database()



# Main Window

app = ctk.CTk()


app.title(
    "Typing Speed Tester Pro"
)


app.geometry(
    "1000x800"
)



# Title

title = ctk.CTkLabel(

    app,

    text="⌨ Typing Speed Tester Pro",

    font=("Arial",35,"bold")

)

title.pack(
    pady=25
)



# Difficulty

difficulty_label = ctk.CTkLabel(

    app,

    text="Select Difficulty",

    font=("Arial",20)

)

difficulty_label.pack(
    pady=5
)



difficulty_box = ctk.CTkComboBox(

    app,

    values=[
        "Easy",
        "Medium",
        "Hard"
    ],

    command=change_difficulty,

    width=220

)


difficulty_box.set(
    "Easy"
)


difficulty_box.pack(
    pady=10
)



# Timer

timer_label = ctk.CTkLabel(

    app,

    text="⏱ Time: 0 sec",

    font=("Arial",20)

)

timer_label.pack()



# Paragraph Box

paragraph_box = ctk.CTkTextbox(

    app,

    width=850,

    height=130,

    font=("Arial",16),

    corner_radius=15

)

paragraph_box.pack(
    pady=20
)


paragraph_box.configure(
    state="disabled"
)



# Typing Box

typing_box = ctk.CTkTextbox(

    app,

    width=850,

    height=180,

    font=("Arial",16),

    corner_radius=15

)

typing_box.pack()



# Buttons

button_frame = ctk.CTkFrame(
    app
)

button_frame.pack(
    pady=25
)



start_button = ctk.CTkButton(

    button_frame,

    text="🚀 Start Test",

    width=180,

    height=45,

    font=("Arial",16),

    command=start_test

)

start_button.grid(
    row=0,
    column=0,
    padx=15
)



submit_button = ctk.CTkButton(

    button_frame,

    text="✅ Submit",

    width=180,

    height=45,

    font=("Arial",16),

    command=submit_test

)

submit_button.grid(
    row=0,
    column=1,
    padx=15
)



dashboard_button = ctk.CTkButton(

    button_frame,

    text="📊 Open Dashboard",

    width=180,

    height=45,

    font=("Arial",16),

    command=open_dashboard

)

dashboard_button.grid(
    row=0,
    column=2,
    padx=15
)



# Result

result_label = ctk.CTkLabel(

    app,

    text="Your Result Will Appear Here",

    font=("Arial",20)

)

result_label.pack(
    pady=20
)



# Run App

app.mainloop()