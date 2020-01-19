import numpy as np
n = input("How many sides? ").replace(",", "")
p = float(n) * ( np.sqrt( 0.5 - (0.5 * np.cos((2 * np.pi)/float(n))) ) )
print(p)

#   this spits out perimeter of an n-sided polygon inscribed in a circle of diameter 1
#   by definition, lim (n->infinity) perimeter approaches pi as it's perimeter approaches the circle's circumference
#   I want to be able to see this so...
# todo: try and animate this in something like manim or mathematica