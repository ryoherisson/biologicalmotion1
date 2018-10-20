from tkinter import *
import math as m

# 頭、首、上腕１、腕１、上腕２、腕２、腹、腿１、腿２、脚１、脚２
ball = {
    'x': [20, 20, 20, 30, 20, 30, 20, 32, 32, 18, 18],
    'y': [-10, 70, 140, 220, 140, 220, 190, 280, 280, 380, 380],
    'w': 20,
    'r': 120,
    'c': [30, 18, 12, 6, 12, 6, 18, 10, 10, 6, 6],
    'B': [0, 0, 0, 0, m.pi, m.pi, 0.9*m.pi, 0, m.pi, 0, m.pi],
}

theta = 0
g = 9.8
t = [0]
β = 0
n = len(ball['x'])
temp = {}

for i in range(n):
    temp.setdefault('x', []).append(ball['x'][i])
    temp.setdefault('y', []).append(ball['y'][i])


win = Tk()
cv = Canvas(win, width = 1000, height = 600, bg="black")
cv.pack()


def draw_objects():
    cv.delete('all')
    for i in range(n):
        cv.create_oval(
            ball['x'][i],
            ball['y'][i],
            ball['x'][i] + ball['w'],
            ball['y'][i] + ball['w'],
            fill='white')

def move_ball():
    if ball['x'][0] > 1050:
        temp['x'] = [20, 20, 20, 30, 20, 30, 20, 32, 32, 18, 18]
        temp['y'] = [-10, 70, 140, 220, 140, 220, 190, 280, 280, 380, 380]

    for i in range(n):
        theta = m.pi / ball['c'][i]
        l = ball['r']
        w = m.sqrt(g / l)
        bx = l * m.sin(theta) * m.cos(t[0]*w + ball['B'][i])
        ball['x'][i] = temp['x'][i] + bx
        ball['y'][i] = temp['y'][i] + m.sqrt(l**2 - bx**2)
        if (t[0]*w) % (2*m.pi) <= m.pi:
            temp['x'][i] += l * m.sin(m.pi/ball['c'][10]) * (m.cos(t[0]*w)-m.cos((t[0]+0.5)*w))

        else:
            temp['x'][i] -= l * m.sin(m.pi/ball['c'][10]) * (m.cos(t[0]*w)-m.cos((t[0]+0.5)*w))

    t[0] += 0.5

def game_loop():
    draw_objects()
    move_ball()
    win.after(50, game_loop)

game_loop()
win.mainloop()
