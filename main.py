import pyglet

win = pyglet.window.Window(480,240)

cells = []

# init, color all cells
for i in range(0,49):
    cells.append([1 for j in range(0, 25)])

@win.event
def on_draw():
    xit = 0
    for i in cells: # column
        yit = 0
        for j in i: # cell
            pyglet.shapes.Rectangle(0+xit*10,0+yit*10,10,10,(0,255,0)).draw()
            print("drawn at "+ str(0+xit*10) + ", "+str(0+yit*10))
            yit+=1
        xit+=1

    win.clear()

pyglet.app.run()