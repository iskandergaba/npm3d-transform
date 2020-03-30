import os
import numpy as np
from ply import read_ply, write_ply
from transform import translate, rotate_x, rotate_y, rotate_z


def main():
    if not os.path.exists('./ply'):
        os.makedirs('./ply')
    for root, dirs, files in os.walk('./ply'):
        for file in files:
            if file.endswith('.ply'):
                print('Transforming', file, '...')
                transform(root, file)
                print('Transforming', file, 'done.')


def transform(root, filename):
    if not os.path.exists('./ply_gen'):
        os.makedirs('./ply_gen')
    # Example transformation.
    # 1. Read the PLY data file.
    data = read_ply(os.path.join(root, filename))
    # 2. Shift points by the vector (25, -10, 7).
    data = translate(data, 25, -10, 7)
    # 3. Rotate points 45 degress around the Z-axis.
    data = rotate_z(data, 45)
    # 4. Write the new points into a new PLY data file.
    write_ply(os.path.join('./ply_gen', filename), [data['x'], data['y'], data['z'], data['x_origin'], data['y_origin'], data['z_origin'],
                                                    data['GPS_time'], data['reflectance']], ['x', 'y', 'z', 'x_origin', 'y_origin', 'z_origin', 'GPS_time', 'reflectance'])


if __name__ == "__main__":
    main()
