import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random,time

class MainWin(tk.Tk):

    def __init__(self):
        super().__init__()
        self.o_score_count=tk.IntVar()
        self.x_score_count=tk.IntVar()
        self.o_score_count.set(0)
        self.x_score_count.set(0)
        self.board_list = []
        self.define_window() # from here change main window properties
        self.create_game_table() # initialize the frame where game is displayed
        self.create_info_panel()


    def define_window(self):
        self.title("X & O game")
        self.geometry("408x306+300+300")
        self.resizable(width=False, height=False)


    def create_game_table(self):
        """creates game table and also from here  the game is re-started"""
        self.turn = random.choice(["o", "x"])  # define who starts the game first
        frame=tk.Frame(self,borderwidth=0, bg="#C5C8C9", width=405, height=305)
        self.bg_icon=tk.PhotoImage(file="images\\bg.gif")
        self.x_icon = tk.PhotoImage(file="images\\x_icon.gif") # icon for x choices
        self.o_icon = tk.PhotoImage(file="images\\o_icon.gif") # icon for o choices
        self.blank_icon= tk.PhotoImage(file="images\\blank_icon.gif") # icon for blank boxes

        self.canvas_frame = tk.Canvas(frame,width=305, height=305,bd=0, highlightthickness=0, )
        self.canvas_frame.create_image(0, 0, image=self.bg_icon, anchor="nw")


        self.label_1= tk.Label(frame, text="blank", image= self.blank_icon, bd=0,)
        self.label_2= tk.Label(frame, text="blank", image= self.blank_icon, bd=0)
        self.label_3= tk.Label(frame, text="blank", image= self.blank_icon, bd=0)
        self.label_4= tk.Label(frame, text="blank", image= self.blank_icon, bd=0)
        self.label_5= tk.Label(frame, text="blank", image= self.blank_icon, bd=0)
        self.label_6= tk.Label(frame, text="blank", image= self.blank_icon, bd=0)
        self.label_7= tk.Label(frame, text="blank", image= self.blank_icon, bd=0)
        self.label_8= tk.Label(frame, text="blank", image= self.blank_icon, bd=0)
        self.label_9= tk.Label(frame, text="blank", image= self.blank_icon, bd=0)


        self.canvas_frame.create_window(5,5,window=self.label_1,anchor="nw")
        self.canvas_frame.create_window(107,5,window=self.label_2,anchor="nw")
        self.canvas_frame.create_window(210,5,window=self.label_3,anchor="nw")
        self.canvas_frame.create_window(5,108,window=self.label_4,anchor="nw")
        self.canvas_frame.create_window(107,108,window=self.label_5,anchor="nw")
        self.canvas_frame.create_window(210,108,window=self.label_6,anchor="nw")
        self.canvas_frame.create_window(5,210,window=self.label_7,anchor="nw")
        self.canvas_frame.create_window(107,210,window=self.label_8,anchor="nw")
        self.canvas_frame.create_window(210,210,window=self.label_9,anchor="nw")

        self.label_1.bind("<Button-1>", self.move_action)
        self.label_2.bind("<Button-1>", self.move_action)
        self.label_3.bind("<Button-1>", self.move_action)
        self.label_4.bind("<Button-1>", self.move_action)
        self.label_5.bind("<Button-1>", self.move_action)
        self.label_6.bind("<Button-1>", self.move_action)
        self.label_7.bind("<Button-1>", self.move_action)
        self.label_8.bind("<Button-1>", self.move_action)
        self.label_9.bind("<Button-1>", self.move_action)


        self.canvas_frame.pack()
        frame.place(x=0, y=0)

    def create_info_panel(self):
        """frame with score and game buttons"""
        self.info_to_display = tk.StringVar()
        self.info_to_display.set(self.turn.upper() + "  to move..  ")
        frame=tk.Frame(self,borderwidth=2, bg="#C5C8C9", width=100, height=340, relief=None)
        self.label_frame_score=tk.LabelFrame(frame, text="Score", labelanchor="n", bg="#C5C8C9")
        self.label_o_score= tk.Label(self.label_frame_score,text="O wins  :", bg="#C5C8C9")
        self.label_x_score= tk.Label(self.label_frame_score,text="X wins  :", bg="#C5C8C9")
        self.label_o_count = tk.Label(self.label_frame_score, textvariable =   self.o_score_count, bg="#C5C8C9")
        self.label_x_count = tk.Label(self.label_frame_score, textvariable =   self.x_score_count, bg="#C5C8C9")
        self.label_frame_turn = tk.LabelFrame(frame, text="Turn", labelanchor="n", bg="#C5C8C9",width=10)
        self.label_turn=tk.Label(self.label_frame_turn, textvariable= self.info_to_display,bg="#C5C8C9")
        self.label_frame_time_played=tk.LabelFrame(frame, text="Time played",bg="#C5C8C9")
        self.label_time_played = tk.Label(self.label_frame_time_played, text="10:00", bg="#C5C8C9")
        self.resset_button=ttk.Button(frame,  text="Start again", takefocus=False, command=self.reset_game_table)
        self.quit_button=ttk.Button(frame,  text="Quit", takefocus=False, command=self.quit_game)


        self.label_time_played.pack()
        self.label_turn.pack()
        self.label_o_score.grid(column=0, row=0)
        self.label_o_count.grid(column=1, row=0)
        self.label_x_score.grid(column=0, row=1)
        self.label_x_count.grid(column=1, row=1)
        self.label_frame_time_played.place(x=10, y=145)
        self.label_frame_score.place(x=10,y=10)
        self.label_frame_turn.place(x=10,y=85)
        self.resset_button.place(x=10, y=240)
        self.quit_button.place(x=10, y=270)
        frame.place(x=306, y=0)




    def move_action(self,event):
        """from here player can select a box"""
        if self.turn=="o":
            if event.widget.cget("text")=="blank":
                event.widget.configure(text="o", image=self.o_icon)
                self.board_list.clear()
                for i in [self.label_1, self.label_2, self.label_3,
                          self.label_4, self.label_5, self.label_6,
                          self.label_7, self.label_8, self.label_9]:
                    self.board_list.append(i["text"])
                self.check_for_winner(self.board_list)
                self.turn="x"
                self.info_to_display.set(self.turn.upper()+ " to move")
        else:
            if event.widget.cget("text") == "blank":
                event.widget.configure(text="x", image=self.x_icon)
                self.board_list.clear()
                for i in [self.label_1, self.label_2, self.label_3,
                          self.label_4, self.label_5, self.label_6,
                          self.label_7, self.label_8, self.label_9]:
                    self.board_list.append(i["text"])
                self.check_for_winner(self.board_list)
                self.turn = "o"
                self.info_to_display.set(self.turn.upper()+ " to move")

    def reset_game_table(self):
        """starting a new game"""
        self.create_game_table()

    def show_tie_message(self):
        """functia care afiseaza cand meciul s-a terminat la egalitate"""
        show_tie_message=messagebox.askquestion(title="No winner!", message="No one won this game,\nDo you want to try again ?")
        if show_tie_message=="yes":
            self.create_game_table()
        else:
            self.quit_game()

    def show_winner_message(self,player_name):
        """functia care afiseaza castigotorul pe ecran si actualizeaza scorul"""
        if player_name=="o":
            self.o_score_count.set(self.o_score_count.get()+1)
        else:
            self.x_score_count.set(self.x_score_count.get() + 1)
        show_winner_message = messagebox.askquestion(title="We have a winner!", message="It seems that {} won this game.\nPlay again?".format(player_name))
        if show_winner_message=="yes":
            self.create_game_table()
            
        else:
            self.quit_game()

    def quit_game(self):
        """destroy main window if ansswer is Yes"""
        self.quit_meesage=messagebox.askquestion(title="Quit message", icon="question", message="Do you really want to quit?")
        if self.quit_meesage =="yes":
            self.destroy()

    def check_for_winner(self,list):
        """ functia care verifica castigatorul, primeste pentru verificare lista actualizata dupa fiecare mutare"""
        winner=False
        for i in range(0, 8, 3):  # verificare pe linii
            if list[i]==list[i+1] and list[i]==list[i+2]:
                if list[i]!="blank":
                    winner=True
                    self.show_winner_message(list[i])

        for i in range(0, 3, 1):  # verificare pe coloane
            if list[i] == list[i + 3] and list[i + 6] == list[i]:
                if list[i] != "blank":
                    winner = True
                    self.show_winner_message(list[i])
        if (list[0] == list[4]) and (list[0] == list[8]):  # verificare pe diagonala
            if list[0] != "blank":
                winner = True
                self.show_winner_message(list[0])
        if (list[2] == list[4]) and (list[2] == list[6]):  # verificare pe diagonala
            if list[2] != "blank":
                winner = True
                self.show_winner_message(list[2])
        if not winner:
            self.tie = True # verificare egalitate
            for i in range(len(list)):
                if list[i] =="blank":
                    self.tie= False
            if self.tie==True:
                self.show_tie_message()

if __name__=="__main__":

    app=MainWin()
    app.mainloop()


