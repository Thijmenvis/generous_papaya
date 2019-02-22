import turtle as tl

def star():
    tl.color('red', 'yellow')
    tl.begin_fill()
    while True:
        tl.forward(200)
        tl.left(170)
        if abs(tl.pos()) < 1:
            break
    tl.end_fill()
    tl.done()

def yes_it_is(x, y):
    tl.goto(x, y)
    tl.write("yes it is!", align='center', font=('Helvetica', 11))

tl.ht()
tl.bgcolor('lightsteelblue')
tl.pencolor('orange')
tl.screensize(300, 300)
tl.write("is this a game?", align='center', font=('Helvetica', 36))

star()

tl.mainloop()
