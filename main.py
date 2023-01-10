import pyttsx3
pyobj = pyttsx3.init()
file = open("C:\\Users\efty1\\OneDrive\\Desktop\\sampleTxt.txt") # sample file from local machine
i = file.read()
file.close()
voices = pyobj.getProperty('voices') # voices from the local machine
pyobj.setProperty("rate", 150)
pyobj.setProperty('voice', voices[1].id)
pyobj.say(i) # or we can write the text here like "Hello World!" 
pyobj.save_to_file(i,"C:\\Users\\efty1\\OneDrive\\Desktop\\sampleTxt.mp3")
pyobj.runAndWait()