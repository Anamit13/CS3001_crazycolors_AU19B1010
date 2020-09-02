#from tkinter imported * which saves the typing by allowing to access the objects directly.
from tkinter import * 

#imported random to shuffle and generate random colors on the screen
import random 

#generated the main_window as object as a starting window 
#object defination seems to be correct but need to get 
main_window = Tk()  

#giving the size to the main_window 
main_window.geometry("600x550")  

#giving the title to the window of the game
main_window.title("CRAZY COLORS_")

#assigning the window black background
main_window.configure(bg = "black")

#giving the image as background
Photo = PhotoImage(file="colorc.png")
Photo_label = Label(image= Photo)
Photo_label.pack()
 
#giving the first heading to the game 
#giving the font name, size and color
#placing the heading on the window.
head = Label(main_window, text = "Crazy Colors!", font = ("Cambria", 40), fg = 'white', bg = 'black').place(x = 140, y = 55)

#giving the second heading of the developer's name
#assigning the font name, size and color
#placing the heading
head1 = Label(main_window, text = "@Anamit - Games", font = ("Cambria", 20), fg = 'cyan', bg = 'black').place(x = 190, y = 185)                         

#list of the color that will display with the color text
color_display = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown'] 

#initialised user users_score
users_score = 0
  
# the user time left, initially 30 seconds. 
users_time = 30


  
def play():  
    
    # This function will start the game
    def startGame(event): 
          
        if users_time == 30: 
              
            #This will start the timer
            time_count() 
              
        #this functions will display the next color 
        show_color() 
      
    
    #Function will display the next colour. 
    def show_color(): 
      
        # use the globally declared 'users_score' 
        #used globally declared timer
        
        global users_score 
        global users_time 
      
        # if the game is in process
        if users_time > 0: 
      
            # will make the text field initiated
            e1.focus_set() 
      
            # if the colour typed is equal 
            # to the colour of the text 
            for i in range(10):
                if e1.get().lower() == color_display[i].lower(): 
                      
                    users_score += 1
      
            # clear the text entry box. 
            e1.delete(0, END) 
              
            random.shuffle(color_display) 
              
            # change the colour to type, by changing the 
            # text _and_ the colour to a random colour value 
            label.config(fg = str(color_display[1]), text = str(color_display[0])) 
              
            # update the users_score. 
            users_scoreLabel.config(text = "users_score: " + str(users_score)) 
      
      
    # time_count timer function  
    def time_count(): 
      
        global users_time 
      
        # if a game is in play 
        if users_time > 0: 
      
            # decrement the timer. 
            users_time -= 1
              
            # update the time left label 
            timeLabel.config(text = "users_time: "
                                   + str(users_time)) 
                                     
            # run the function again after 1 second. 
            timeLabel.after(1000, time_count) 
      
      
    # Driver Code 
      
    # create a GUI window 
    play_window = Tk() 
      
    # set the title 
    play_window.title("Crazy Colors") 
      
    # set the size 
    play_window.geometry("400x350") 
    
    play_window.configure(bg = "black")
      
    # add an instructions label 
    instructions = Label(play_window, text = "Type in the color"
                            " of the words, and not the word text!", 
                                          font = ('Cambria', 12), bg = "black", fg = "white")
    instructions.pack()  
      
    # add a users_score label 
    users_scoreLabel = Label(play_window, text = "Press enter to start", 
                                          font = ('Cambria', 12), bg = "black", fg = "white") 
    users_scoreLabel.pack()
      
    # add a time left label 
    timeLabel = Label(play_window, text = "users_time: " +
                  str(users_time), font = ('Cambria', 12), bg = "black", fg = "white") 
                    
    timeLabel.pack() 
      
    # add a label for displaying the color_display 
    label = Label(play_window, font = ('Cambria', 30), bg = "black") 
    label.pack() 
      
    # add a text entry box for 
    # typing in color_display 
    e1 = Entry(play_window) 
      
    # run the 'startGame' function  
    # when the enter key is pressed 
    play_window.bind('<Return>', startGame) 
    e1.pack() 
      
    # set focus on the entry box 
    e1.focus_set() 
      
    # start the GUI
    if __name__ == "__main__":
        play_window.mainloop()
    
    
  
def inst():  
    

    messagebox.showinfo("Instructions", """1. Firstly, you have to choose easy or hard level you want to play.
                        
2. Then, you have to see the text which come on the screen randomly and identify that text color. Actually the text will also be a color only.

3. Put your answer in the text box within the running time.

4. If the answer will be right than another random color will come on the screen.

5. If the answer is wrong then you will get one more chance for the same and if again it goes wrong the game will automatically get over.

6. The users_score will get updated as you go ahead in the game by +1.

7. You can also quit the game at the same time.
""")
  

   
start = Button(main_window, text = "START GAME!",command = play, font = ('Calibiri light', 20), fg = 'white', bg = 'grey').place(bordermode = 'outside',height = 60, width = 220, x = 55, y = 400)

info = Button(main_window, text = " INSTRUCTIONS ", command = inst, font = ('Calibiri light', 20), fg = 'white', bg = 'grey').place(bordermode = 'outside',height = 60, width = 220, x = 320, y = 400)

# add a label for displaying the color_display 


if __name__ == "__main__":
    main_window.mainloop() 

