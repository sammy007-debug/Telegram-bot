from datetime import datetime

def sampleResponse(input_text):

    userMessage = str(input_text).lower()

    if userMessage in ("hello", "hi", "whatsup",):
        return "Hey man! How is it going?"

    if userMessage in ("who are you", "who are ?",):
        return "I am your bot! hahaha "

    if userMessage in ("time", "time?","what is the time?"):
        now = datetime.now()
        dateTime = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(dateTime)


    return "I don't understand you man. Why are you so complicated"

