# Starting hand simulator
A starting hand simulator. Mainly used for deck-building in TCGs.

## How to use
Put card images (`.png` or `.jpg`) in a folder that represents the deck. Duplicate the images for each copy in the deck. Then, run
``` 
python main.py path/to/deck/
```
The deck can also be represented as text files with the format:
```
card_name1, number_of_copies
card_name2, number_of_copies
card_name3, number_of_copies
...
```
