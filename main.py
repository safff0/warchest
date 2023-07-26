from pyglet import *

class Hexagon:
    def __init__(self, x, y, r, color=(255, 255, 255, 255), batch=None, group=None):
        self.shape = shapes.Polygon([x + r, y], [x + r/2, y + r * 3 ** 0.5/2], [x - r/2, y + r * 3 ** 0.5/2], [x - r, y], [x - r/2, y - r * 3 ** 0.5/2], [x + r/2, y - r * 3 ** 0.5/2], color=color, batch=batch)
    
    def draw(self):
        self.shape.draw()


resolutions = ((1280, 720), (1920, 1080), (3840, 2160), (2560, 1440))

win = window.Window(1280, 720, resizable=True)
win.config.alpha_size = 8
batch = graphics.Batch()

bg = shapes.Rectangle(x=0, y=0, width=3000, height=3000, color=(250, 250, 230), batch=batch)
# я не придумал как нарисовать hexagon
#hexagon = shapes.Polygon([100, 100], [200, 100], [250, 200], [200, 300], [100, 300], [50, 200], color=(100, 100, 100), batch=batch)
hexagon = Hexagon(100, 100, 100, color=(100, 100, 100), batch=batch)


@win.event
def on_draw():
    win.clear()
    batch.draw()
    #hexagon.draw()


@win.event
def on_resize(width, height):
    if (width, height) in resolutions:
        return
    res = min(resolutions, key=lambda x: abs(x[0] - width))
    width, height = res
    win.set_size(width, height)


app.run()
