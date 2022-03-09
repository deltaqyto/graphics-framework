import glfw
from OpenGL.GL import *


class Window:
    def __init__(self, size=(720, 480), title="Untitled screen"):
        self.title = title
        self.size = size
        self.clear_flags = (False, False)
        self.clear_color = (0.0, 0, 0.4, 0)
        glfw.init()
        glfw.window_hint(glfw.SAMPLES, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        self.window = glfw.create_window(*size, title, None, None)

        glfw.make_context_current(self.window)

        glClearColor(0.0, 0, 0.4, 0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)

    def swap(self):
        glfw.swap_buffers(self.window)

    def clear(self, do_color=True, do_depth=True):
        glClearColor(*self.clear_color)
        if do_color:
            glClear(GL_COLOR_BUFFER_BIT)
        if do_depth:
            glClear(GL_DEPTH_BUFFER_BIT)
        self.clear_vals = (do_color, do_depth)
