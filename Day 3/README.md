# Advent of Code Day 3
### Part 1
See how many #'s you'd hit on a map moving right 3, down 1 each time

#### My approach
I looped through each line in the inp getting the line based on the value for y. I then tested if the value of line[x % line(line)] was #

### Part 2
Do the same for a variety of movement pattern, the key is all the encounters multiplied together.

#### My approach
Use part1 code with different values for x += and y += iterating through a 2D array of each movement pattern

## Conclusion
Once again I dont think this is the best solution however it was the one I thought of first so I went with it. The code runs extremely fast even with the size of the data set 
