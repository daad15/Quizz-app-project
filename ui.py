from tkinter import *
from quiz_brain import QuizBrain
import pygame

THEME_COLOR = "#13229D"
RIGHT_ANS_COLOR = "#27ae60"
WRONG_ANS_COLOR = "#ff6b6b"
FONT = ("Bahnschrift", 17, "bold")

pygame.mixer.init()

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain



        # Window
        self.window = Tk()
        self.window.title("Quiz Me")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.resizable(width=False, height=False)

        # Question number label
        self.question_number = self.quiz.question_number
        self.question_number_label = Label(text=f"Question: {self.question_number}/{len(self.quiz.question_list)}",
                                           fg="White", bg=THEME_COLOR, highlightthickness=0,font=('Calibri',15,"bold"))
        self.question_number_label.grid(row=0, column=0)

        # Score label
        self.score = self.quiz.score
        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR, highlightthickness=0,font=("Calibri",15,"bold"))
        self.score_label.grid(row=0, column=1)

        # Canvas

        # start
        self.canvas1 = Canvas()
        self.canvas1.config(width=340, height=510,  highlightthickness=0)
        img = PhotoImage(file="images/background.png")
        self.canvas1.create_image(0,0, anchor=NW, image=img)
        self.canvas1.place(x=-20, y=-15)
        start_button_img = PhotoImage(file="images/start.png")
        self.start_button = Button(image=start_button_img, highlightthickness=0, command=self.start_quiz)
        self.start_button.place(x=85, y=300)

        # questions
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            font=FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_img, highlightthickness=0, command=self.pressed_true)
        self.true_button.grid(row=2, column=0)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.pressed_false)
        self.false_button.grid(row=2, column=1)

        # order
        Misc.lift(self.canvas1)
        Misc.lift(self.start_button)

        self.get_next_question()
        self.window.mainloop()

    def start_quiz(self):
      self.canvas1.place_forget()
      self.start_button.place_forget()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.question_number += 1
            self.question_number_label.config(text=f"Question: {self.question_number}/{len(self.quiz.question_list)}",
                                              fg="White", bg=THEME_COLOR, highlightthickness=0)
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text, fill=THEME_COLOR)
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
        else:
            endImg = PhotoImage(file="images/end.png")
            self.canvas.create_image(0, 0, anchor=NW, image=endImg)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.window.mainloop()

    def pressed_true(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)

    def pressed_false(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        if is_right:
            self.canvas.config(bg=RIGHT_ANS_COLOR)
            self.canvas.itemconfig(self.question_text, fill="white")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            pygame.mixer.music.load("images/Ding-sound-effect.mp3")
            pygame.mixer.music.play(loops=1)
        else:
            self.canvas.config(bg=WRONG_ANS_COLOR)
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)
