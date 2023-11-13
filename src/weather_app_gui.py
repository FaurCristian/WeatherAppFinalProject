import tkinter as tk
from datetime import datetime, timedelta
from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk
from weather_data import WeatherData


class WeatherAppGUI:
    def __init__(self, window):
        print("Initializing WeatherAppGUI.")
        self.window = window
        self.setup_window()
        self.create_widgets()
        self.weather_data = WeatherData()
        print("WeatherAppGUI initialization complete.")

    def setup_window(self):
        print("Setting up the window...")
        self.window.title("Weather App")
        self.window.config(bg="#c70202")
        self.window.geometry("890x490")
        self.window.resizable(False, False)
        print("Window setup complete.")

    def create_widgets(self):
        print("Creating widgets...")
        self.create_gui_elements()
        self.create_labels()
        self.create_search_box()
        self.create_frame_boxes()
        self.create_clock_timezone_labels()
        self.create_cells()
        print("Widget creation complete.")

    # Function that change the icon
    def create_gui_elements(self):
        print("Creating GUI elements...")
        icon_image = PhotoImage(file="resources/Images/logo.png")
        self.window.iconphoto(False, icon_image)
        print("GUI elements created.")

    # Function that create the labels for this program
    def create_labels(self):
        print("Creating labels...")
        self.rounded_box = PhotoImage(file="resources/Images/Rounded Rectangle 1.png")
        Label(self.window, image=self.rounded_box, bg="#c70202").place(x=700, y=170)
        # Label
        self.temp_label = Label(self.window, text='Temperature: ', font=("Roboto Slab", 11), fg="white",
                                bg="#203243")
        self.temp_label.place(x=703, y=175)

        self.window_humidity_label = Label(self.window, text='Humidity: ',
                                           font=("Roboto Slab", 11), fg="white", bg="#203243")
        self.window_humidity_label.place(x=703, y=195)

        self.pressure_label = Label(self.window, text='Pressure: ', font=("Roboto Slab", 11), fg="white",
                                    bg="#203243")
        self.pressure_label.place(x=703, y=215)

        self.wind_sp_label = Label(self.window, text='Wind Speed: ', font=("Roboto Slab", 11), fg="white",
                                   bg="#203243")
        self.wind_sp_label.place(x=703, y=235)

        self.description_label = Label(self.window, text='Description: ', font=("Roboto Slab", 11), fg="white",
                                       bg="#203243")
        self.description_label.place(x=703, y=255)

        self.t = Label(self.window, font=("Roboto Slab", 10), fg="white", bg="#203243")
        self.t.place(x=792, y=176)
        self.h = Label(self.window, font=("Roboto Slab", 10), fg="white", bg="#203243")
        self.h.place(x=792, y=196)
        self.p = Label(self.window, font=("Roboto Slab", 10), fg="white", bg="#203243")
        self.p.place(x=792, y=216)
        self.w = Label(self.window, font=("Roboto Slab", 10), fg="white", bg="#203243")
        self.w.place(x=792, y=236)
        self.d = Label(self.window, font=("Roboto Slab", 10), fg="white", bg="#203243")
        self.d.place(x=792, y=256)
        print("Labels created.")

    def create_search_box(self):
        print("Creating search box...")
        self.search_image = PhotoImage(file="resources/Images/Rounded Rectangle 3.png")
        search_label = Label(image=self.search_image, bg="#c70202")
        search_label.place(x=220, y=225)

        self.weather_image = PhotoImage(file="resources/Images/Layer 7.png")
        weather_label = Label(image=self.weather_image, bg="#203243")
        weather_label.place(x=250, y=230)

        self.text_entry = tk.Entry(self.window, justify="center", width=15, font=("quicksand", 25, "bold"),
                                   bg="#203243", border=0, fg="white")

        self.text_entry.place(x=320, y=230)
        self.text_entry.focus()

        self.search_icon = PhotoImage(file="resources/Images/Layer 6.png")
        search_button = Button(image=self.search_icon, borderwidth=0, cursor="hand2", bg="#203243",
                               command=self.getweather)
        search_button.place(x=600, y=230)
        print("Search box created.")

    def create_frame_boxes(self):
        print("Creating frame boxes...")
        # Create the search box and related elements
        frame = Frame(self.window, width=900, height=180, bg="#212120")
        frame.pack(side=BOTTOM)

        # bottom boxes
        first_box = PhotoImage(file="resources/Images/Rounded Rectangle 2.png")
        second_box = PhotoImage(file="resources/Images/Rounded Rectangle 2 copy.png")

        Label(frame, image=first_box, bg="#c70202").place(x=30, y=20)
        Label(frame, image=second_box, bg="#c70202").place(x=300, y=30)
        Label(frame, image=second_box, bg="#c70202").place(x=400, y=30)
        Label(frame, image=second_box, bg="#c70202").place(x=500, y=30)
        Label(frame, image=second_box, bg="#c70202").place(x=600, y=30)
        Label(frame, image=second_box, bg="#c70202").place(x=700, y=30)
        Label(frame, image=second_box, bg="#c70202").place(x=800, y=30)
        print("Frame boxes created.")

    def create_clock_timezone_labels(self):
        print("Creating clock and timezone labels...")
        # Clock
        self.clock_label = Label(self.window, font=("Roboto Slab", 50, "bold"), fg="white", bg="#c70202")
        self.clock_label.place(x=30, y=20)

        # Timezone
        self.timezone = Label(self.window, font=("Roboto Slab", 20, "bold"), fg="white", bg="#c70202")
        self.timezone.place(x=600, y=20)

        # Long and Lat
        self.long_lat = Label(self.window, font=("Roboto Slab", 10, "bold"), fg="white", bg="#c70202")
        self.long_lat.place(x=600, y=50)
        print("Clock and timezone labels created.")

    def create_cells(self):
        print("Creating cells...")
        first_frame = Frame(self.window, width=230, height=132, bg="#282829")
        first_frame.place(x=35, y=335)

        self.day1 = Label(first_frame, font="arial 20", bg="#282829", fg="#fff")
        self.day1.place(x=100, y=5)

        self.first_image = Label(first_frame, bg="#282829")
        self.first_image.place(x=1, y=15)

        self.day1temp = Label(first_frame, bg="#282829", fg="#fff", font="arial 15 bold")
        self.day1temp.place(x=100, y=50)

        # second frame
        second_frame = Frame(self.window, width=70, height=115, bg="#282829")
        second_frame.place(x=305, y=345)

        self.day2 = Label(second_frame, bg="#282829", fg="#fff")
        self.day2.place(x=5, y=5)

        self.second_image = Label(second_frame, bg="#282829")
        self.second_image.place(x=7, y=20)

        self.day2temp = Label(second_frame, bg="#282829", fg="#fff")
        self.day2temp.place(x=2, y=70)
        # third frame
        third_frame = Frame(self.window, width=70, height=115, bg="#282829")
        third_frame.place(x=405, y=345)

        self.day3 = Label(third_frame, bg="#282829", fg="#fff")
        self.day3.place(x=5, y=5)

        self.third_image = Label(third_frame, bg="#282829")
        self.third_image.place(x=7, y=20)

        self.day3temp = Label(third_frame, bg="#282829", fg="#fff")
        self.day3temp.place(x=2, y=70)
        # fourth frame
        fourth_frame = Frame(self.window, width=70, height=115, bg="#282829")
        fourth_frame.place(x=505, y=345)

        self.day4 = Label(fourth_frame, bg="#282829", fg="#fff")
        self.day4.place(x=5, y=5)

        self.forth_image = Label(fourth_frame, bg="#282829")
        self.forth_image.place(x=7, y=20)

        self.day4temp = Label(fourth_frame, bg="#282829", fg="#fff")
        self.day4temp.place(x=2, y=70)
        # fifth frame
        fifth_frame = Frame(self.window, width=70, height=115, bg="#282829")
        fifth_frame.place(x=605, y=345)

        self.day5 = Label(fifth_frame, bg="#282829", fg="#fff")
        self.day5.place(x=5, y=5)

        self.fifth_image = Label(fifth_frame, bg="#282829")
        self.fifth_image.place(x=7, y=20)

        self.day5temp = Label(fifth_frame, bg="#282829", fg="#fff")
        self.day5temp.place(x=2, y=70)
        # sixth frame
        sixth_frame = Frame(self.window, width=70, height=115, bg="#282829")
        sixth_frame.place(x=705, y=345)

        self.day6 = Label(sixth_frame, bg="#282829", fg="#fff")
        self.day6.place(x=5, y=5)

        self.sixth_image = Label(sixth_frame, bg="#282829")
        self.sixth_image.place(x=7, y=20)

        self.day6temp = Label(sixth_frame, bg="#282829", fg="#fff")
        self.day6temp.place(x=2, y=70)
        # seventh frame
        seventh_frame = Frame(self.window, width=70, height=115, bg="#282829")
        seventh_frame.place(x=805, y=345)

        self.day7 = Label(seventh_frame, bg="#282829", fg="#fff")
        self.day7.place(x=5, y=5)

        self.seventh_image = Label(seventh_frame, bg="#282829")
        self.seventh_image.place(x=7, y=20)

        self.day7temp = Label(seventh_frame, bg="#282829", fg="#fff")
        self.day7temp.place(x=2, y=70)
        print("Cells created.")

    def getweather(self):
        print("Getting weather data...")
        try:
            city = self.text_entry.get()
            current_time, timezone, long_lat = self.weather_data.get_weather(city)
            self.clock_label.config(text=current_time)
            self.timezone.config(text=timezone)
            self.long_lat.config(text=long_lat)

            # weather:
            url = "https://ai-weather-by-meteosource.p.rapidapi.com/hourly"

            querystring = {
                "place_id": city,
                "timezone": "auto",
                "language": "en",
                "units": "auto"}

            headers = {
                "X-RapidAPI-Key": "66914dd25amshce3d79e92365c71p17ee14jsn6a50319ddb00",
                "X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()

            url_2 = "https://ai-weather-by-meteosource.p.rapidapi.com/daily"

            querystring_2 = {"place_id": city, "language": "en", "units": "metric"}

            headers_2 = {
                "X-RapidAPI-Key": "66914dd25amshce3d79e92365c71p17ee14jsn6a50319ddb00",
                "X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
            }

            response_daily = requests.get(url_2, headers=headers_2, params=querystring_2)

            data2 = response_daily.json()

            # current
            temp = data['hourly']['data'][0]['temperature']
            humidity = data['hourly']['data'][1]['humidity']
            pressure = data['hourly']['data'][1]['pressure']
            wind = data['hourly']['data'][0]['wind']['speed']
            description = data['hourly']['data'][0]['weather']

            self.t.config(text=(temp, "°C"))
            self.h.config(text=(humidity, "%"))
            self.p.config(text=(pressure, "hPa"))
            self.w.config(text=(wind, "m/s"))
            self.d.config(text=description)

            # first cell
            first_day_image = data2['daily']['data'][0]["icon"]
            photo1 = ImageTk.PhotoImage(file=f"resources/icon/{first_day_image}.png")
            self.first_image.config(image=photo1)
            self.first_image.image = photo1

            temp_min1 = data2['daily']['data'][0]["temperature_min"]
            temp_max1 = data2['daily']['data'][0]["temperature_max"]

            self.day1temp.config(text=f"Min: {temp_min1}\n Max: {temp_max1}")
            # second cell
            second_day_image = data2['daily']['data'][1]["icon"]
            photo2 = ImageTk.PhotoImage(file=f"resources/icon small/small/{second_day_image}.png")
            self.second_image.config(image=photo2)
            self.second_image.image = photo2

            temp_min2 = data2['daily']['data'][1]["temperature_min"]
            temp_max2 = data2['daily']['data'][1]["temperature_max"]

            self.day2temp.config(text=f"Min: {temp_min2}\n Max: {temp_max2}")

            # third cell
            third_day_image = data2['daily']['data'][2]["icon"]
            photo3 = ImageTk.PhotoImage(file=f"resources/icon small/small/{third_day_image}.png")
            self.third_image.config(image=photo3)
            self.third_image.image = photo3

            temp_min3 = data2['daily']['data'][2]["temperature_min"]
            temp_max3 = data2['daily']['data'][2]["temperature_max"]

            self.day3temp.config(text=f"Min: {temp_min3}\n Max: {temp_max3}")
            # forth cell
            forth_day_image = data2['daily']['data'][3]["icon"]
            photo4 = ImageTk.PhotoImage(file=f"resources/icon small/small/{forth_day_image}.png")
            self.forth_image.config(image=photo4)
            self.forth_image.image = photo4

            temp_min4 = data2['daily']['data'][3]["temperature_min"]
            temp_max4 = data2['daily']['data'][3]["temperature_max"]

            self.day4temp.config(text=f"Min: {temp_min4}\n Max: {temp_max4}")
            # fifth cell
            fifth_day_image = data2['daily']['data'][4]["icon"]
            photo5 = ImageTk.PhotoImage(file=f"resources/icon small/small/{fifth_day_image}.png")
            self.fifth_image.config(image=photo5)
            self.fifth_image.image = photo5

            temp_min5 = data2['daily']['data'][4]["temperature_min"]
            temp_max5 = data2['daily']['data'][4]["temperature_max"]

            self.day5temp.config(text=f"Min: {temp_min5}\n Max: {temp_max5}")
            # sixth cell
            sixth_day_image = data2['daily']['data'][5]["icon"]
            photo6 = ImageTk.PhotoImage(file=f"resources/icon small/small/{sixth_day_image}.png")
            self.sixth_image.config(image=photo6)
            self.sixth_image.image = photo6

            temp_min6 = data2['daily']['data'][5]["temperature_min"]
            temp_max6 = data2['daily']['data'][5]["temperature_max"]

            self.day6temp.config(text=f"Min: {temp_min6}\n Max: {temp_max6}")
            # seventh cell
            seventh_day_image = data2['daily']['data'][6]["icon"]
            photo7 = ImageTk.PhotoImage(file=f"resources/icon small/small/{seventh_day_image}.png")
            self.seventh_image.config(image=photo7)
            self.seventh_image.image = photo7

            temp_min7 = data2['daily']['data'][6]["temperature_min"]
            temp_max7 = data2['daily']['data'][6]["temperature_max"]

            self.day7temp.config(text=f"Min: {temp_min7}\n Max: {temp_max7}")

            # days

            first = datetime.now()
            self.day1.config(text=first.strftime("%A"))

            second = first + timedelta(days=1)
            self.day2.config(text=second.strftime("%A"))

            third = first + timedelta(days=2)
            self.day3.config(text=third.strftime("%A"))

            fourth = first + timedelta(days=3)
            self.day4.config(text=fourth.strftime("%A"))

            fifth = first + timedelta(days=4)
            self.day5.config(text=fifth.strftime("%A"))

            sixth = first + timedelta(days=5)
            self.day6.config(text=sixth.strftime("%A"))

            seventh = first + timedelta(days=6)
            self.day7.config(text=seventh.strftime("%A"))

        except Exception:
            messagebox.showerror("Weather App", "Invalid Entry!!")
        print("getweather function execution complete.")



