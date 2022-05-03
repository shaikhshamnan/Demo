from pydoc import text
import tkinter
import random

timeleft= 30

def game(event):

    comp_win = 0
    player_win = 0
    n = 0
    if (roundentry.get().isnumeric and (int (roundentry.get())) > 0):
        n = int (roundentry.get())
        roundentry.grid_forget()
        roundInputlabel.grid_forget()
        instructions.grid(row=2, column=1, sticky="E")
        instructions2.grid(row=3, column=1, ipadx="50px")
        inputGame = tkinter.Entry(root, textvariable=var_choice)
        inputGame.grid(row=4, column=1, ipadx="70px")
       # inputGame.
        inputGame.focus_set()
        instructions3.grid(row=10, column=1)
        instructions4.grid(row=11, column=1)
    else:
        return

    round = 1
    #print("Rules:-\nSnake vs. Water: Snake drinks the water hence wins.\nWater vs. Gun: The gun will drown in water, hence a point for water.\nGun vs. Snake: Gun will kill the snake and win.\nIn situations where both players choose the same object, the result will be a draw.")
    #print("Select your choice..........\n1.)Snake(s).....\n2.)Water(w)......\n3.)Gun(g)......")
    while round <= n:
        instructions3.config( text = "Let's Begin Round - {}".format(round))
        rand_no = random.randint(1, 3)

        if rand_no == 1:
            comp = "s"
        elif rand_no == 2:
            comp = "w"
        else:
            comp = "g"
        inputGame.bind('<Up>', lambda event, comp=comp, player=inputGame.get(), round=round: 
        checkCompAndPlayer(event, comp, player, round))
        #inputGame.bind("<Return>", lambda:checkCompAndPlayer(comp, inputGame.get(), round))
        

    if player_win > comp_win:
        instructions3.config(text= "😄 You Win the Game with {} score 😄".format(player_win))
    elif player_win == comp_win:
        instructions3.config(text="😅 Game is Tie Play Again 😅")
    else:
        instructions3.config(text="😭 Sorry You lose the game 😭\n computer win the game with {} score".format(comp_win))

def countdown():
    global timeleft
    # if a game is in play
    if timeleft > 0:
        # decrement the timer.
        timeleft -= 1

def checkCompAndPlayer(event, comp , player, round):
    if player != 's' and player != 'w' and player != 'g':
            instructions3.config( text = "Invalid input, try again")
            return
    if comp == player:
        instructions3.config( text = "Tie")
    elif (comp == "s" and player == "w") or ( comp == "w" and player == "g") or (comp=="g" and player=="s"):
            instructions3.config( text = "Comp wins!")
            comp_win = comp_win+1
    elif (comp == "s" and player == "g") or (comp == "g" and player == "w") or (comp =="w" and player=="s"):
            instructions3.config( text = "Player wins!")
            player_win += 1
    instructions4.config(text="PLAYER SCORE {} \n COMPUTER SCORE {} \n".format(
        player_win, comp_win))
    round = round+1 

if __name__ == "__main__" :

    var_choice = tkinter.StringVar()
   
    # create a GUI window
    root = tkinter.Tk()
    
    # set the title
    root.title("Snake-Water-Gun")
    
    # set the size
    root.geometry("600x350")
    # add a text entry box for
    # typing input
    roundInputlabel = tkinter.Label(root, text = "Enter the No of Rounds you want to Play!: ",
                   fg = 'black', bg = 'grey')
    roundInputlabel.grid(row=1 , column=1, sticky="E")
    roundentry = tkinter.Entry(root)
         #   print("Rules:-\nSnake vs. Water: Snake drinks the water hence wins.\nWater vs. Gun: The gun will drown in water, hence a point for water.\nGun vs. Snake: Gun will kill the snake and win.\nIn situations where both players choose the same object, the result will be a draw.")

    instructions = tkinter.Label(root, text = "Rules:-\nSnake vs. Water: Snake drinks the water hence wins.\nWater vs. Gun: The gun will drown in water, hence a point for water.\nGun vs. Snake: Gun will kill the snake and win.\nIn situations where both players choose the same object, the result will be a draw.",
                                      font = ('Helvetica', 12))
    
    instructions.grid_forget()

    instructions2 = tkinter.Label(root, text = "Select your choice\n1.)Snake(s)\n2.)Water(w)\n3.)Gun(g)",
                                      font = ('Helvetica', 12))

    instructions2.grid_forget()
    instructions3 = tkinter.Label(root, text = "Let's Begin with {} Round .....",
                                    font = ('Helvetica', 12))
    instructions4 = tkinter.Label(root, text = "",
                                    font = ('Helvetica', 12))
    #roundentry.pack()
   # e = tkinter.Entry(root)
    # run the 'startGame' function 
    # when the enter key is pressed
    roundentry.grid(row = 1, column = 2, ipadx="50px") 
    roundentry.bind("<Return>", game)
    #e.pack()
    #roundentry.pack()
    roundentry.focus_set()
    # set focus on the entry box
    #e.focus_set()
    
    # start the GUI
    root.mainloop()
#game()
