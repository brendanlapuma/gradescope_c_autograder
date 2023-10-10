from gradescope_utils.autograder_utils.decorators import weight
import unittest
import subprocess
import itertools
import random

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
        test.terminate()

        # Testing existence of exercise 3
        try:
            test = subprocess.Popen(["./exercise3.out"])
            test.kill()
            self.assertTrue(True)
        except:
            self.fail(msg = 'file exercise3.c either doesn\'t exist, or doesn\'t compile\n\nCheck your submitted file\'s name, and make sure the code compiles on grace.')

        test.terminate()

    @weight(5)
    def test_Public_1(self):
        """Exercise One - Public 1"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public00.in', 'r')
        num = input.readline()
        input.close()

        input = open('./public00.in', 'r')
        output = open('./myPublic00.output','w')

        test = subprocess.Popen(["./exercise1.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic00.output', 'r') as myOutput, open('./public00.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput: " + num + "\n\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(5)
    def test_Public_2(self):
        """Exercise One - Public 2"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public01.in', 'r')
        num = input.readline()
        input.close()

        input = open('./public01.in', 'r')
        output = open('./myPublic01.output','w')

        test = subprocess.Popen(["./exercise1.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic01.output', 'r') as myOutput, open('./public01.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput: " + num + "\n\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(5)
    def test_Public_3(self):
        """Exercise One - Public 3"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public02.in', 'r')
        num = input.readline()
        input.close()

        input = open('./public02.in', 'r')
        output = open('./myPublic02.output','w')

        test = subprocess.Popen(["./exercise1.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic02.output', 'r') as myOutput, open('./public02.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput: " + num + "\n\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(13)
    def test_Public_4(self):
        """Exercise One - Public 4 (randomized inputs)"""
        inputs = [random.randint(1,100) for i in range(0,50)]

        # counter for tests
        x = 1
        for n in inputs:
            num = str(n)
            input = open('./public03.in','w')
            input.write(f'{num}\n')
            input.close()

            output = open('./public03.output','w')

            output.write('Please enter an integer: ')

            # writing correct output to file
            for i in range(0,n + 1):
                for j in range(0,i):
                    output.write('*')
                output.write('\n')

            output.close()


            # opening i/o for student's results
            input = open('./public03.in','r')
            myOutput = open('./myPublic03.output','w')
            test = subprocess.Popen(["./exercise1.out"], stdin = input, stdout = myOutput, stderr=subprocess.PIPE)
            test.wait()
            input.close()
            myOutput.close()

            # tests output line-by-line, tells student exactly what the difference is on that line
            with open('./myPublic03.output', 'r') as myOutput, open('./public03.output', 'r') as correctOutput:
                mine = ''
                correct = ''
                for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                    mine += myLine
                    correct += correctLine
            
                self.assertTrue(mine.strip() == correct.strip(), msg=("\n\nFailed on test " + str(x) + " of " + str(len(inputs)) + " random inputs\nInput: " + num + "\n\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))
            x += 1
        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(5)
    def test_Public_5(self):
        """Exercise Two - Public 1"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public20.in', 'r')
        num = input.readline()
        input.close()

        input = open('./public20.in', 'r')
        output = open('./myPublic20.output','w')

        test = subprocess.Popen(["./exercise2.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic20.output', 'r') as myOutput, open('./public20.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput: " + num + "\n\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))
        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(5)
    def test_Public_6(self):
        """Exercise Two - Public 2"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public21.in', 'r')
        num = input.readline()
        input.close()

        input = open('./public21.in', 'r')
        output = open('./myPublic21.output','w')

        test = subprocess.Popen(["./exercise2.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic21.output', 'r') as myOutput, open('./public21.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput: " + num + "\n\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))

        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(5)
    def test_Public_7(self):
        """Exercise Two - Public 3"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public22.in', 'r')
        num = input.readline()
        input.close()

        input = open('./public22.in', 'r')
        output = open('./myPublic22.output','w')

        test = subprocess.Popen(["./exercise2.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic22.output', 'r') as myOutput, open('./public22.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput: " + num + "\n\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))

        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(13)
    def test_Public_8(self):
        """Exercise Two - Public 4 (randomized inputs)"""
        inputs = [random.randint(1,100) for i in range(0,50)]

        # counter for tests
        x = 1
        for n in inputs:
            num = str(n)
            input = open('./public23.in','w')
            input.write(f'{num}\n')
            input.close()

            # writing correct output to file
            output = open('./public23.output','w')

            output.write('Please enter an integer: ')
            output.write('\n')

            for i in range(0,n):
                output.write('*')

            output.write('\n')

            for i in range(1,n - 1):
                output.write('*')
                for j in range(1,n - 1):
                    output.write(' ')
                output.write('*\n')

            if n != 1:
                for i in range(0,n):
                    output.write('*')

            output.close()

            # opening i/o for student's results
            input = open('./public23.in','r')
            myOutput = open('./myPublic23.output','w')
            test = subprocess.Popen(["./exercise2.out"], stdin = input, stdout = myOutput, stderr=subprocess.PIPE)
            test.wait()
            input.close()
            myOutput.close()

            # tests output line-by-line, tells student exactly what the difference is on that line
            with open('./myPublic23.output', 'r') as myOutput, open('./public23.output', 'r') as correctOutput:
                mine = ''
                correct = ''
                for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                    mine += myLine
                    correct += correctLine
            
                self.assertTrue(mine.strip() == correct.strip(), msg=("\n\nFailed on test " + str(x) + " of " + str(len(inputs)) + " random inputs\nInput: " + num + "\n\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))
            x += 1
        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(5)
    def test_Public_9(self):
        """Exercise Three - Public 1"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public30.in', 'r')
        num = input.readline()
        input.close()

        input = open('./public30.in', 'r')
        output = open('./myPublic30.output','w')

        test = subprocess.Popen(["./exercise3.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic30.output', 'r') as myOutput, open('./public30.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput: " + num + "\n\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))

        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(5)
    def test_Public_10(self):
        """Exercise Three - Public 2"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public31.in', 'r')
        num = input.readline()
        input.close()

        input = open('./public31.in', 'r')
        output = open('./myPublic31.output','w')

        test = subprocess.Popen(["./exercise3.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic31.output', 'r') as myOutput, open('./public31.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput: " + num + "\n\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))

        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(5)
    def test_Public_11(self):
        """Exercise Three - Public 3"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public32.in', 'r')
        num = input.readline()
        input.close()

        input = open('./public32.in', 'r')
        output = open('./myPublic32.output','w')

        test = subprocess.Popen(["./exercise3.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic32.output', 'r') as myOutput, open('./public32.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput: " + num + "\n\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))

        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(5)
    def test_Public_12(self):
        """Exercise Three - Public 4"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public33.in', 'r')
        num = input.readline()
        input.close()

        input = open('./public33.in', 'r')
        output = open('./myPublic33.output','w')

        test = subprocess.Popen(["./exercise3.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic33.output', 'r') as myOutput, open('./public33.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput: " + num + "\n\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))

        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(5)
    def test_Public_13(self):
        """Exercise Three - Public 5"""

        # Create a subprocess to run the students code to obtain an output 
        input = open('./public34.in', 'r')
        num = input.readline()
        input.close()

        input = open('./public34.in', 'r')
        output = open('./myPublic34.output','w')

        test = subprocess.Popen(["./exercise3.out"], stdin = input, stdout = output, stderr=subprocess.PIPE)
        test.wait()

        output.close()
        input.close()

        # tests output line-by-line, tells student exactly what the difference is on that line
        with open('./myPublic34.output', 'r') as myOutput, open('./public34.output', 'r') as correctOutput:
            mine = ''
            correct = ''
            for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                mine += myLine
                correct += correctLine
            
            self.assertTrue(mine.strip() == correct.strip(), msg=("\nInput: " + num + "\n\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))

        myOutput.close()
        correctOutput.close()
        test.terminate()

    @weight(14)
    def test_Public_14(self):
        """Exercise Three - Public 6 (randomized inputs)"""
        inputs = [random.randint(-5,100) for i in range(0,50)]

        # counter for tests
        x = 1
        for n in inputs:
            num = str(n)
            input = open('./public35.in','w')
            input.write(f'{num}\n')
            input.close()

            # writing correct output to file
            output = open('./public35.output','w')

            output.write('Please enter an integer: ')
            output.write('\n')

            if n < 1:
                output.write('Invalid entry.')
            elif n == 1:
                output.write('This number is not prime.')
            else:
                flag = False
                for i in range(2,(n // 2) + 1):
                    if n % i == 0:
                        flag = True
                        break
                if not flag:
                    output.write('This is prime.')
                else:
                    output.write('This number is not prime.')

            output.close()

            # opening i/o for student's results
            input = open('./public35.in','r')
            myOutput = open('./myPublic35.output','w')
            test = subprocess.Popen(["./exercise3.out"], stdin = input, stdout = myOutput, stderr=subprocess.PIPE)
            test.wait()
            input.close()
            myOutput.close()

            # tests output line-by-line, tells student exactly what the difference is on that line
            with open('./myPublic35.output', 'r') as myOutput, open('./public35.output', 'r') as correctOutput:
                mine = ''
                correct = ''
                for myLine, correctLine in itertools.zip_longest(myOutput, correctOutput, fillvalue=' '):
                    mine += myLine
                    correct += correctLine
            
                self.assertTrue(mine.strip() == correct.strip(), msg=("\n\nFailed on test " + str(x) + " of " + str(len(inputs)) + " random inputs\nInput: " + num + "\n\nExpected: \n" + correct.strip() + "\nFound: \n" + mine.strip()))
            x += 1
        myOutput.close()
        correctOutput.close()
        test.terminate()