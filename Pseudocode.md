## Exercise 27 - Pseudocode

Write a Pseudocode for the programs you created for the exercises 25, 24 and 23
* Exercise 23 – for your for loop that calculates the sum
* Exercise 24 – for your while loop that searches for a specific number
* Exercise 25 – for your loops that find the maximal value of a matrix

**Exercise 23 - Your first loops** [(`FirstLoop.py`)](https://github.com/rominafernandez/Python_Loops/blob/master/FirstLoop.py)\
sum = 0\
for range():\
&nbsp;&nbsp;&nbsp;&nbsp; add i to sum

**Exercise 24 - 3 while loops** [(`WhileLoops.py`)](https://github.com/rominafernandez/Python_Loops/blob/master/WhileLoops.py)\
while i < list:\
&nbsp;&nbsp;&nbsp;&nbsp; if list[i] = searched_number:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print found\
&nbsp;&nbsp;&nbsp;&nbsp; i+1

**Exercise 25 - Loop trough a matrix** [(`MatrixLoop.py`)](https://github.com/rominafernandez/Python_Loops/blob/master/MatrixLoop.py)\
max = 0\
for i in outer_matrix:\
&nbsp;&nbsp;&nbsp;&nbsp; for j in inner_matrix:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if matrix[i,j] > max:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; max = matrix[i,j]\
print max
