import tkinter as tk
from tkinter import *
import requests
from tkinter import messagebox

root=tk.Tk()
root.title("weather app")
root.geometry("500x200")

def submit():
    city=city_var.get().lower()
    if city=="":
        messagebox.showerror('Error','invalid details')
        return 
    if not city:
        messagebox.showwarning('Input error','please input a valid city')
        return
    api_key="7b7cbc3d90f980af4ddf13d5e4ce9f2d"
    url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


    try:
        response=requests.get(url)
        
        if response.status_code == 200:
           data = response.json()
           temp = data['main']['temp']
           description = data['weather'][0]['description']
           print(f"Temperature in {city}: {temp}°C, {description}")
           
        else:
          messagebox.showerror("Error", "City not found or API error")

    except:
        messagebox.showerror("Error", "Network error occurred")

def submit1():
    messagebox.showinfo('done its done')
def submit_for():
    submit()
    submit1()

tk.Label(root,text="Details Wheater").grid(row=0,column=0,columnspan=3,sticky='w',padx=10,pady=5)

city_var=tk.StringVar()
tk.Label(root,text="Enter the City Name: ",font=('Arial',16,'bold')).grid(row=1,column=0,sticky='w',padx=10,pady=5)
enrty_city=tk.Entry(root,width=40,textvariable=city_var)
enrty_city.grid(row=1,column=1,padx=10,pady=5)
enrty_city.focus()

submit_btn=Button(root,text="Get Details",command=submit_for,bg="green",padx=10,pady=5)
submit_btn.grid(row=4,column=2,padx=10,pady=5)

root.mainloop()
