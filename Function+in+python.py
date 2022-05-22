
# coding: utf-8

# In[ ]:

### Writting fonction 


# In[ ]:

# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Replace print with return
    return(shout_word)

# Pass 'congratulations' to shout: yell
yell = shout('congratulations')

# Print yell
print(yell)


# In[ ]:

# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations', 'you')

# Print yell
print(yell)


# In[ ]:

# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    """Return a tuple of strings"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')

# Print yell1 and yell2
print(yell1)
print(yell2)


# In[ ]:

# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv('tweets.csv')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)


# In[ ]:

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)


# In[ ]:

# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league"
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)


# In[ ]:

### How to Create a Simple Function in Python


# In[1]:

print("Hello! Hope you're doing well")


# In[8]:

def my_func():
  print("Hello! Hope you're doing well")
my_func()


# In[10]:

def my_func(name,place):
  print(f"Hello {name}! Are you from {place}?")
my_func("Diallo","Guinea")


# In[11]:

my_func(place = "United States of America", name = "Abdoulaye Diallo")


# In[22]:

def total_calc(bill_amount,tip_perc=10):
  total = bill_amount*(1 + 0.01*tip_perc)
  total = round(total,2)
  print(f"Please pay ${total}")


# In[25]:

total_calc(150)


# In[29]:

# specify both bill_amount and a custom tip percentage
 # the tip percentage specified in the function call is used
 
total_calc(200,15)


# In[30]:

total_calc(167,7.5)


# In[ ]:

### Return


# In[31]:

def volume_of_cuboid(length,breadth,height):
  return length*breadth*height


# In[32]:

volume = volume_of_cuboid(5.5,20,6)
print(f"Volume of the cuboid is {volume} cubic units")


# In[ ]:

### Return multiple value


# In[42]:

def cube(side):
  volume = side **3
  surface_area = 6 * (side**2) 
    
  return volume, surface_area


# In[43]:

returned_values = cube(8)
print(returned_values)


# In[44]:

volume, area = cube(6.5)
print(f"Volume of the cube is {volume} cubic units and the total surface area is {area} sq. units")


# In[ ]:

### How to Create a Function that Takes a Variable Number of Arguments in Python


# In[45]:

def my_var_sum(*args):
  sum = 0
  for arg in args:
    sum += arg
  return sum


# In[46]:

# Example 1 with 4 numbers
sum = my_var_sum(99,10,54,23)
print(f"The numbers that you have add up to {sum}")


# In[47]:

# Example 2 with 3 numbers
sum = my_var_sum(9,87,45)
print(f"The numbers that you have add up to {sum}")


# In[48]:

# Example 3 with 6 numbers
sum = my_var_sum(5,21,36,79,45,65)
print(f"The numbers that you have add up to {sum}")


# In[ ]:

# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))


# In[ ]:

# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))


# In[ ]:

# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    
    # Concatenate word with itself: echo_word
    echo_word = word * 2
    
    # Print echo_word
    print(echo_word)
    
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""
        
        # Use echo_word in nonlocal scope
        nonlocal echo_word
        
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'
    
    # Call function shout()
    shout()
    
    # Print echo_word
    print(echo_word)

# Call function echo_shout() with argument 'hello'
echo_shout('hello')

