from __future__ import division, absolute_import, print_function
import unittest
from svgpathtools import *

class TestSVG2Paths(unittest.TestCase):
    def test_svg2paths_polygons(self):

        paths, _ = svg2paths('polygons.svg')

        # triangular polygon test
        path = paths[0]
        path_correct = Path(Line(55.5+0j, 55.5+50j), 
                            Line(55.5+50j, 105.5+50j), 
                            Line(105.5+50j, 55.5+0j))
        self.assertTrue(path.isclosed())
        self.assertTrue(len(path)==3)
        self.assertTrue(all(path[k].end==path[k+1].start 
                                for k in range(len(path))))

        # triangular polygon with redundant 4th "closure" point
        path = paths[1]
        path_correct = Path(Line(0+0j, 0+100j),
                            Line(0+100j, 100+100j),
                            Line(100+100j, 55.5+0j))

        self.assertTrue(path.isclosed())
        self.assertTrue(len(path)==3)
        self.assertTrue(all(path[k].end==path[k+1].start 
                                for k in range(len(path))))
