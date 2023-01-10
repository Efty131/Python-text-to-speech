import pyttsx3
pyobj = pyttsx3.init()
voices = pyobj.getProperty('voices') # voices from the local machine
pyobj.setProperty("rate", 150)
pyobj.setProperty('voice', voices[1].id)
pyobj.say("The quick brown fox jumps over the lazy dog. The rain in Spain falls mainly on the plain. Jackdaws love my big sphinx of quartz. How vexingly quick daft zebras jump!")
pyobj.runAndWait()