# Problem Summary
Find 3 numbers in a data set that sum to make 2020

## My approach
*My approach for part 2 was mostly the same as the approach to part 1*
### eliminateImpossibles.py
Similar to part 1 I first started by eliminating all the numbers that even when summed with the greatest number and 2nd greatest number in the group still made a number < 2020.
However, I decided it was probably best to eliminate numbers that would also be too nih. I did this by also testing if their sum against the first 2 number > 2020.

### findKey.py
I looped through each item, looping through each item within that loop, and again within that loop *I don't like this approach however I couldn't think of anything else* and tested if the sum of the 3 numbers was 2020.

## Conclusion
I dont think this is the best solution however it was the one I thought of first so I went with it. The code runs extremely fast even with the size of the data set 
