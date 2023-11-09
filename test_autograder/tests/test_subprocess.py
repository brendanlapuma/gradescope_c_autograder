from gradescope_utils.autograder_utils.decorators import weight
import unittest
import subprocess
import itertools
import random
import pickle

class TestDiff(unittest.TestCase):
    def setUp(self):
        self.coords = [[i,j] for i in range(1,4) for j in range(1,4)] 

    @weight(5)
    def test_sanity(self):
        """Sanity Check"""

        # Testing existence of exercise 1
        try:
            test = subprocess.Popen(["./hw4.out"])
            test.kill()
            self.assertTrue(True)
        except:
            self.fail(msg = 'file hw4.c either doesn\'t exist, or doesn\'t compile\n\nCheck your submitted file\'s name, and make sure the code compiles on grace.')

        test.terminate()
    
    # X col win
    @weight(5)
    def test_Public_1(self):
        """Public 1"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public1.in', 'r')
        nums = input.readlines()
        sol = ''
        for num in nums:
            sol += num
        input.close()

        input = open('./public1.in', 'r')
        output = open('./myPublic1.output','w')

        test = subprocess.Popen(["./hw4.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()
        output.close()
        input.close()

        correctOutput = open('./public1.output','w')
        input = open('./public1.in', 'r')
        test2 = subprocess.Popen(['./sol.out'], stdin = input, stdout = correctOutput, stderr = subprocess.PIPE)
        test2.wait()
        correctOutput.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic1.output', 'r') as myOutput, open('./public1.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    # O col win
    @weight(5)
    def test_Public_2(self):
        """Public 2"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public2.in', 'r')
        nums = input.readlines()
        sol = ''
        for num in nums:
            sol += num
        input.close()

        input = open('./public2.in', 'r')
        output = open('./myPublic2.output','w')

        test = subprocess.Popen(["./hw4.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()
        output.close()
        input.close()

        correctOutput = open('./public2.output','w')
        input = open('./public2.in', 'r')
        test2 = subprocess.Popen(['./sol.out'], stdin = input, stdout = correctOutput, stderr = subprocess.PIPE)
        test2.wait()
        correctOutput.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic2.output', 'r') as myOutput, open('./public2.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    # Draw
    @weight(5)
    def test_Public_3(self):
        """Public 3"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public3.in', 'r')
        nums = input.readlines()
        sol = ''
        for num in nums:
            sol += num
        input.close()

        input = open('./public3.in', 'r')
        output = open('./myPublic3.output','w')

        test = subprocess.Popen(["./hw4.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()
        output.close()
        input.close()

        correctOutput = open('./public3.output','w')
        input = open('./public3.in', 'r')
        test2 = subprocess.Popen(['./sol.out'], stdin = input, stdout = correctOutput, stderr = subprocess.PIPE)
        test2.wait()
        correctOutput.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic3.output', 'r') as myOutput, open('./public3.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    # Last move X diag win
    @weight(5)
    def test_Public_4(self):
        """Public 4"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public4.in', 'r')
        nums = input.readlines()
        sol = ''
        for num in nums:
            sol += num
        input.close()

        input = open('./public4.in', 'r')
        output = open('./myPublic4.output','w')

        test = subprocess.Popen(["./hw4.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()
        output.close()
        input.close()

        correctOutput = open('./public4.output','w')
        input = open('./public4.in', 'r')
        test2 = subprocess.Popen(['./sol.out'], stdin = input, stdout = correctOutput, stderr = subprocess.PIPE)
        test2.wait()
        correctOutput.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic4.output', 'r') as myOutput, open('./public4.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    # Immediate quit
    @weight(5)
    def test_Public_5(self):
        """Public 5"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public5.in', 'r')
        nums = input.readlines()
        sol = ''
        for num in nums:
            sol += num
        input.close()

        input = open('./public5.in', 'r')
        output = open('./myPublic5.output','w')

        test = subprocess.Popen(["./hw4.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()
        output.close()
        input.close()

        correctOutput = open('./public5.output','w')
        input = open('./public5.in', 'r')
        test2 = subprocess.Popen(['./sol.out'], stdin = input, stdout = correctOutput, stderr = subprocess.PIPE)
        test2.wait()
        correctOutput.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic5.output', 'r') as myOutput, open('./public5.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    # Moves then quit
    @weight(10)
    def test_Public_6(self):
        """Public 6"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public6.in', 'r')
        nums = input.readlines()
        sol = ''
        for num in nums:
            sol += num
        input.close()

        input = open('./public6.in', 'r')
        output = open('./myPublic6.output','w')

        test = subprocess.Popen(["./hw4.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()
        output.close()
        input.close()

        correctOutput = open('./public6.output','w')
        input = open('./public6.in', 'r')
        test2 = subprocess.Popen(['./sol.out'], stdin = input, stdout = correctOutput, stderr = subprocess.PIPE)
        test2.wait()
        correctOutput.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic6.output', 'r') as myOutput, open('./public6.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    # Invalid inputs, some valid moves, then quit
    @weight(10)
    def test_Public_7(self):
        """Public 7"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public7.in', 'r')
        nums = input.readlines()
        sol = ''
        for num in nums:
            sol += num
        input.close()

        input = open('./public7.in', 'r')
        output = open('./myPublic7.output','w')

        test = subprocess.Popen(["./hw4.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()
        output.close()
        input.close()

        correctOutput = open('./public7.output','w')
        input = open('./public7.in', 'r')
        test2 = subprocess.Popen(['./sol.out'], stdin = input, stdout = correctOutput, stderr = subprocess.PIPE)
        test2.wait()
        correctOutput.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic7.output', 'r') as myOutput, open('./public7.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    # Invalid inputs, valid moves, diagonal winner
    @weight(10)
    def test_Public_8(self):
        """Public 8"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public8.in', 'r')
        nums = input.readlines()
        sol = ''
        for num in nums:
            sol += num
        input.close()

        input = open('./public8.in', 'r')
        output = open('./myPublic8.output','w')

        test = subprocess.Popen(["./hw4.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()
        output.close()
        input.close()

        correctOutput = open('./public8.output','w')
        input = open('./public8.in', 'r')
        test2 = subprocess.Popen(['./sol.out'], stdin = input, stdout = correctOutput, stderr = subprocess.PIPE)
        test2.wait()
        correctOutput.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic8.output', 'r') as myOutput, open('./public8.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    # Bunch of randomized tests
    @weight(30)
    def test_Public_9(self):
        """Public 9 (randomized inputs)"""
        random.shuffle(self.coords)

        # counter for tests
        x = 1
        while x < 200:
            input = open('./public9.in','w')
            sol = ''
            for num in self.coords: 
                input.write(f'{str(num[0])},{str(num[1])}\n')
                sol += str(num[0]) + ',' + str(num[1]) + '\n'
            input.close()

            # opening i/o for solution
            input = open('./public9.in','r')
            output = open('./public9.output','w')
            test = subprocess.Popen(["./sol.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
            test.wait()
            input.close()
            output.close()
            
            # opening i/o for student's results
            input = open('./public9.in','r')
            myOutput = open('./myPublic9.output','w')
            test = subprocess.Popen(["./hw4.out"], stdin = input, stdout = myOutput, stderr=subprocess.PIPE)
            test.wait()
            input.close()
            myOutput.close()

            # tests output line-by-line, tells student exactly what the difference is on that line
            with open('./myPublic9.output', 'r') as myOutput, open('./public9.output', 'r') as correctOutput:
                mine = ''
                correct = ''
                for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                    mine += myLine
                    correct += correctLine
            
                self.assertTrue(mine.strip() == correct.strip(), msg=("\n\nFailed on test " + str(x) + " of 100") + " random inputs\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip())
            x += 1
            random.shuffle(self.coords)

        myOutput.close()
        correctOutput.close()
        test.terminate()
