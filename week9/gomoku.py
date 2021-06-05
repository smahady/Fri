from tkinter import * 
import random

BOARD_WIDTH = 532
BOARD_HEIGHT = 536
BOARD_SIZE = 15


# Define the offsets disatance between the pixel of the coordinate of the board and the array.

X_OFFSET = 21
Y_OFFSET = 23

# Define the ratio betwwent the pixel of the coordinate of the board and the board array.
X_RATE = (BOARD_WIDTH - X_OFFSET * 2) / (BOARD_SIZE - 1)
Y_RATE = (BOARD_HEIGHT - Y_OFFSET * 2) / (BOARD_SIZE - 1)
BLACK_CHESS = "b"
WHITE_CHESS = "w"

#count the moves
counter=0
board = []

# Assign "empty" to every element, representing an empty spot
for i in range(BOARD_SIZE):
    row = ["empty"] * BOARD_SIZE
    board.append(row)

# Create a Tk object called root
root = Tk()

# disallow changing the window size
root.resizable(0, 0)

# Set the title to gomoku
root.title("gomoku")

# Create a canvas named cv, width set to BOARD_WIDTH and height set to BOARD_HEIGHT and add to the window. 
cv=Canvas(root, width=BOARD_WIDTH, height=BOARD_HEIGHT)
cv.pack()

#Make the board!
#create PhotoImage named bm with the file set to "image/board.png" 
bm = PhotoImage(file="image/board.png")

#create_image for the board
cv.create_image(BOARD_HEIGHT / 2 + 1, BOARD_HEIGHT / 2 + 1, image=bm)

#create a PhotoImage called selectedbm with the file ""image/selected.gif" 
img = PhotoImage(file="image/selected.gif")

# Create the image of the selected icon. This should use Canvas' create_image function offscreen, at -100, -100, with image set to img. 
selectedbm = cv.create_image(-100,-100, image=img)

#Set the create_image to selectedbm 

def move_handler(event):
    # Calculate the user's selected point and to make sure the point is between 0 to 14.
    selectedX = max(0, min(round((event.x - X_OFFSET) / X_RATE), 14))
    selectedY = max(0, min(round((event.y - Y_OFFSET) / Y_RATE), 14))
    # Move the red selected icon
    cv.coords(selectedbm, (selectedX * X_RATE + X_OFFSET,
                         selectedY * Y_RATE + Y_OFFSET))


#functions of check winning
#4 possible situation of winning:vertical,horizontal,2 diagonals
def check_vertical():
  for x in range(BOARD_SIZE):
    for y in range(BOARD_SIZE-4):
      if board[y][x] != "empty":
        piece_counter=0
        for i in range (5):
          if board[y+i][x]==board[y][x] :
            piece_counter=piece_counter+1
        if piece_counter >=5:
          print("GAME OVER")
          cv.unbind('<Button>')
          if board[y][x]=="w":
            print("white wins")
          if board[y][x]=="b":
            print("black wins")

          
def check_horizontal():
  for x in range(BOARD_SIZE-4):
    for y in range(BOARD_SIZE):
      if board[y][x] != "empty":
        piece_counter=0
        for i in range (5):
          if board[y][x+i]==board[y][x] :
            piece_counter=piece_counter+1
        if piece_counter >=5:
          print("GAME OVER")
          cv.unbind('<Button>')
          if board[y][x]=="w":
            print("white wins")
          if board[y][x]=="b":
            print("black wins")
      
def check_diagonal():
  for x in range(BOARD_SIZE-4):
    for y in range(BOARD_SIZE-4):
      if board[y][x] != "empty":
        piece_counter=0
        for i in range (5):
          if board[y+i][x+i]==board[y][x] :
            piece_counter=piece_counter+1
        if piece_counter >=5:
          print("GAME OVER")
          cv.unbind('<Button>')
          if board[y][x]=="w":
            print("white wins")
          if board[y][x]=="b":
            print("black wins")        
        
def check_counter_diagonal():
  for x in range(4,BOARD_SIZE):
    for y in range(BOARD_SIZE-4):
      if board[y][x] != "empty":
        piece_counter=0
        for i in range (5):
          if board[y+i][x-i]==board[y][x] :
            piece_counter=piece_counter+1
        if piece_counter >=5:
          print("GAME OVER")
          cv.unbind('<Button>')
          if board[y][x]=="w":
            print("white wins")
          if board[y][x]=="b":
            print("black wins")   
            

# Make a PhotoImage called black that has the file "image/black.gif" 
black = PhotoImage(file="image/black.gif")

# Make a PhotoImage called white that has the file "image/white.gif" 
white = PhotoImage(file="image/white.gif")

def click_handler(event):
     # Calculate the user's selected point to put a piece and to make sure the point is between 0 to 14.
    
    userX = max(0, min(round((event.x - X_OFFSET) / X_RATE), 14))
    userY = max(0, min(round((event.y - Y_OFFSET) / Y_RATE), 14))
    # If this spot is empty, the user can place the piece
    if board[userY][userX] == "empty":
        global counter
        if counter%2==0:   
          cv.create_image(userX * X_RATE + X_OFFSET, userY * Y_RATE + Y_OFFSET,
                        image=black)             
          board[userY][userX] = "b"
        else:
          cv.create_image(userX * X_RATE + X_OFFSET, userY * Y_RATE + Y_OFFSET,
                        image=white)
          board[userY][userX] = "w"
        counter=counter+1
        check_vertical()
        check_horizontal()
        check_diagonal()
        check_counter_diagonal()
        #while True:
        #    comX = random.randint(0, BOARD_SIZE - 1)
        #    comY = random.randint(0, BOARD_SIZE - 1)
        #    # If the spot is empty, the computer can place a piece
        #    if board[comY][comX] == "empty":
        #        break
        #cv.create_image(comX * X_RATE + X_OFFSET, comY * Y_RATE + Y_OFFSET,
        #                image=white)
        #board[comY][comX] = "w"


def leave_handler(event):
    # Move the red selection inco out of the interface.
    cv.coords(selectedbm, -100, -100)




# Bind a function for the mouse moving event. (move_handler) 
cv.bind('<Motion>', move_handler)

# Bind a function for the mouse clicking event. (click_handler) 
cv.bind('<Button>', click_handler)

# Bind a function for the mouse leaving event. 
cv.bind('<Motion>', move_handler)

root.mainloop()
