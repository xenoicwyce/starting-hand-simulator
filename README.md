# Starting hand simulator
A starting hand simulator. Mainly used for deck-building in TCGs.

## How to use
Put card images (`.png` or `.jpg`) in a folder that represents the deck. Duplicate the images for each copy in the deck. Then, run
``` 
python main.py path/to/deck/ num_draw num_rounds
```
`num_draw`: Number of draws each round.\
`num_rounds`: Number of rounds to simulate.

The deck can also be represented as text files with the format:
```
card_name1, number_of_copies
card_name2, number_of_copies
card_name3, number_of_copies
...
```
In this case, run
```
python main.py --use-dat path/to/file.dat num_draw num_rounds
```
