from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def MidpointCircle(radius, x0, y0):
    x = radius
    y = 0
    p = 1 - radius  

    Circlepoints(x, y, x0, y0)

    while x > y:
        y += 1
        if p <= 0:
            x -= 1
            p = p + 2 * y + 1
        else:

            

            p = p + 2 * y - 2 * x + 1
        Circlepoints(x, y, x0, y0)
    
    
def Circlepoints(x, y, x0, y0):


    draw_points(x + x0, y + y0)
    draw_points(y + y0, x + x0)
    draw_points(y + y0, -x + x0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + y0, -x + x0)
    draw_points(-y + y0, x + x0)
    draw_points(-x + x0, y + y0)




def draw_points(x, y):
    glPointSize(3) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()




def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    x = 250
    y = 250
    radius = 150
    MidpointCircle(radius, x, y)



    # MidpointCircle(75,325,250)
    # MidpointCircle(75,175,250)
    # MidpointCircle(75,250,325)
    # MidpointCircle(75,250,175)

    # MidpointCircle(75,303,303)
    # MidpointCircle(75,197,303)
    # MidpointCircle(75,197,197)
    # MidpointCircle(75,303,197)


    MidpointCircle(50,250,400)
    MidpointCircle(50,100,250)
    MidpointCircle(50,250,100)
    MidpointCircle(50,400,250)



    MidpointCircle(50,356,356)
    MidpointCircle(50,144,356)
    MidpointCircle(50,144,144)
    MidpointCircle(50,356,144)

    


   
    glutSwapBuffers()






glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)


glutMainLoop()
