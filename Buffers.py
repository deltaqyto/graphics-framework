from OpenGL.GL import *


class Vao:
    def __init__(self):
        self.id = glGenVertexArrays(1)
        self.buffers = []
        glBindVertexArray(self.id)

        self.buffer_count = 0

    def bind(self):
        glBindVertexArray(self.id)
        for i in range(len(self.buffers)):
            glEnableVertexAttribArray(i)

    def unbind(self):
        for i in range(len(self.buffers)):
            glDisableVertexAttribArray(i)
        glBindVertexArray(0)

    def add_buffer(self, buffer):
        self.buffers.append(buffer)
        self.bind()
        buffer.bind()
        glVertexAttribPointer(self.buffer_count, 3, GL_FLOAT, #buffer.size, {float: GL_FLOAT, int: GL_INT}[buffer.data_type],
                              GL_FALSE, 0, None)
        glEnableVertexAttribArray(self.buffer_count)

        self.buffer_count += 1

    def draw(self, mode, draw_range=None):
        if not self.buffers:
            return

        self.bind()
        if draw_range is None:
            glDrawArrays({"tris": GL_TRIANGLES, "lines": GL_LINES}[mode], 0, len(self.buffers[0].data))
        else:
            glDrawArrays({"tris": GL_TRIANGLES, "lines": GL_LINES}[mode], *draw_range)
        self.unbind()


class Vbo:
    def __init__(self):
        self.id = glGenBuffers(1)
        self.bind()
        self.size = 1
        self.data_type = None
        self.data = []

    def bind(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.id)

    def unbind(self):
        glBindBuffer(0)

    def set_data(self, data, size=1, data_type=float, mode=GL_STATIC_DRAW):
        self.bind()
        self.size = size
        self.data = data
        self.data_type = data_type
        formats = {float: (4, GLfloat), int: (4, GLint)}
        data = [data_type(d) for d in data]
        glBufferData(GL_ARRAY_BUFFER, len(data) * formats[data_type][0],
                     (formats[data_type][1] * len(data))(*data), mode)