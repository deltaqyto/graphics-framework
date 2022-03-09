from OpenGL import GL as gl
from utils import print_opengl_error


class Shader:
    def __init__(self, vert="", frag="", vert_is_file=False, frag_is_file=False, verbose=False):
        self.vert_source = open(vert + ".vert").read() if vert_is_file else vert
        self.frag_source = open(vert + ".frag").read() if frag_is_file else frag

        self.verbose = verbose

        self.vert = self.compile(self.vert_source, "v")
        self.frag = self.compile(self.frag_source, "f")

        self.prog = self.link()

    def compile(self, prog, mode):
        shader = gl.glCreateShader({"v": gl.GL_VERTEX_SHADER, "f": gl.GL_FRAGMENT_SHADER}[mode])
        gl.glShaderSource(shader, prog)
        gl.glCompileShader(shader)
        if not self.verbose and gl.GL_TRUE != gl.glGetShaderiv(shader, gl.GL_COMPILE_STATUS):
            err = gl.glGetShaderInfoLog(shader)
            raise AssertionError(f"Failed to compile {mode} shader", err)
        print_opengl_error()
        return shader

    def link(self):
        if self.vert is None or self.frag is None:
            print("Shader is not compiled")
            return None
        program = gl.glCreateProgram()
        gl.glAttachShader(program, self.vert)
        gl.glAttachShader(program, self.frag)
        gl.glLinkProgram(program)
        if not self.verbose and gl.GL_TRUE != gl.glGetProgramiv(program, gl.GL_LINK_STATUS):
            err = gl.glGetProgramInfoLog(program)
            raise Exception(err)
        print_opengl_error()
        return program

    def bind(self):
        if gl.glUseProgram(self.prog):
            print_opengl_error()

    def unbind(self):
        gl.glUseProgram(0)

    def get_loc(self, name):
        return gl.glGetUniformLocation(self.prog, name)

    def set_value(self, name, value):
        options = {"mat4fv": gl.glUniformMatrix4fv}  # todo implement fully
        gl.glUniformMatrix4fv(gl.glGetUniformLocation(self.prog, name), 1, gl.GL_FALSE, value)
