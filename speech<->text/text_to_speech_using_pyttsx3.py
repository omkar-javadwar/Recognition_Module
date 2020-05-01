# Import the required module for text to speech conversion 
import pyttsx3 
  
# init function to get an engine instance for the speech synthesis  
engine = pyttsx3.init() 
  
# Taking input from user.
str = input()
print(str)

# say method on the engine that passing input text to be spoken 
engine.say(str) 
  
# run and wait method, it processes the voice commands.  
engine.runAndWait() 
