from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Ui:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.word = self.canvas.create_text(150, 125, text="sample", font=("Ariel", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        self.label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", highlightthickness=0)
        self.label.grid(column=1, row=0)

        self.button1 = Button(image=false_img, command=self.wrong)
        self.button1.grid(column=1, row=2)
        self.button1.config(pady=50)

        self.button2 = Button(image=true_img, command=self.right)
        self.button2.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question_left = self.quiz.still_has_questions()
        if question_left:
            question_text = self.quiz.next_question()
            self.canvas.configure(bg="white")
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.word, text=question_text)
        else:
            self.canvas.configure(bg="yellow")
            self.canvas.itemconfig(self.word, text="Game Over")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")

    def right(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong(self):
        is_wrong = self.quiz.check_answer("False")
        self.give_feedback(is_wrong)

    def give_feedback(self, answer):
        if answer:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
