# Advent of Code Day 4
*My approach for this day was heavily assisted by [m-sterling's solutions](https://github.com/m-sterling/Advent-of-Code-2020)*

### Part 1
Check how many passports in the file contain all the required information

#### My approach
I looped through each line checking first if it was empty, if it was not I'd add it to the dictionary passports. If it was a new line the program checked each key to ensure it was in the keys list for the passprots array. If it was, the passport was valid

### Part 2
Validate the passport data and give the number of valid passports

#### My approach
I used a similar approach to part one adding them to a dictionary then checking everything when a new line had been reached. I then simply checked each item to ensure it was valid

## Conclusion
Unfortunately I struggled with this one a lot so a lot of this code isn't mine. It taught me quite a bit about how to go about such a problem however.