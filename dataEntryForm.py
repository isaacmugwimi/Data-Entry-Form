from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter


def enterData():
    messagebox.showinfo("Output", "Do you want to Submit data?")
    firstName = fNameEntry.get()
    lastName = lNameEntry.get()
    title = titleCombobox.get()
    age = ageSpinbox.get()
    nationality = nationalityCombobox.get()
    isRegistered = regStatus.get()
    completed_Course = completedCourseSpinBox.get()
    semester = semesterSpinBox.get()
    terms_conditions = terms_conditions_status.get()

    print(
        f"First Name: {firstName}\n Last Name: {lastName}\n Title: {title}\n age: {age}\n Nationality: {nationality}\n Registration Status: {isRegistered}\n Completed Courses: {completed_Course}\n Semester: {semester}\n Agreed to Terms and Conditions: {terms_conditions}"
    )


window = Tk()
window.geometry("600x400")
window.title("Data Entry Form")

mainFrame = Frame(window)

user_info_frame = LabelFrame(mainFrame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

fNameLabel = Label(user_info_frame, text="First Name")
fNameLabel.grid(column=0, row=0)

fNameEntry = Entry(user_info_frame)
fNameEntry.grid(row=1, column=0, padx=15)


lNameLabel = Label(user_info_frame, text="Last Name")
lNameLabel.grid(column=1, row=0)

lNameEntry = Entry(user_info_frame)
lNameEntry.grid(row=1, column=1, padx=15)

titleLabel = Label(user_info_frame, text="Title")
titleLabel.grid(column=2, row=0)
titleCombobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Mrs.", "Dr."])
titleCombobox.grid(row=1, column=2, padx=15)


ageLabel = Label(user_info_frame, text="Age")
ageLabel.grid(row=2, column=0)
ageSpinbox = Spinbox(user_info_frame, from_=0, to=120)
ageSpinbox.grid(row=3, column=0)


nationalityLabel = Label(user_info_frame, text="Nationality")
nationalityLabel.grid(row=2, column=1)

nationalityCombobox = ttk.Combobox(
    user_info_frame, values=["", "Kenya", "Tanzania", "Ghana", "Spain"], width=19
)
nationalityCombobox.grid(
    row=3,
    column=1,
)


course_frame = LabelFrame(mainFrame)
course_frame.grid(row=1, column=0, padx=20, pady=20)

registrationLabel = Label(course_frame, text="Registration Status")
registrationLabel.grid(row=0, column=0)

regStatus = StringVar(value="Not registered")
registrationCheckButton = Checkbutton(
    course_frame,
    text="Currently Registered",
    variable=regStatus,
    onvalue="Registered",
    offvalue="Not registerd",
)
registrationCheckButton.grid(row=1, column=0, padx=15)

completedCourseLabel = Label(course_frame, text="#Completed Courses")
completedCourseLabel.grid(row=0, column=1)

completedCourseSpinBox = Spinbox(course_frame, from_=0, to=10)
completedCourseSpinBox.grid(row=1, column=1, padx=15)

semesterLabel = Label(course_frame, text="#Semester")
semesterLabel.grid(row=0, column=2)

semesterSpinBox = Spinbox(course_frame, from_=0, to=4)
semesterSpinBox.grid(row=1, column=2, padx=15)


terms_conditions_frame = LabelFrame(mainFrame, text="Terms & Conditons")
terms_conditions_frame.grid(row=2, column=0, padx=20, pady=20)

terms_conditions_status = StringVar(value="No")

termsCheckButton = tkinter.Checkbutton(
    terms_conditions_frame,
    text="I accept the terms and conditions.",
    variable=terms_conditions_status,
    offvalue="No",
    onvalue="Yes",
)
termsCheckButton.grid(row=0, column=0, sticky="news")

enterDataButton = Button(mainFrame, text="Enter data", command=enterData)
enterDataButton.grid(row=3, column=0, padx=20, pady=20)


mainFrame.pack()
window.mainloop()
