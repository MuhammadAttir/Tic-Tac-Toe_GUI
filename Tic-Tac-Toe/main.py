from tkinter import *
from tkinter import messagebox
import pygame

pygame.mixer.init()

#--------------------------------------------------Load Music----------------------------------------------------------
def load_music():
    # Load background music
    pygame.mixer.music.load("audio.mp3")  
    pygame.mixer.music.play(-1, 0.0) 

def play_click_sound():
    click_sound = pygame.mixer.Sound("click.mp3") 
    click_sound.play()
    
def victory():
    pygame.mixer.music.stop()  # Stop background music
    click_sound = pygame.mixer.Sound("victory.mp3") 
    click_sound.play()
    
def tie():
    pygame.mixer.music.stop()  # Stop background music
    click_sound = pygame.mixer.Sound("tie.mp3") 
    click_sound.play()


#------------------------------------------------Functions------------------------------------------------------------

#Switch Turn
def button_click(b):
    global player
    if b['text'] == '':  
        b['text'] = player
        play_click_sound()
        b["bg"] = "blue" if player == "X" else "yellow"
    
    
    if check_winner():
        victory()
        turn_label.config(text=f"Congrats! Player {player} Won.")
        disable()
        return
    
    # Check for a tie
    elif all(btn['text'] != '' for btn in [b1,b2,b3,b4,b5,b6,b7,b8,b9]):
        tie()
        turn_label.config(text="It's a Tie!")
        disable()
        return
        
    player = "O" if player == "X" else "X"
    turn_label.config(text=f"Player {player}'s Turn")
    
#Check Winner
def check_winner():
    
    #Check Rows
    if b1['text']==b2['text']==b3['text'] !="":
        return True
    elif b4['text']==b5['text']==b6['text'] !="":
        return True
    elif b4['text']==b5['text']==b6['text'] !="":
        return True
    
    #Check Columns
    elif b1['text']==b4['text']==b7['text'] !="":
        return True
    elif b2['text']==b5['text']==b8['text'] !="":
        return True
    elif b3['text']==b6['text']==b9['text'] !="":
        return True
    
    #Check Diagonals
    elif b1['text']==b5['text']==b9['text'] !="":
        return True
    elif b3['text']==b5['text']==b7['text'] !="":
        return True
    
# Disable Buttons

def disable():
    
    buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    
    for btn in buttons:
        btn.config(state='disable')
    
    
    

#------------------------------------------------Mian Window----------------------------------------------------------

def main():
    global window, player, turn_label
    global b1, b2, b3, b4, b5, b6, b7, b8, b9

    window = Tk()
    window.geometry('315x350')
    window.title("Tic-Tac-Toe")
    window.configure(bg='#1e1e1e')

    # Global Var
    player = 'X'

    # Show rules
    messagebox.showinfo(
        "Game Rules",
        "1). Take turns placing X or O in empty squares.\n"
        "2). Get 3 of your symbols in a row to win.\n"
        "3). If all 9 squares are filled with no winner, it’s a tie."
    )

    load_music()

    # Label to show player turn
    turn_label = Label(text=f"Player {player}'s Turn", font=("Segoe UI", 14, "bold"), bg='#1e1e1e', fg='white')
    turn_label.grid(row=0, column=0, columnspan=3, pady=13)

    # 1st Row
    b1 = Button(text="", width=5, height=2, font=("Arial", 24), bg='black', command=lambda: button_click(b1))
    b1.grid(row=1, column=0)

    b2 = Button(text="", width=5, height=2, font=("Arial", 24), bg='black', command=lambda: button_click(b2))
    b2.grid(row=1, column=1)

    b3 = Button(text="", width=5, height=2, font=("Arial", 24), bg='black', command=lambda: button_click(b3))
    b3.grid(row=1, column=2)

    # 2nd Row
    b4 = Button(text="", width=5, height=2, font=("Arial", 24), bg='black', command=lambda: button_click(b4))
    b4.grid(row=2, column=0)

    b5 = Button(text="", width=5, height=2, font=("Arial", 24), bg='black', command=lambda: button_click(b5))
    b5.grid(row=2, column=1)

    b6 = Button(text="", width=5, height=2, font=("Arial", 24), bg='black', command=lambda: button_click(b6))
    b6.grid(row=2, column=2)

    # 3rd Row
    b7 = Button(text="", width=5, height=2, font=("Arial", 24), bg='black', command=lambda: button_click(b7))
    b7.grid(row=3, column=0)

    b8 = Button(text="", width=5, height=2, font=("Arial", 24), bg='black', command=lambda: button_click(b8))
    b8.grid(row=3, column=1)

    b9 = Button(text="", width=5, height=2, font=("Arial", 24), bg='black', command=lambda: button_click(b9))
    b9.grid(row=3, column=2)

    window.mainloop()

if __name__ == "__main__":
    main()
