import Point
from PyCartes import Line





def tester(a_x=0, a_y=0, b_x=0, b_y=0 ):
    a = Point.Point(a_x, a_y)
    b = Point.Point(b_x, b_y)
    l1 = Line.Line(a, b)

    print "slope -", l1.slope()
    print "is_in_origin -", l1.is_in_origin()
    print "dist -", l1.dist()
    print "line_equation -", l1.line_equation()
    print "draw_line -", l1.draw_line()
    print "mid_point_coor -", l1.mid_point_coor()
    print "y_intersect -", l1.y_intersect()
    print "x_intersect -", l1.x_intersect()


if __name__=='__main__':
    tester(1,8,2,4)

# l1.draw_line(dots_color="red")

# l =Line.Line(poin_l[0],a)



# print l.slope()
# print l.y_intersect()
# print l.line_equation()



