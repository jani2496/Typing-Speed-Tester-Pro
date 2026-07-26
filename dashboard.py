import customtkinter as ctk
import matplotlib.pyplot as plt

from database import get_results

# Theme

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")



# Get data

results = get_results()
def show_difficulty_chart():

    levels = {
        "Easy": [],
        "Medium": [],
        "Hard": []
    }


    for row in results:

        difficulty = row[6]
        wpm = row[2]


        if difficulty in levels:

            levels[difficulty].append(wpm)



    difficulty_names = []
    average_wpm = []


    for level, speeds in levels.items():

        difficulty_names.append(level)


        if len(speeds) > 0:

            average = sum(speeds) / len(speeds)

        else:

            average = 0


        average_wpm.append(
            round(average,2)
        )



    plt.figure(
        figsize=(7,4)
    )


    plt.bar(
        difficulty_names,
        average_wpm
    )


    plt.xlabel(
        "Difficulty Level"
    )


    plt.ylabel(
        "Average WPM"
    )


    plt.title(
        "Typing Speed Comparison by Difficulty"
    )


    plt.show()


# Main window

app = ctk.CTk()

app.title(
    "Typing Speed Dashboard"
)

app.geometry(
    "1000x750"
)



# Title

title = ctk.CTkLabel(

    app,

    text="📊 Typing Speed Dashboard",

    font=("Arial",35,"bold")

)

title.pack(
    pady=20
)



# Statistics calculation

total_tests = len(results)


if total_tests > 0:

    speeds = [
        row[2]
        for row in results
    ]

    accuracies = [
        row[3]
        for row in results
    ]


    best_speed = max(
        speeds
    )


    avg_speed = round(
        sum(speeds)/total_tests,
        2
    )


    avg_accuracy = round(
        sum(accuracies)/total_tests,
        2
    )


else:

    best_speed = 0
    avg_speed = 0
    avg_accuracy = 0



# Overall Card

stats = ctk.CTkLabel(

    app,

    text=f"""

📝 Total Tests

{total_tests}


🏆 Best Speed

{best_speed} WPM


⚡ Average Speed

{avg_speed} WPM


🎯 Accuracy

{avg_accuracy}%


""",

    font=("Arial",20)

)


stats.pack(
    pady=15
)



# Difficulty Calculation

levels = {

    "Easy": [],

    "Medium": [],

    "Hard": []

}



for row in results:

    difficulty = row[6]

    wpm = row[2]


    if difficulty in levels:

        levels[difficulty].append(
            wpm
        )




difficulty_text = "📈 Difficulty Performance\n\n"



for level, speeds in levels.items():


    if len(speeds) > 0:

        best = max(speeds)

        avg = round(
            sum(speeds)/len(speeds),
            2
        )

    else:

        best = 0
        avg = 0



    if level == "Easy":

        emoji = "🟢"

    elif level == "Medium":

        emoji = "🟡"

    else:

        emoji = "🔴"



    difficulty_text += f"""

{emoji} {level}


🏆 Best:
{best} WPM


⚡ Average:
{avg} WPM


"""



difficulty_label = ctk.CTkLabel(

    app,

    text=difficulty_text,

    font=("Arial",18)

)


difficulty_label.pack(
    pady=10
)
chart_button = ctk.CTkButton(

    app,

    text="📊 Show Difficulty Chart",

    width=250,

    height=45,

    font=("Arial",16),

    command=show_difficulty_chart

)


chart_button.pack(
    pady=15
)


# History Table

history_title = ctk.CTkLabel(

    app,

    text="📋 Test History",

    font=("Arial",25,"bold")

)

history_title.pack(
    pady=10
)



history_box = ctk.CTkTextbox(

    app,

    width=900,

    height=180,

    font=("Arial",15)

)

history_box.pack()



for row in results:


    history_box.insert(

        "end",

        f"""

Date: {row[1]}

Speed: {row[2]} WPM

Accuracy: {row[3]}%

Errors: {row[4]}

Time: {round(row[5],2)} sec

Level: {row[6]}


----------------------------

"""

    )


history_box.configure(
    state="disabled"
)



app.mainloop()