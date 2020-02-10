# Маленькая геометрическая библиотека
# точки обозначаются заглавными
# вектора обозначаются маленькими буквами
from math import sqrt


class Abstract2D():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __str__(self):
        return '%f %f' % (self.x, self.y)
    
    def add(self, a, t):
        return self.x + a.x*t, self.y + a.y*t

class Point2D(Abstract2D):
    pass
class Vector2D(Abstract2D):
    pass

# расстояние между лучём и точкой
def distance(a: Vector2D, A0: Point2D, B: Point2D):
    try:
        t = (a.x * (B.x - A0.x) + a.y * (B.y - A0.y)) / (a.x**2 + a.y**2)
        A1 = Point2D(A0.x+a.x*t, A0.y+a.y*t)
        return distance_between_points(A1,B)
    except:
        pass

# расстояние между 2 точками
def distance_between_points(A: Point2D, B: Point2D):
    return sqrt((A.x-B.x)**2 + (A.y-B.y)**2)

# рассчёт точки пересечения
# A0        начальная точка перехватываемого объекта
# v         вектор его движения
# B0        точка перехватчика
# v_bullet  скорость перехвата
def calc_aim(bullet: Point2D, v_aim: Vector2D, aim: Point2D, v_bullet):
    dx = bullet.x - aim.x
    dy = -(bullet.y - aim.y)
    a_eq = v_aim.x**2 + v_aim.y**2 - v_bullet**2
    b_eq = 2*(v_aim.x*dx + v_aim.y*dy)
    c_eq = dx**2 + dy**2
    t1, t2 = calc_roots(a_eq, b_eq, c_eq)
    t = max(t1, t2)
    return aim.add(v_aim, t)

# поиск корней уравнения a*x^2 + b*x + c = 0
def calc_roots(a, b, c):
    D = b**2 - 4*a*c
    sqrt_D = sqrt(D)
    root1 = (-b + sqrt_D) / (2.0*a) 
    root2 = (-b - sqrt_D) / (2.0*a)
    return root1, root2