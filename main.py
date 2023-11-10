import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import requests
import subprocess


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("\nListening....")
        r.pause_threshold = 1  # Waiting time to take command
        audio = r.listen(source)
        try:
            print("Recognizing......")
            query = r.recognize_google(audio, language="en-in")
            # print(f"User said : {query}")
            return query

        except Exception as e:
            say("Some Error Occurred. Sorry Please try again!")
            return "None"


if __name__ == '__main__':
    say("Hello Welcome you to Desktop AI world, I am Alex. \n How can i help you?")
    while True:
        query = takecommand()

        if "time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")

        elif "weather".lower() in query.lower():
            api_key = "8bc227b7bd074643ae2203815232805"
            base_url = "http://api.weatherapi.com/v1"
            say("what is the city name")
            city_name = takecommand()
            complete_url = base_url + "/current.json?key=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            a = x.keys()
            a = list(a)
            if a[0] != "error":
                y = x["current"]
                current_temperature = y["temp_c"]
                current_humidiy = y["humidity"]
                z = x["current"]
                weather_description = z["condition"]["text"]
                say(" Temperature is " +
                      str(current_temperature) +"degree celcius" +
                      "\n humidity is " +
                      str(current_humidiy) +"percentage" +
                      "\n description  " +
                      str(weather_description))
            
            else:
                say("There is some error.\n Please check my code and api kay,\n try again?")
            
        elif "Close".lower() in query.lower():
            quit()
            
        elif "log off" in query.lower() or "sign out" in query.lower():
            say("Ok , your pc will log off, make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
            
        elif "shut down my pc" in query.lower():
            say("Ok , your pc will shut down, make sure you exit from all applications")
            subprocess.call(["shutdown", "/s"])
            
        elif "restart my pc" in query.lower():
            say("Ok , your pc will restart, make sure you exit from all applications")
            subprocess.call(["shutdown", "/r"])

        else:
            statement =query
            results = wikipedia.summary(statement, sentences = 3)
            say("According to Wikipedia")
            # print(results)
            say(results)
