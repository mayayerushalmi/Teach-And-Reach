import pandas as pd
from tkinter import *
import consts
import Screen1

teachers_df = pd.DataFrame
root = Tk()

root.title('Teach and Reach')
root.geometry(f'{consts.WINDOW_WIDTH}x{consts.WINDOW_HEIGHT}')
root.configure(background='lightblue')
# Creating a DataFrame for teachers
# teachers_data = {
#     'Full Name': ['Miriam Cohen', 'Yossi Levi', 'Dana Friedman', 'Oren Mizrahi', 'Shachar Rabinowitz',
#                   'Ravit Avraham', 'Itai Shuster', 'Maayan Barak', 'Noa Alon', 'Daniel Golan'],
#     'Gender': ['Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male'],
#     'Subject': ['Math', 'Science', 'Literature', 'History', 'Geography', 'Art', 'Music', 'Physics', 'Chemistry',
#                 'Biology'],
#     'Age Range': ['10-15', '12-18', '10-17', '15-20', '11-16', '8-14', '12-19', '13-18', '10-15', '9-16'],
#     'Phone Number': [
#         '050-1234567', '050-2345678', '050-3456789', '050-4567890', '050-5678901',
#         '050-6789012', '050-7890123', '050-8901234', '050-9012345', '050-0123456'
#     ],
#     'Short Explanation': [
#         'Algebra, geometry, and problem-solving techniques.',
#         'Biology, chemistry, and hands-on experiments.',
#         'Poetry analysis, creative writing, and literary theory.',
#         'World history, significant events, and cultural impacts.',
#         'Physical geography, human geography, and environmental studies.',
#         'Drawing, painting, and art history.',
#         'Music theory, composition, and instrumental practice.',
#         'Classical mechanics, electricity, and thermodynamics.',
#         'Organic chemistry, reactions, and lab safety.',
#         'Ecology, evolution, and human biology.'
#     ]
# }
def addTeacher(full_name, gender, subject, age_range, phone_number, short_explanation):
    global teachers_df

    new_teacher = pd.Series({
        'Full Name': full_name,
        'Gender': gender,
        'Subject': subject,
        'Age Range': age_range,
        'Phone Number': phone_number,
        'Short Explanation': short_explanation
    })

    teachers_df = teachers_df.append(new_teacher, ignore_index=True)
    teachers_df.to_csv('teachers_data.csv', index=False)


def load_data():
    teachers_df = pd.DataFrame('teachers_data.csv')
    return teachers_df


def apply_data(teachers_df):
    teachers_df.to_csv('teachers_data.csv', index=False)


text_var = StringVar()
text_var.set("The details you entered have been added to the database!")


def create_confirmation_text():
    label = Label(root,
                     textvariable=text_var,
                     anchor=CENTER,
                     height=40,
                     width=60,
                     bd=3,
                     font=("calibri", 32, "bold"),
                     cursor="hand2",
                     fg="black",
                     padx=15,
                     pady=15,
                     justify=CENTER,
                     relief=RAISED,
                     wraplength=250
                     )

    label.pack(pady=20)
    root.mainloop()

# student_data = {
#     'Full Name': full_name,
#     'Gender': gender,
#     'Age': age,
#     'Subject': subject,
#     'Short Explanation': short_explanation
# }

create_confirmation_text()