# Advent of Code Day 2
### Part 1
Find the number of valid passwords in this database according to the password policy

Example <br>
1-3 a: abcde <br>
Must have at least 1 a and a max of 3 a's <br>
Therefore this is valid

#### My approach
Iterate through each line in the database, pulling out the min, max, letter, and password <br>
Simple check with password.count()

### Part 2
Under a different password policy, check how many are valid

Example <br>
1-3 a: abcde <br>
Must have EXACTLY one a at position 1 or 3 <br>
1-3 a: **a**b**c**de <br>
Only an a at position one therefore it is valid

#### My approach
Iterate through each line in the database, pulling out the min, max, letter, and password <br>
Simple XOR check

## Conclusion
Once again I dont think this is the best solution however it was the one I thought of first so I went with it. The code runs extremely fast even with the size of the data set 
