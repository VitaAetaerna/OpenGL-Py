import pygame as pg
import moderngl as mgl
import numpy as numpy
import time
WIN_RES = (600, 600)

class Engine():
    def __init__(self):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = "auto"

        self.clock = pg.time.Clock()
        self.deltaTIme = 0
        self.time = 0
        self.is_running = True


    def update(self):
        self.deltaTIme = pg.time.Clock.tick()
        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f'{ self.clock.get_fps() :.0f}')
            
    def Render(self):
        print("rendering")
    def handle_Events(self):
        print("handling or smth")

if __name__ == "__main__":
    App = Engine()
    App.run()
