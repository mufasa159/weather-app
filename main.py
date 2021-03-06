import tkinter as tk
import requests

HEIGHT = 400
WIDTH = 700

root = tk.Tk()
root.title("Weather App")


def format_response(weather):
    try:
        name = weather["name"]
        desc = weather["weather"][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: ' + str(name) + '\nCondition: ' + str(desc) + '\nTemperature (ºF): ' + str(temp)
    except:
        final_str = "Something went wrong"
    return final_str


def get_weather(city):
    weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {"APPID":weather_key, "q":city, 'units':'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background_image = tk.PhotoImage(file='wallpaper2.png')

# background_label = tk.Label(root, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='blue', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="blue", bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
