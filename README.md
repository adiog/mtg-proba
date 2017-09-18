# opening_hand_probability

Implementation of function returning the probability of getting an opening hand:
```
def compute(hand, deck, constraints)
```

# constraints examples
e.g. in bridge the probability of having:
* at least 3 aces and and least 5 lower cards in given colour can be calculated as follows:
```
compute(13, 52, '3+/4 5+/12')
```
* at least 3 and at most 8 hearts:
```
compute(13, 52, '3-8/13')
```
