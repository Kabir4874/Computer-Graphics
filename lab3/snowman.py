from OpenGL.GL import *          
from OpenGL.GLU import *          
from OpenGL.GLUT import *        
import math


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600



X0, Y0 = 100, 80
X1, Y1 = 200, 520


def get_zone(dx,dy):

    adx, ady = abs(dx), abs(dy)

    if adx >= ady:
        if dx >= 0 and dy >= 0:
            return 0
        if dx < 0 and dy >= 0:
            return 3
        if dx < 0 and dy < 0:
            return 4
        return 7
    else:         
        if dx >= 0 and dy >= 0:
            return 1
        if dx < 0 and dy >= 0:
            return 2
        if dx < 0 and dy < 0:
            return 5
        return 6


def convert_to_zone_0(x,y,zone):
    if zone == 0:   
        return x, y
    if zone == 1:   
        return y, x
    if zone == 2:   
        return y, -x
    if zone == 3:   
        return -x, y
    if zone == 4:   
        return -x, -y
    if zone == 5:   
        return -y, -x
    if zone == 6:   
        return -y, x
    if zone == 7:   
        return x, -y
    return x, y


def convert_back_from_zone_0(x,y,zone):
    if zone == 0:   
        return x, y
    if zone == 1:   
        return y, x
    if zone == 2:   
        return -y, x
    if zone == 3:   
        return -x, y
    if zone == 4:   
        return -x, -y
    if zone == 5:   
        return -y, -x
    if zone == 6:   
        return y, -x
    if zone == 7:   
        return x, -y
    return x, y

def mid_point_circle(cx, cy, r):

    pts = []
    x = 0
    y = r
    d = 1 - r

    def plot8(cx, cy, x, y):
        pts.extend([
            (cx + x, cy + y),
            (cx + y, cy + x),
            (cx + y, cy - x),
            (cx + x, cy - y),
            (cx - x, cy - y),
            (cx - y, cy - x),
            (cx - y, cy + x),
            (cx - x, cy + y),
        ])

    plot8(cx, cy, x, y)
    while x <= y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        plot8(cx, cy, x, y)

    return pts


def mid_point_line(X1, Y1, X2, Y2):
    points = []  

    dx = X2 - X1
    dy = Y2 - Y1

    zone = get_zone(dx, dy)

    x0_z0, y0_z0 = convert_to_zone_0(X1, Y1, zone)
    x1_z0, y1_z0 = convert_to_zone_0(X2, Y2, zone)

    dx = x1_z0 - x0_z0
    dy = y1_z0 - y0_z0

    dx = abs(dx)
    dy = abs(dy)

    x = x0_z0
    y = y0_z0
    xr,yr= convert_back_from_zone_0(x,y,zone)
    points.append((xr,yr))

    if dx >= dy:
        d = 2 * dy - dx
        for _ in range(dx):
            x += 1
            if d <= 0:
                d += 2 * dy
            else:
                y += 1
                d += 2 * (dy - dx)
            xr,yr= convert_back_from_zone_0(x,y,zone)
            points.append((xr,yr))
    else:
        d = 2 * dx - dy
        for _ in range(dy):
            y += 1
            if d <= 0:
                d += 2 * dx
            else:
                x += 1
                d += 2 * (dx - dy)
                xr,yr= convert_back_from_zone_0(x,y,zone)
                points.append((xr,yr))

    return points

    



def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0) 
    glPointSize(4.0)

    glBegin(GL_POINTS)


    circle_pts = mid_point_circle(300, 150, 140)
    for x, y in circle_pts:
        glVertex2f(float(x), float(y))


    circle_pts = mid_point_circle(300, 360, 110)
    for x, y in circle_pts:
        glVertex2f(float(x), float(y))


    circle_pts = mid_point_circle(300, 380, 10)
    for x, y in circle_pts:
        glVertex2f(float(x), float(y))

    circle_pts = mid_point_circle(300, 320, 10)
    for x, y in circle_pts:
        glVertex2f(float(x), float(y))



    circle_pts = mid_point_circle(300, 520, 80)
    for x, y in circle_pts:
        glVertex2f(float(x), float(y))
    
    circle_pts = mid_point_circle(260, 560, 10)
    for x, y in circle_pts:
        glVertex2f(float(x), float(y))

    circle_pts = mid_point_circle(340, 560, 10)
    for x, y in circle_pts:
        glVertex2f(float(x), float(y))


    points= mid_point_line(300,540,300,510)
    for x, y in points:
        glVertex2f(float(x), float(y))

    points= mid_point_line(300,540,350,525)
    for x, y in points:
        glVertex2f(float(x), float(y))

    points= mid_point_line(300,510,350,525)
    for x, y in points:
        glVertex2f(float(x), float(y))

    circle_pts = mid_point_circle(300, 520, 40)
    for x, y in circle_pts:
        if y<500:
            glVertex2f(float(x), float(y))
        




    glEnd()

    glutSwapBuffers()


def reshape(width, height):


    glViewport(0, 0, width, height)


    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()


    gluOrtho2D(0, width, 0, height)


    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()




def init_glut_window():
 

    glutInit()

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)

    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)

    glutInitWindowPosition(400, 100)

    glutCreateWindow(b"DDA Line Drawing Algorithm - PyOpenGL + GLUT")

    glutDisplayFunc(display)  
    glutReshapeFunc(reshape)  
    glClearColor(0.0, 0.0, 0.0, 1.0) 




def main():

    init_glut_window()


    glutMainLoop()




if __name__ == "__main__":
    main()
