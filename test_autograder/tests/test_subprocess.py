import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess
import itertools


class TestDiff(unittest.TestCase):
    def setUp(self):
        pass 

    @weight(5)
    def test_sanity_proj2_1(self):
        """Sanity Check: proj2-1.c"""

        # Create a subprocess to run the students code to obtain an output 
        try:
            test = subprocess.Popen(["./p2-1.out"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
            test.kill()
            self.assertTrue(True)
        except:
            self.fail(msg = 'file proj2-1.c either doesn\'t exist, or doesn\'t compile\n\nCheck your submitted file\'s name, and make sure the code compiles on grace.')

        test.terminate()

    @weight(5)
    def test_sanity_proj2_2(self):
        """Sanity Check: proj2-2.c"""

        # Create a subprocess to run the students code to obtain an output 
        try:
            test = subprocess.Popen(["./p2-2.out"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
            test.kill()
            self.assertTrue(True)
        except:
            self.fail(msg = 'file proj2-2.c either doesn\'t exist, or doesn\'t compile\n\nCheck your submitted file\'s name, and make sure the code compiles on grace.')

        test.terminate()

    @weight(5)
    def test_sanity_proj2_3(self):
        """Sanity Check: proj2-3.c"""

        # Create a subprocess to run the students code to obtain an output 
        try:
            test = subprocess.Popen(["./p2-3.out"], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
            test.kill()
            self.assertTrue(True)
        except:
            self.fail(msg = 'file proj2-3.c either doesn\'t exist, or doesn\'t compile\n\nCheck your submitted file\'s name, and make sure the code compiles on grace.')

        test.terminate()

    @weight(5)
    def test_Public_1(self):
        """Exercise One - Public 1"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public00.in', 'r')
        time = input.readline()
        input.close()

        input = open('./public00.in', 'r')
        output = open('./myPublic00.output','w')

        test = subprocess.Popen(["./a.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic00.output', 'r') as myOutput, open('./public00.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue='_'):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput: " + input + "\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))

        test.terminate()