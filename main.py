from pyglet import *

class Hexagon:
    def __init__(self, x, y, r, color=(255, 255, 255, 255), batch=None, group=None):
        self.shape = shapes.Polygon([x + r, y], [x + r/2, y + r * 3 ** 0.5/2], [x - r/2, y + r * 3 ** 0.5/2], [x - r, y], [x - r/2, y - r * 3 ** 0.5/2], [x + r/2, y - r * 3 ** 0.5/2], color=color, batch=batch)
    
    def draw(self):
        self.shape.draw()


class Window(window.Window):
    resolutions = ((640, 360), (1280, 720), (1920, 1080), (3840, 2160), (2560, 1440))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(640, 360)
        self.win_width = 1280
        self.win_height = 720
        self.objects = []
        self.push_handlers(on_resize=self.loc_on_resize)

    def loc_on_resize(self, width, height):
        if (width, height) in Window.resolutions:
            return
        width, height = min(Window.resolutions, key=lambda x: abs(x[0] - width))
        self.win_width, self.win_height = width, height
            
    def on_draw(self):
        self.set_size(self.win_width, self.win_height)
        self.clear()
        for obj in self.objects:
            obj.draw()


win = Window(1280, 720, resizable=True)
batch = graphics.Batch()

bg = shapes.Rectangle(x=0, y=0, width=3000, height=3000, color=(250, 250, 230), batch=batch)
# я не придумал как нарисовать hexagon
#hexagon = shapes.Polygon([100, 100], [200, 100], [250, 200], [200, 300], [100, 300], [50, 200], color=(100, 100, 100), batch=batch)
hexagon = Hexagon(100, 100, 100, color=(100, 100, 100), batch=batch)
win.objects.append(bg)
win.objects.append(hexagon)


app.run()
