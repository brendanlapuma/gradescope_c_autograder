# C Differential Output Auto-Grader (Template)

Uses multiprocessing in python and differential output checking to automatically grade C programs through gradescope

1. Zip all files (except 'Code' folder) and upload to GradeScope as the auto grader file

2. Done!

## Making Custom Tests

- Edit the test_subprocesses.py file as necessary
- If you want custom executable file names, edit the compile command in run_autograder by adding the flag -o \<filename> (make sure to change the executable file name in the unit tests as well)
- See Gradescope documentation for assigning weights and providing output to students
