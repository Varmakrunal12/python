# module,comments & pip

print("hello world")


# import pyjokes

# joke = pyjokes.get_joke()
# print(joke)

# problem set

# # 1.multi line comment
# print("""
# Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
# like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
# When the blazing sun is set, and the grass with dew is wet. Then you show your little
# light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
# are.
# Then the traveler in the dark thanks you for your tiny spark. How could he see where to
# go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
# As your bright and tiny spark lights the traveler in the dark, though I know not what you
# are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are""")

# # 2.write and speak
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello,my name is krunal.i am 18 year old")
# engine.runAndWait()

# problem 3

import os

# Select the directory whose content you want to list 
directory_path = '/'

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the contents of the directory 
print(contents)
    