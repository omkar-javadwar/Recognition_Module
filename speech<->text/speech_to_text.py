# Python program to translate speech to text

# Importing Speech Recognition module
import speech_recognition as sr

# Initialize the recognizer  
r = sr.Recognizer()
   
# use the microphone as source for input. 
with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)
    print("Time Over, Thanks!")

# Exception handling to handle exceptions at the runtime
try:
    print("Text : "+ r.recognize_google(audio))

except sr.RequestError as e:
    print("Could not request results; {0}".format(e)) 

except sr.UnknownValueError: 
    print("unknown error occured")
