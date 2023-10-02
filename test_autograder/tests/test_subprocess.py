import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess
import itertools


class TestDiff(unittest.TestCase):
    def setUp(self):
        pass 

    @weight(16)
    def test_Public00(self):
        """Public 0"""

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
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue='_'):
                self.assertTrue(myLine == correctLine, msg=("\nInput: " + time + "\nExpected Line: " + correctLine + "\nFound Line: " + myLine))

        test.terminate()

    @weight(16)
    def test_Public01(self):
        """Public 1"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public01.in', 'r')
        time = input.readline()
        input.close()

        input = open('./public01.in', 'r')
        output = open('./myPublic01.output','w')

        test = subprocess.Popen(["./a.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic01.output', 'r') as myOutput, open('./public01.output', 'r') as correctOutput:
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue='_'):
                self.assertTrue(myLine == correctLine, msg=("\nInput: " + time + "\nExpected Line: " + correctLine + "\nFound Line: " + myLine))

        test.terminate()

    @weight(17)
    def test_Public02(self):
        """Public 2"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public02.in', 'r')
        time = input.readline()
        input.close()

        input = open('./public02.in', 'r')
        output = open('./myPublic02.output','w')

        test = subprocess.Popen(["./a.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic02.output', 'r') as myOutput, open('./public02.output', 'r') as correctOutput:
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue='_'):
                self.assertTrue(myLine == correctLine, msg=("\nInput: " + time + "\nExpected Line: " + correctLine + "\nFound Line: " + myLine))

        test.terminate()

    @weight(17)
    def test_Release00(self):
        """Release 0"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./release00.in', 'r')
        time = input.readline()
        input.close()

        input = open('./release00.in', 'r')
        output = open('./myRelease00.output','w')

        test = subprocess.Popen(["./a.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myRelease00.output', 'r') as myOutput, open('./release00.output', 'r') as correctOutput:
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue='_'):
                self.assertTrue(myLine == correctLine, msg=("\nInput: " + time + "\nExpected Line: " + correctLine + "\nFound Line: " + myLine))

        test.terminate()

    @weight(17)
    def test_Release01(self):
        """Release 1"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./release01.in', 'r')
        time = input.readline()
        input.close()

        input = open('./release01.in', 'r')
        output = open('./myRelease01.output','w')

        test = subprocess.Popen(["./a.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myRelease01.output', 'r') as myOutput, open('./release01.output', 'r') as correctOutput:
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue='_'):
                self.assertTrue(myLine == correctLine, msg=("\nInput: " + time + "\nExpected Line: " + correctLine + "\nFound Line: " + myLine))

        test.terminate()

    @weight(17)
    def test_Release02(self):
        """Release 2"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./release02.in', 'r')
        time = input.readline()
        input.close()

        input = open('./release02.in', 'r')
        output = open('./myRelease02.output','w')

        test = subprocess.Popen(["./a.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myRelease02.output', 'r') as myOutput, open('./release02.output', 'r') as correctOutput:
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue='_'):
                self.assertTrue(myLine == correctLine, msg=("\nInput: " + time + "\nExpected Line: " + correctLine + "\nFound Line: " + myLine))

        test.terminate()