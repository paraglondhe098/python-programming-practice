import json
import requests
def speak(x):
    import win32com.client
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(x)
r=requests.get("http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-28&sortBy=publishedAt&apiKey=3298fb944ecf450e99d68e8856012831")
txt=r.text
y=json.loads(txt)
news=y["articles"]
for content in news:
    speak(content['title'])
    speak("next news is")
