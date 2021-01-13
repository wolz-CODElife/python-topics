"""
Programmed by Idunnuoluwa, 1:57 pm WAT 13/1/2021.
Function to check whether a string can be gotten from another,
if the letters are in a random order.
Aids in the production of word unscrambling algorithms
"""



def isin(lily, ylil): # checks if arg1 can be taken letter by letter from arg2
    a = list(lily) # turns arg 1 to a transversable object
    b = list(ylil) # turns arg 2 to a transversable object
    for i in a:
        if i not in ylil: # first condition to confirm whether they have
                          # the same letters
            return False
    for i in a:
        if a.count(i) > b.count(i): # second condition to confirm whether
                                    # duplicates are allowed in arg 2
                                    # and checks the number of duplicates allowed
            return False
    return True
