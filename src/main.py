import tkinter as tk

from weather_app_gui import WeatherAppGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherAppGUI(root)
    root.mainloop()
