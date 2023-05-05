import pyttsx3 
import datetime
import requests
import speech_recognition as sr
import wikipedia
import webbrowser
from bs4 import BeautifulSoup
import os
import smtplib
import json
import pywhatkit as kit
import threading

#voice selection for jarvis
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#voices is a list of voices on your computer
engine.setProperty('voice',voices[0].id)


#speak function will take string input and speak
def speak(audio):
	engine.say(audio)
	engine.runAndWait()


#wishMe() function will greet you whenever you run this script
def wishMe():
	hour = int(datetime.datetime.now().hour)
	
	if hour>=0 and hour<12:
		speak("good morning bro")

	elif hour>=12 and hour<18:
		speak("good afternoon bro")
	
	else:
		speak("Good Evening bro")

	speak("I am GAMMA bro ,Tell me how can I help you?")


#jarvis will take your voice command and convert into string
def takeCommand():
	#it takes microphone input from user and returns string output
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		
	try:
		print("Recognizing...")
		query = r.recognize_google(audio,language='en-in')
		print(f"User said; {query}\n")

	except Exception as e:
		print(e)
		print("Say That Again Please...")
		return "None"

	return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password-here')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    if 1:
        query=takeCommand().lower()
        
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'The time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Bro,the time is{strTime}")    
            
        elif 'open code' in query:
            codepath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
        elif 'open folder' in query:
            folder_path="C:\\Users\\DELL\\registration sample\\Django_Login_System.exe"
            os.startfile(folder_path)
            
        elif 'email to Priyank' in query:
            try:
                speak("what should I say?")
                content=takeCommand()
                to="yourEmail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry.I am not able to send this email")
                
        elif " send message" in query:
            def send_message():
             kit.sendwhatmsg("+9324616552", "this is testing protocol",2,25)
             t=threading.Thread(target=send_message)
             t.start()   
        elif "temperature" in query:
            try:
               search = "temperature in Mumbai"
               url = f"https://www.google.com/search?q={search}"
               r = requests.get(url)
               print(r.text)
               data = BeautifulSoup(r.text, "html.parser")
               temp = data.find("div",class_="BNeawe iB vvp4i AP7wnd").text
               speak(f"current {search} is {temp}")
            except:
               speak("Sorry, I couldn't get the temperature. Please try again later.")
            
'''base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "cec1642367771d9c80a77229e2871bf2"
url= "http://api.openweathermap.org/data/2.5/weather?"'''

'''city_name = input("Enter city name : ") 
full_url = base_url + "q=" + city_name + "&appid=" + api_key
req = requests.get(full_url)
info = req.json() 

if info["cod"] != "404":
  try: 
    x = info["main"] 
    current_temperature = x["temp"]
    tnc = round(float(current_temperature - 273.15),2)
    current_pressure = x["pressure"] 
    current_humidiy = x["humidity"] 
    z = info["weather"] 
    weather_description = z[0]["description"]
    s = info["wind"]
    speed = s["speed"]
    print()
    print("Temperature (in celsius unit): ", 
                  round(float(current_temperature - 273.15),2) , "°C",
            "\nAtmospheric pressure : " +
                  str(current_pressure) + "hpa"
            "\nHumidity : " +
                  str(current_humidiy) + "%"
            "\nDescription: " +
                  str(weather_description).capitalize()+
                "\nWind Speed :" + str(speed) + "m/s")
  except KeyError as e:
      print(f"Error: {e} key not found in API response.")
else: 
  print(" City Not Found ")'''