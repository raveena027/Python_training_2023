import os
#import subprocess
import webbrowser


def send_sms():
    from twilio.rest import Client

    # Twilio credentials
    account_sid = 'Enter your Api_key'
    auth_token = 'enter you auth token'
    twilio_phone_number = "enter the twilio number"

    # Recipient's phone number
    to_phone_number = "enter receiver's phone number"

    # Your message
    your_message = "YOUR_MESSAGE"

    # Create Twilio client
    client = Client(account_sid,auth_token)

# Send SMS
    message = client.messages.create(
        body=your_message,
        from_=twilio_phone_number,
        to=to_phone_number
    )

    print(message.body)


def send_email():
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login('your email id', 'password')

    server.sendmail('your email id', 'receivers email id', 'Mail sent from python')
    print('mail sent')

def play_audio():

    import multiprocessing
    from playsound import playsound

    p = multiprocessing.Process(target=playsound, args=("audiofile_path",))
    p.start()
    input("press ENTER to stop playback")
    p.terminate()

def wiki_info():
    import wikipedia
 
    data = wikipedia.summary("ITC Limited")

    print(data)

def geolocation():
    import geopy
    import certifi
    import ssl
    import geopy.geocoders 

    from geopy.geocoders import Nominatim

    #Certficate  issue
    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx

      #compulsory add scheme
    location = Nominatim(scheme = 'https', user_agent="GetLoc")

       # entering the location name
    getLocation = location.geocode("Petlad, Anand")

        # printing address
    print(getLocation.address)

    # printing latitude and longitude
    print("Latitude = ", getLocation.latitude, "\n")
    print("Longitude = ", getLocation.longitude)

def whatsapp_msg():

    import pywhatkit
    # Defining the Phone Number and Message
    phone_number = input("Enter the phone number: ")
    message = input("Enter the message: ")

    # Sending the WhatsApp Message
    pywhatkit.sendwhatmsg_instantly(phone_number, message)

    # Displaying a Success Message
    print("WhatsApp message sent!")

def menu():
    print("1.Notepad")
    print("2.Chrome")
    print("3.Whatsapp")
    print("4.Email")
    print("5.SMS")
    print("6.ChatGPT")
    print("7.Geolocation")
    print("8.Twitter")
    print("9.wikipedia")
    print("10.Audio player")
    print("11.Video player")
    print("12.Speak")
    print("0. Exit")



while True:
    menu()
    option = int(input("Please enter a number (0 to exit): "))
    
    if option == 0:
        print("Exiting the program. Goodbye!")
        break
    elif option == 1:
        os.system("notepad filename.txt")
        
    elif option == 2:
        webbrowser.open("https://www.google.com/")
    
    elif option == 3:
        whatsapp_msg()

    elif option == 4:
        send_email()

    elif option == 5:
        send_sms()

    elif option == 7:
        geolocation()
    
    elif option == 9:
        wiki_info()
    elif option == 10:
        play_audio()

    else:
        print("Selected an invalid option. Please try again.")
