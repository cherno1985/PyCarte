import math
import matplotlib.pyplot as plt


class Line:

    """
    stuff to do -

    * take care of quations from the type of x=number, we have division by zero
    * check all other stuff

    """

    def __init__(self, dot_1, dot_2):
        self.dot_1 = dot_1
        self.dot_2 = dot_2

    def dist(self):
        return math.sqrt((self.dot_2.x - self.dot_1.x) ** 2 + (self.dot_2.y - self.dot_1.y) ** 2)

    def slope(self):
        if self.dot_2.x == self.dot_1.x:
            return None
        else:
            return float(format(float(self.dot_2.y - self.dot_1.y) / (self.dot_2.x - self.dot_1.x), '.2f'))

    def y_intersect(self):
        if self.slope() is None and self.dot_1.x==0:
            return 0
        elif self.slope() is None and self.dot_1.x!=0:
            None
        else:
            return -1 * self.slope() * self.dot_1.x + self.dot_1.y

    def x_intersect(self):
        if self.slope() is None and self.dot_1.x == 0 or self.dot_2.x == 0:
            return 0
        elif self.slope() is None:
            return False
        else:
            return self.dot_1.x - (self.dot_1.y / self.slope())


    def line_equation(self):
        if self.slope() is None:
            return "x={}".format(self.dot_1.x)
        elif self.y_intersect()==0 and self.slope()==0:
            return "y =0"
        elif self.slope()==0:
            return "y = {}".format(self.y_intersect())
        elif self.y_intersect()==0:
            return "y = {} *x ".format(self.slope())
        else:
            return "y = {} *x + {}".format(self.slope(), self.y_intersect())

    def is_in_origin(self):
        if self.slope() is None:
            return self.dot_1.y == 0
        else:
            return self.x_intersect()==0 and self.y_intersect()==0

    def mid_point_coor(self):
        x_mid = float(format((self.dot_1.x + self.dot_2.x) / 2, '.2f'))
        y_mid = float(format((self.dot_1.y + self.dot_2.y) / 2, '.2f'))
        return (x_mid, y_mid)

    def draw_line(self, dots_color="green", midpo_color="red"):
        """
         - Doesn't yet support drawing for 2 lines simultaniously
         -
        """
        xs = [self.dot_1.x, self.dot_2.x]
        ys = [self.dot_1.y, self.dot_2.y]

        f = plt.figure()
        fig = f.add_subplot(111)


        #Axis
        plt.plot([-1*self.dist(), 1*self.dist()], [0, 0], 'k-', lw=1.5)
        plt.plot([0, 0], [-1 * self.dist(), 1 * self.dist()], 'k-', lw=1.5)


        #Actual line
        fig.plot(xs, ys, lw=1.5)

        #Assisting points
        plt.plot(self.mid_point_coor()[0], self.mid_point_coor()[1], marker="o", markersize=3, color=midpo_color)
        plt.plot(self.dot_1.x, self.dot_1.y, marker="o", markersize=3, color=dots_color)
        plt.plot(self.dot_2.x, self.dot_2.y, marker="o", markersize=3, color=dots_color)
        plt.plot
        plt.show()








