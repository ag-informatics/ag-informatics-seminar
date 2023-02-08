## Code Source: https://greenteapress.com/thinkpython2/html/thinkpython2010.html
## Class Contributor: Megan

## For is_abecedarian we have to compare adjacent letters, which is a little tricky with a for loop:

def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

## An alternative is to use recursion:
def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])
Another option is to use a while loop:
def is_abecedarian(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i+1
    return True
