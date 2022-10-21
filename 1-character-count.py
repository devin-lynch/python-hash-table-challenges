'''
1. Character Count:
given a string count each letter in the string and then print the result.

Example 1:

character_count('banana')

Input: 'banana'
Output (in the console): 
the character b occurs 1 times
the character a occurs 3 times
the character n occurs 2 times

Example 2:

character_count('hello world')

Input: 'hello world'
Output (in the console): 
the character h occurs 1 times
the character e occurs 1 times
the character l occurs 3 times
the character o occurs 2 times
the character   occurs 1 times
the character w occurs 1 times
the character r occurs 1 times
the character d occurs 1 times
'''

def character_count(string):
  # use a dictionary as a has table to store uniqu values
  hash_table = {}
  # loop over the numbers, check if they are in the hash table
  for char in string:
      # if a char is in the hash table -- return True
      if char in hash_table:
          hash_table[char] += 1
          print(hash_table)
      # if a number isn't in the hash table -- add it to the hash table
      else:
          hash_table[char] = 1
          
  # for char in hash_table: # this way also works
  #    print(f'the character {char} occurs {hash_table[char]} times')

  for x, y in hash_table.items():
    print(f'the character {x} occurs {y} times')

# character_count('banana')


# ## # ## # ## # ## #
# CLASS REVIEW EXAMPLE

def character_count(string):
  # hash table to store strings and count their occurances
  table = {}
  for letter in string:
    # if the letter is in our table, we can increment its value
    if letter in table:
      table[letter] += 1
    # if the letter is not in our table, we can add it with a value of 2
    else:
      table[letter] = 1

  print(table)

  # loop over our table and print out the count for each letter
  for letter in table:
    print(f'the character {letter} occurs {table[letter]}')

# character_count('hello world')