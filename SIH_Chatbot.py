import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyaudio

eng = pyttsx3.init("sapi5")
voices = eng.getProperty("voices")
print(voices[1].id)
eng.setProperty("voice",voices[1].id)
eng.setProperty("rate",120)
hour = datetime.datetime.now().hour
start_and_quit_program = True


def intro():
    eng.say("Hello This is Decoders Chatbot at your service")
    eng.runAndWait()


def get_user_name():
    rr = sr.Recognizer()
    with sr.Microphone() as name:
        print("Hey Speak whats you name.....")
        eng.say("Hey Speak whats you name")
        eng.runAndWait()
        listen_user_name = rr.listen(name,timeout=4,phrase_time_limit=4)
    try:
        global user_name
        user_name = rr.recognize_google(listen_user_name,language="en-in")
        eng.say(f"Ok So Your Name is {user_name}")
        eng.runAndWait()
        print(f"Ok So Your Name is : {user_name}")

    except Exception as e:
        print("Sorry I Cant't Recognize Your Name")
        eng.say("Sorry I Cant't Recognize Your Name")
        eng.runAndWait()



def Welcome():
    if hour >= 0 and hour < 12:
        eng.say(f"Hello Good Morning {user_name},How May I Help You")
        eng.runAndWait()
    elif hour >= 12 and hour < 16:
        eng.say(f"Hello Good Afternoon {user_name},How May I Help You")
        eng.runAndWait()
    elif hour >= 16 and hour < 20:
        eng.say(f"Hello Good Evening {user_name},How May I Help You")
        eng.runAndWait()
    elif hour >= 20 and hour <= 24:
        eng.say(f"Hello Good Night {user_name},How May I Help You")
        eng.runAndWait()


def takecomm():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"i am Listening...")
        eng.say(f" am Listening")
        eng.runAndWait()
        audio = r.listen(source,timeout=7,phrase_time_limit=7)
    try:
        print("Recognizing...")
        que = r.recognize_google(audio,language="en-in")
        print(f"{user_name} :{que}\n")
    except Exception as e:
        eng.say("Sorry I Cant't Recognize please speak again")
        eng.runAndWait()
        print("Sorry I Cant't Recognize please speak again")
        print(e)
    return que

if __name__=="__main__":
    intro()
    get_user_name()
    Welcome()


    while start_and_quit_program:
        recognize_user_cmd = takecomm().lower()
        with open("chatbot_FAQs_Asked.txt", "a") as file1:
            file1.write(f"{user_name} said : {recognize_user_cmd} \n")

        if "fee structure" in recognize_user_cmd:
            eng.say("showing you the fee structure of mauli college of engineering")
            eng.runAndWait()
            webbrowser.open("http://mcoet.mauligroup.org/Fees%20Structure/FEES%20For%20A.%20Y.%202018-19.pdf")

        elif "chairman" in recognize_user_cmd:
            print("Shri Dnyaneshwar Dada Patil is the charirman of mauli group of institutions")
            eng.say("Shree Dnyaneshwar Dada Patil is the charirman of mauli group of institutions")
            eng.runAndWait()

        elif "principal" in recognize_user_cmd:
            print("Dr.C.M.Jadhao is the principal of mauli college of engineering")
            eng.say("Doctor C M Jadhao is the principal of mauli college of engineering")
            eng.runAndWait()


        elif "about mauli" in recognize_user_cmd:
            eng.say("you can see all the information about mauli college of engineering here")
            eng.runAndWait()
            webbrowser.open("http://mcoet.mauligroup.org/aboutus.html")

        elif "training and placement"  in recognize_user_cmd or  "t and p"  in recognize_user_cmd :
            eng.say("Showing you the result for training and placement in mauli college of engineering")
            eng.runAndWait()
            webbrowser.open("http://mcoet.mauligroup.org/abouttandp.html")

        elif "courses" in recognize_user_cmd:
            eng.say("Showing you the courses availabel in mauli college of engineering")
            eng.runAndWait()
            webbrowser.open("http://mcoet.mauligroup.org/courses.html")

        elif "website" in recognize_user_cmd:
            eng.say("opening website of mauli college of engineering for you")
            eng.runAndWait()
            webbrowser.open("http://mcoet.mauligroup.org/index.html")

        elif "images" in recognize_user_cmd or "photos" in recognize_user_cmd or "pictures" in recognize_user_cmd or "photographs" in recognize_user_cmd :
            eng.say("showing you some of the images of mauli college of engineering")
            eng.runAndWait()
            webbrowser.open("http://mcoet.mauligroup.org/photographs.html")

        elif "placement records" in recognize_user_cmd or "placements" in recognize_user_cmd or "placement record" in recognize_user_cmd  or "placements record" in recognize_user_cmd:
            eng.say("Showing the Placement Records of mauli college of engineering")
            eng.runAndWait()
            webbrowser.open("http://mcoet.mauligroup.org/placementrecord-tnp.html")

        elif "recruiters" in recognize_user_cmd or "placements" in recognize_user_cmd  or "creators" in recognize_user_cmd or "re creators" in recognize_user_cmd:
            eng.say("The recuiters are")
            eng.runAndWait()
            webbrowser.open("http://mcoet.mauligroup.org/campusoffcampus.html")

        start_and_quit_program = False
