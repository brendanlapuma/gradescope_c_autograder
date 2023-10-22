from gradescope_utils.autograder_utils.decorators import weight
import unittest
import subprocess
import itertools
import random
import pickle

class TestDiff(unittest.TestCase):
    def setUp(self):
        pass 

    @weight(5)
    def test_sanity(self):
        """Sanity Check"""

        # Testing existence of exercise 1
        try:
            test = subprocess.Popen(["./exercise1.out"])
            test.kill()
            self.assertTrue(True)
        except:
            self.fail(msg = 'file exercise1.c either doesn\'t exist, or doesn\'t compile\n\nCheck your submitted file\'s name, and make sure the code compiles on grace.')

        # Testing existence of exercise 2
        try:
            test = subprocess.Popen(["./exercise2.out"])
            test.kill()
            self.assertTrue(True)
        except:
            self.fail(msg = 'file exercise2.c either doesn\'t exist, or doesn\'t compile\n\nCheck your submitted file\'s name, and make sure the code compiles on grace.')

        # Testing existence of exercise 3
        try:
            test = subprocess.Popen(["./exercise3.out"])
            test.kill()
            self.assertTrue(True)
        except:
            self.fail(msg = 'file exercise3.c either doesn\'t exist, or doesn\'t compile\n\nCheck your submitted file\'s name, and make sure the code compiles on grace.')

        # Testing existence of exercise 4
        try:
            test = subprocess.Popen(["./exercise4.out"])
            test.kill()
            self.assertTrue(True)
        except:
            self.fail(msg = 'file exercise4.c either doesn\'t exist, or doesn\'t compile\n\nCheck your submitted file\'s name, and make sure the code compiles on grace.')

        test.terminate()

    @weight(7)
    def test_Public_1(self):
        """Exercise One - Public 1"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public10.in', 'r')
        nums = input.readlines()
        sol = ''
        for num in nums:
            sol += num
        input.close()

        input = open('./public10.in', 'r')
        output = open('./myPublic10.output','w')

        test = subprocess.Popen(["./exercise1.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()
        output.close()
        input.close()

        correctOutput = open('./public10.output','w')
        input = open('./public10.in', 'r')
        test2 = subprocess.Popen(['./sol3-1.out'], stdin = input, stdout = correctOutput, stderr = subprocess.PIPE)
        test2.wait()
        correctOutput.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic10.output', 'r') as myOutput, open('./public10.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(15)
    def test_Public_2(self):
        """Exercise One - Public 2 (randomized inputs)"""
        inputs = [[random.randint(0,100000) for i in range(0,10)] for j in range(0,50)]

        # counter for tests
        x = 1
        for n in inputs:
            input = open('./public11.in','w')
            sol = ''
            for num in n: 
                input.write(f'{str(num)}\n')
                sol += str(num) + '\n'
            input.close()

            # opening i/o for solution
            input = open('./public11.in','r')
            output = open('./public11.output','w')
            test = subprocess.Popen(["./sol3-1.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
            test.wait()
            input.close()
            output.close()
            
            # opening i/o for student's results
            input = open('./public11.in','r')
            myOutput = open('./myPublic11.output','w')
            test = subprocess.Popen(["./exercise1.out"], stdin = input, stdout = myOutput, stderr=subprocess.PIPE)
            test.wait()
            input.close()
            myOutput.close()

            # tests output line-by-line, tells student exactly what the difference is on that line
            with open('./myPublic11.output', 'r') as myOutput, open('./public11.output', 'r') as correctOutput:
                mine = ''
                correct = ''
                for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                    mine += myLine
                    correct += correctLine
            
                self.assertTrue(mine.strip() == correct.strip(), msg=("\n\nFailed on test " + str(x) + " of " + str(len(inputs)) + " random inputs\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
            x += 1
        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(7)
    def test_Public_3(self):
        """Exercise Two - Public 1"""

        n = ['X','O','O','X','X','X','O','O','X']

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public20.in', 'w')
        sol = ''
        for num in n: 
            input.write(f'{str(num)}\n')
            sol += num + '\n'
        input.close()

        input = open('./public20.in', 'r')
        output = open('./myPublic20.output','w')

        test = subprocess.Popen(["./exercise2.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()
        output.close()
        input.close()

        correctOutput = open('./public20.output','w')
        input = open('./public20.in', 'r')
        test2 = subprocess.Popen(['./sol3-2.out'], stdin = input, stdout = correctOutput, stderr = subprocess.PIPE)
        test2.wait()
        correctOutput.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic20.output', 'r') as myOutput, open('./public20.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(15)
    def test_Public_4(self):
        """Exercise Two - Public 2 (randomized inputs)"""
        d = {
            0:'X',
            1:'O'
        }

        inputs = [[d[random.randint(0,1)] for i in range(0,9)] for j in range(0,50)]

        # counter for tests
        x = 1
        for n in inputs:
            input = open('./public21.in','w')
            sol = ''
            for num in n: 
                input.write(f'{str(num)}\n')
                sol += num + '\n'
            input.close()

            # opening i/o for solution
            input = open('./public21.in','r')
            output = open('./public21.output','w')
            test = subprocess.Popen(["./sol3-2.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
            test.wait()
            input.close()
            output.close()
            
            # opening i/o for student's results
            input = open('./public21.in','r')
            myOutput = open('./myPublic21.output','w')
            test = subprocess.Popen(["./exercise2.out"], stdin = input, stdout = myOutput, stderr=subprocess.PIPE)
            test.wait()
            input.close()
            myOutput.close()

            # tests output line-by-line, tells student exactly what the difference is on that line
            with open('./myPublic21.output', 'r') as myOutput, open('./public21.output', 'r') as correctOutput:
                mine = ''
                correct = ''
                for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                    mine += myLine
                    correct += correctLine
            
                self.assertTrue(mine.strip() == correct.strip(), msg=("\n\nFailed on test " + str(x) + " of " + str(len(inputs)) + " random inputs\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
            x += 1
        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(7)
    def test_Public_5(self):
        """Exercise Three - Public 1"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public30.in', 'r')
        nums = input.readlines()
        sol = ''
        for num in nums:
            sol += num
        input.close()

        input = open('./public30.in', 'r')
        output = open('./myPublic30.output','w')

        test = subprocess.Popen(["./exercise3.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()
        output.close()
        input.close()

        correctOutput = open('./public30.output','w')
        input = open('./public30.in', 'r')
        test2 = subprocess.Popen(['./sol3-3.out'], stdin = input, stdout = correctOutput, stderr = subprocess.PIPE)
        test2.wait()
        correctOutput.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic30.output', 'r') as myOutput, open('./public30.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(15)
    def test_Public_6(self):
        """Exercise Three - Public 2 (randomized inputs)"""
        inputs = [[random.randint(0,1000) for i in range(0,10)] for j in range(0,10)]

        # counter for tests
        x = 1
        for n in inputs:
            input = open('./public31.in','w')
            sol = ''
            for num in n: 
                input.write(f'{str(num)}\n')
                sol += str(num) + '\n'
            input.close()

            # opening i/o for solution
            input = open('./public31.in','r')
            output = open('./public31.output','w')
            test = subprocess.Popen(["./sol3-3.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
            test.wait()
            input.close()
            output.close()
            
            # opening i/o for student's results
            input = open('./public31.in','r')
            myOutput = open('./myPublic31.output','w')
            test = subprocess.Popen(["./exercise3.out"], stdin = input, stdout = myOutput, stderr=subprocess.PIPE)
            test.wait()
            input.close()
            myOutput.close()

            # tests output line-by-line, tells student exactly what the difference is on that line
            with open('./myPublic31.output', 'r') as myOutput, open('./public31.output', 'r') as correctOutput:
                mine = ''
                correct = ''
                for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                    mine += myLine
                    correct += correctLine
            
                self.assertTrue(mine.strip() == correct.strip(), msg=("\n\nFailed on test " + str(x) + " of " + str(len(inputs)) + " random inputs\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
            x += 1
        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(7)
    def test_Public_7(self):
        """Exercise Four - Public 1"""
        n = ['X','O','O','X','X','X','O','O','X']

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public40.in', 'w')
        sol = ''
        for num in n: 
            input.write(f'{str(num)}\n')
            sol += num + '\n'
        input.close()

        input = open('./public40.in', 'r')
        output = open('./myPublic40.output','w')

        test = subprocess.Popen(["./exercise4.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()
        output.close()
        input.close()

        correctOutput = open('./public40.output','w')
        input = open('./public40.in', 'r')
        test2 = subprocess.Popen(['./sol3-4.out'], stdin = input, stdout = correctOutput, stderr = subprocess.PIPE)
        test2.wait()
        correctOutput.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic40.output', 'r') as myOutput, open('./public40.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(7)
    def test_Public_8(self):
        """Exercise Four - Public 2"""

        n = ['X','O','X','X','O','X','O','X','O']

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public41.in', 'w')
        sol = ''
        for num in n: 
            input.write(f'{str(num)}\n')
            sol += num + '\n'
        input.close()

        input = open('./public41.in', 'r')
        output = open('./myPublic41.output','w')

        test = subprocess.Popen(["./exercise4.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()
        output.close()
        input.close()

        correctOutput = open('./public41.output','w')
        input = open('./public41.in', 'r')
        test2 = subprocess.Popen(['./sol3-4.out'], stdin = input, stdout = correctOutput, stderr = subprocess.PIPE)
        test2.wait()
        correctOutput.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic41.output', 'r') as myOutput, open('./public41.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput:\n" + sol + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(15)
    def test_Public_9(self):
        """Exercise Four - Public 3 (randomized inputs)"""

        vb = open('validboards','rb')
        vboards = pickle.load(vb)
        vb.close()

        # counter for tests
        x = 1
        for i in range(0,50):
            input = open('./public42.in','w')
            board = vboards[random.randint(0, len(vboards) - 1)]

            input.write(board)
            input.close()

            # opening i/o for solution
            input = open('./public42.in','r')
            output = open('./public42.output','w')
            test = subprocess.Popen(["./sol3-4.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
            test.wait()
            input.close()
            output.close()
            
            # opening i/o for student's results
            input = open('./public42.in','r')
            myOutput = open('./myPublic42.output','w')
            test = subprocess.Popen(["./exercise4.out"], stdin = input, stdout = myOutput, stderr=subprocess.PIPE)
            test.wait()
            input.close()
            myOutput.close()

            # tests output line-by-line, tells student exactly what the difference is on that line
            with open('./myPublic42.output', 'r') as myOutput, open('./public42.output', 'r') as correctOutput:
                mine = ''
                correct = ''
                for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                    mine += myLine
                    correct += correctLine
            
                self.assertTrue(mine.strip() == correct.strip(), msg=("\n\nFailed on test " + str(x) + " of 50 random inputs\nInput:\n" + board + "\n\nExpected: \n" + correct.strip() + "\n\nFound: \n" + mine.strip()))
            x += 1
        myOutput.close()
        correctOutput.close()
        test.terminate()