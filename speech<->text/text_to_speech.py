# Import the required module for text to speech conversion 
from gtts import gTTS 

# This module is imported so that we can play the converted audio 
import os 

# User choice as input
print('Enter your choice : \n 1. Manual input \n 2. file as input \n 3. exit from the program')
choice = int(input())

if choice == 1 :

    # Taking input manually
    mytext = input()
    print(mytext)
    
    # Language in which you want to convert 
    language = 'en'

    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed 
    myobj = gTTS(text=mytext, lang=language, slow=False) 

    # Saving the converted audio in a mp3 file named welcome 
    myobj.save("welcome.mp3") 

    # Playing the converted file 
    os.system("welcome.mp3") 


elif choice == 2:    
    # Taking input from file
    input_lines = []
    with open('input.txt', 'r') as file:
            input_lines = [line.strip() for line in file]

    # The text that you want to convert to audio 
    mytext = ' '.join(input_lines)
    print(mytext)

    myobj = gTTS(text=mytext, lang='en', slow=False) 
    myobj.save("welcome.mp3") 
    os.system("welcome.mp3") 

elif choice == 3:
    exit()