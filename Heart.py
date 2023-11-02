import turtle
from turtle import *
wn=Screen()
wn.bgcolor('light blue')
t=turtle.Turtle()
t.pencolor('white')
def curve():
    for _ in range(200):
        t.rt(1)
        t.fd(1)
def heart():
    t.fillcolor('pink')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(110)
    t.end_fill()

heart()
t.ht()
def write(message,pos):
        x,y=pos
        t.penup()
        t.goto(x,y)
        t.color('white')
        style=('Stencil Std',22,'italic')
        t.write(message,font=style)

write('H',(-50,250))
write('a',(-35,250))
write('p',(-23,250))
write('p',(-11,250))
write('i',(0,250))
write('n',(6,250))
write('e',(18,250))
write('s',(30,250))
write('s',(40,250))

def write(message,pos):
        x,y=pos
        t.penup()
        t.goto(x,y)
        t.color('white')
        style=('Stencil Std',19,'italic')
        t.write(message,font=style)


write('I',(-68,95))
write('L',(-55,95))
write('O',(-42,95))
write('V',(-30,95))
write('E',(-14,95))
write('Y',(10,95))
write('O',(26,95))
write('U',(45,95))
def write(message,pos):
        x,y=pos
        t.penup()
        t.goto(x,y)
        t.color('white')
        style=('Stencil Std',19,'italic')
        t.write(message,font=style)

write('C',(-75,-80))
write('ô',(-62,-80))
write('G',(-46,-80))
write('á',(-32,-80))
write('i',(-22,-80))
write('C',(-15,-80))
write('ủ',(-2,-80))
write('a',(7,-80))
write('T',(22,-80))
write('ô',(32,-80))
write('i',(42,-80))
write('<3',(50,-80))


wn.mainloop()