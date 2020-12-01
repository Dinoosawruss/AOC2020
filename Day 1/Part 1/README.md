# Problem Summary
Find 2 numbers in a data set that sum to make 2020

## My approach

### eliminateImpossibles.py
I first started by eliminating all the numbers that even when summed with the greatest number in the group still made a number < 2020.

### findKey.py
I then simply looped through even item *and then again through every item* summing them all with each other until it found a value that summed to 2020.
Once this had been found I simply multiplied them together and outputted the value given.

## Conclusion
I dont think this is the best solution however it was the one I thought of first so I went with it. The code runs extremely fast even with the size of the data set 
