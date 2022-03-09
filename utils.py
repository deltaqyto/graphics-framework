from OpenGL import GL


def print_opengl_error():
    err = GL.glGetError()
    if err != GL.GL_NO_ERROR:
        print(f"An error was encountered: {GL.gluErrorString(err)}")
