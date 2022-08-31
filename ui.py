from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"





class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


    def create_canvas(self):
        self.canvas = Canvas(height=250, width=300, bg="#ffffff", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Hello",
                                                     fill=THEME_COLOR, font=("Arial", 15, "italic"))
        self.canvas.grid(row=2, column=0, columnspan=2, pady=40)

    def buttons_and_label(self):
        # right button
        self.right_button = Button()
        right_image = PhotoImage(file=".\images\wright.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.right_pressed)
        self.right_button.grid(row=3, column=0)

        # wrong button
        wrong_image = PhotoImage(file=".\images\wrong.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.wrong_pressed)
        self.wrong_button.grid(row=3, column=1)

        # the label
        self.score_label = Label(text="Score: 0", fg="#ffffff", bg=THEME_COLOR, font=("Arial", 10, "bold"))
        self.score_label.grid(row=1, column=1)

        self.get_next_question()



        self.window.mainloop()

    def right_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the game")

            # to make sure after the game, the buttons do not change the bg color to red or green again
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


