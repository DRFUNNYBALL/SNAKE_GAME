import tkinter as tk, random
from tkinter import messagebox
####################################

Rows = 25
Cols = 25
tile_size = 25

window_width = tile_size * Rows
window_height = tile_size * Cols

######################################
app = tk.Tk()
app.resizable(False, False)
app.title("SNAKE GAME")
app.iconbitmap('image//sn.ico')

canvas = tk.Canvas(app, bg = "black", width= window_height, height= window_height, borderwidth=0, highlightthickness=0)
canvas.pack()
app.update()

class Tile :
    def __init__(self, x, y):
        self.x = x
        self.y = y
snake = Tile(5*tile_size, 5*tile_size)#for snake head
food = Tile(10*tile_size, 10*tile_size)
snake_body = [] 
velocityX = 0
velocityY = 0
game_over = False
score = 0 
def change_diraction(e):
    global velocityX, velocityY, game_over
    if (game_over):
        return
    
    if (e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    if (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = +1
    if (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    if (e.keysym == "Right" and velocityX != -1):
        velocityX = +1
        velocityY = 0   
def move():
    global snake, food, snake_body, game_over, score
    if (game_over):
        return
    if (snake.x < 0 or snake.x >= window_width or snake.y <0 or snake.y >= window_height):
        game_over = True
        return
    for tile in snake_body:
        if (snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return
    
    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, Cols-1) * tile_size
        food.y = random.randint(0, Cols-1) * tile_size
        score += 1

    #update snaek body :
    for i in range(len(snake_body)-1 , -1, -1):
        tile = snake_body[i]
        if (i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]    
            tile.x = prev_tile.x
            tile.y = prev_tile.y
            
    snake.x += velocityX * tile_size
    snake.y += velocityY * tile_size
    
def draw():
    global snake, food, snake_body, game_over, score
    move()
    
    canvas.delete("all")
    
    #draw food
    canvas.create_rectangle(food.x, food.y, food.x + tile_size, food.y + tile_size, fill="Green")
  
    #draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + tile_size, snake.y + tile_size, fill= "blue")
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + tile_size, tile.y + tile_size, fill = "blue")
    if (game_over):
        canvas.create_text(window_height/2, window_width/2, font= "Arial 20", text=f"""GAME OVER LOSSSSER LOL XD 
        YOUR SCORE WAS:{score}""", fill = "Red")
    else:
        canvas.create_text(30, 20, font= "Arial 10", text = f"Score {score}", fill = "white")
    app.after(100, draw) 
    

    
draw()

app.bind("<KeyRelease>", change_diraction)#for keys
app.mainloop()