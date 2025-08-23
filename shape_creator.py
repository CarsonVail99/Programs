#Super() is good to reduce repeating yourself
import math

class Shapes:
    def __init__(self, color=None, filled=None):
        self.color = color
        self.filled = bool(filled) if filled is not None else None

class Circle(Shapes):
    def __init__(self, radius, color=None, filled=None, depth=None):
        super().__init__(color, filled)
        self.name = 'circle'
        self.radius = float(radius)
        self.depth = None if depth is None else float(depth)

class Square(Shapes):
    def __init__(self, width, height, color=None, filled=None, depth=None):
        super().__init__(color, filled)
        self.name = 'square'
        self.width = float(width)
        self.height = float(height)
        self.depth = None if depth is None else float(depth)

class Triangle(Shapes):
    def __init__(self, base, height, color=None, filled=None, depth=None):
        super().__init__(color, filled)
        self.name = 'triangle'
        self.base = float(base)
        self.height = float(height)
        self.depth = None if depth is None else float(depth)

def shape_maker():
    shape_type = input('Enter the shape type: (circle, square, triangle)').strip().lower()
    if shape_type == 'circle':
        radius = input('Enter the radius: ')
        return Circle(radius)
    elif shape_type == 'square':
        width = input('Enter the width: ')
        height = input('Enter the height: ')
        return Square(width, height)
    elif shape_type == 'triangle':
        base = input('Enter the base: ')
        height = input('Enter the height: ')
        return Triangle(base, height)
    else:
        print('Invalid shape type')
        return None

def color_maker(shape):
    if shape is None:
        return None
    color = input('Enter the color: ')
    shape.color = color
    filled_input = (input('Is the shape filled? (y/n)')).lower()
    filled = filled_input in ['y', 'yes']
    shape.filled = filled
    return shape

def area_maker(shape):
    if isinstance(shape, Circle):
        area =  float(math.pi * shape.radius ** 2)
    elif isinstance(shape, Square):
        area = float(shape.width * shape.height)
    elif isinstance(shape, Triangle):
        area = float(0.5 * shape.base * shape.height)
    else:
        area = None
    return area

def volume_maker(shape):
    dimensions_ask = input('Is your object 3D (y/n)? ')
    if dimensions_ask in ['yes', 'y']:
        depth = float(input('Enter the depth: '))
        shape.depth = depth
        if isinstance(shape, Circle):
            volume = float(4/3 * math.pi * shape.radius ** 3)
            return volume
        elif isinstance(shape, Square):
            volume = (shape.width * shape.height * shape.depth)
            return volume
        elif isinstance(shape, Triangle):
            volume = float(0.5 * shape.base * shape.height * shape.depth)
            return volume
        else:
            return None
    else:
        return None


def main():
    shape = shape_maker()
    shape = color_maker(shape)
    area = area_maker(shape)
    volume = volume_maker(shape)
    if volume is None:
        print(f'You have made a {shape.name} with color {shape.color} and A filled status: {shape.filled}, the area is {area} meters.')
    else:
        print(f'You have made a {shape.name} with color {shape.color} and A filled status: {shape.filled}, the volume is {volume} meters.')


if __name__ == '__main__':
    main()

