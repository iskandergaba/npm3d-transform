from math import sin, cos

def translate(vertices, tx, ty, tz):
    for v in vertices:
        v['x'] = v['x'] + tx
        v['y'] = v['y'] + ty
        v['z'] = v['z'] + tz        
    return vertices

def rotate_z(vertices, theta, diff_origin=False):
    sin_t = sin(theta)
    cos_t = cos(theta)
    for v in vertices:
        dx, dy = v['x'], v['y']
        if diff_origin:
            dx = v['x'] - v['x_origin']
            dy = v['y'] - v['y_origin']
        v['x'] = dx * cos_t - dy * sin_t
        v['y'] = dy * cos_t + dx * sin_t
    return vertices

def rotate_y(vertices, theta, diff_origin=False):
    sin_t = sin(theta)
    cos_t = cos(theta)
    for v in vertices:
        dx, dz = v['x'], v['z']
        if diff_origin:
            dx = v['x'] - v['x_origin']
            dz = v['z'] - v['z_origin']
        v['x'] = dx * cos_t - dz * sin_t
        v['z'] = dz * cos_t + dx * sin_t
    return vertices

def rotate_x(vertices, theta, diff_origin=False):
    sin_t = sin(theta)
    cos_t = cos(theta)
    for v in vertices:
        dy, dz = v['y'], v['z']
        if diff_origin:
            dy = v['y'] - v['y_origin']
            dz = v['z'] - v['z_origin']
        v['y'] = dy * cos_t - dz * sin_t
        v['z'] = dz * cos_t + dy * sin_t
    return vertices
