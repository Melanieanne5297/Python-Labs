def equilateral(sides):
    """equal on all sides"""
    a,b,c =sides
    return (a == b == c and
            a > 0 and b > 0 and c > 0 
            and a + b > c 
            and b + c > a 
            and a + c > b
           )

def isosceles(sides):
    """2 sides are equal"""
    a, b, c = sides
    return ((a == b or c == a or b == c )
            and a > 0 and b > 0 and c > 0 
            and a + b > c 
            and b + c > a 
            and a + c > b
           )

def scalene(sides):
    """no equal sides"""
    a, b, c = sides
    return ((a != b and a != c and b != c)
           and a > 0 and b > 0 and c > 0 
           and a + b > c 
           and b + c > a 
           and a + c > b
           )
