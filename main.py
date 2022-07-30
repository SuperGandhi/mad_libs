"""
    Practice concat strings
    Suppose we want to create a string that says:
    Learn to program with _______.
"""

# space_blank = 'Python'
# print('Learn to program with' + '' + space_blank)
# print('Learn to program with {}'.format(space_blank))
# print(f'Learn to program with {space_blank}')

adj = input('Enter an adjetive: ')
verb_one  = input('Enter a verb: ')
verb_two = input('Enter another verb: ')
sust_plural = input('Enter a sustantive in plural: ')

mad_lib = f'!Programming is {adj}¡ Always excites me because I love it {verb_one} problems. ! Learn to {verb_two} with Python and reach you {sust_plural}'
print(mad_lib)
