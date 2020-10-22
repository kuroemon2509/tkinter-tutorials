import pyglet

if __name__ == "__main__":
    window = pyglet.window.Window()
    image = pyglet.resource.image('sample.png')

    @window.event
    def on_draw():
        window.clear()
        image.blit(0, 0)

    pyglet.app.run()
