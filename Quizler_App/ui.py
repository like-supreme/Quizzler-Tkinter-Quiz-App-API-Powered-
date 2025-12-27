from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox

THEME_COLOR = "#375362"
LOW_COLOR = "#ffffff"

class QuizInterface:
    def __init__(self , quiz_brain: QuizBrain):
        # accessing another classes
        self.quiz = quiz_brain

        #Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text="Score: 0",
            fg="white", 
            bg=THEME_COLOR , 
            font=("Arial" , 12 , "bold"))
        self.score_label.grid(row=0 , column=1 , padx=20 , pady=20)
       
        #Canvas
        self.canvas = Canvas(width=300 , height=250, bg= LOW_COLOR)
        self.question_text = self.canvas.create_text(150,
            125,
            text= "Welcome to Quizzler",
            font=("Arial" , 20 , "italic"), fill=THEME_COLOR , width=250)
        self.canvas.grid(row=1 , column=0 , padx=20 , pady=20 , columnspan=2)
        
        # Load images
        self.true_btn_img = PhotoImage(file="") #YOUR PATH
        self.false_btn_img = PhotoImage(file="") # YOUR PATH 

        #Buttons
        self.true_btn = Button(image=self.true_btn_img,
            highlightthickness= 0, padx=20 , pady=20, command= self.is_True)
        self.true_btn.grid(row=2 , column=0)
        
        self.false_btn = Button(image=self.false_btn_img, 
            highlightthickness= 0, padx=20 , pady=20 , command=self.is_False) 
        self.false_btn.grid(row=2 , column=1)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)   
        else:
            messagebox.showinfo("Quiz Finished", "You reached the end!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def is_True(self):
        self.give_feedback(self.quiz.check_answer("True"))
        #is_right = self.quiz.check_answer("False")
        #self.give_feedback(is_right)
        # Same codes 
    def is_False(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self , is_right):
        if is_right == True:
            self.canvas.config(bg= "green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000 , self.get_next_question)

