from pyglet import *


resolutions = ((1280, 720), (1920, 1080), (3840, 2160), (2560, 1440))

win = window.Window(1280, 720, resizable=True)
win.config.alpha_size = 8
batch = graphics.Batch()

bg = shapes.Rectangle(x=0, y=0, width=3000, height=3000, color=(250, 250, 230), batch=batch)
# я не придумал как нарисовать hexagon
hexagon = shapes.Rectangle(x=500, y=500, width=400, height=400, batch=batch)


@win.event
def on_draw():
    win.clear()
    batch.draw()
    hexagon.draw()


@win.event
def on_resize(width, height):
    if (width, height) in resolutions:
        return
    res = min(resolutions, key=lambda x: abs(x[0] - width))
    width, height = res
    win.set_size(width, height)


app.run()
