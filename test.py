import tkinter as tk
from tkinter import ttk
from scraper import Scraper
from urllib.request import urlopen
import urllib.error
import base64

def enter(event=None):
    name = entry_selection.get()
    retrieve_info = Scraper
    url = retrieve_info.search(Scraper, athlete_name=name)
    info = retrieve_info.text_scrape(Scraper, url=url)
    image_url = retrieve_info.image_scrape(Scraper, athlete_name=name)
    display_image(image_url)
    display_stats(info)


def display_stats(info):
    name_label.config(font=("Arial", 12, "bold"), text=entry_selection.get(), bg='gray12', fg='red')
    record_label.config(font=("Arial", 12, "bold"), text=info[len(info) - 1], bg='gray12', fg='red')
    height_label.config(font=("Courier", 12, "bold"), text=info[0][0] + '\t' + ' ' + info[0][1], bg='gray12', fg='white')
    weight_label.config(font=("Courier", 12, "bold"), text=info[1][0] + '\t' + ' ' + info[1][1], bg='gray12', fg='white')
    reach_label.config(font=("Courier", 12, "bold"), text=info[2][0] + '\t' + ' ' + info[2][1], bg='gray12', fg='white')
    stance_label.config(font=("Courier", 12, "bold"),  text=info[3][0] + '\t' + ' ' + info[3][1], bg='gray12', fg='white')
    dob_label.config(font=("Courier", 12, "bold"), text=info[4][0] + '\t' + ' ' + info[4][1], bg='gray12', fg='white')
    slpm_label.config(font=("Courier", 12, "bold"), text=info[5][0] + '\t' + ' ' + info[5][1], bg='gray12', fg='white')
    stracc_label.config(font=("Courier", 12, "bold"),text=info[6][0] + ' ' + info[6][1], bg='gray12', fg='white')
    sapm_label.config(font=("Courier", 12, "bold"), text=info[7][0] + '\t' + ' ' + info[7][1], bg='gray12', fg='white')
    strdef_label.config(font=("Courier", 12, "bold"), text=info[8][0] + '\t' + ' ' + info[8][1], bg='gray12', fg='white')
    tdavg_label.config(font=("Courier", 12, "bold"), text=info[10][0] + '\t' + ' ' + info[10][1], bg='gray12', fg='white')
    tdacc_label.config(font=("Courier", 12, "bold"), text=info[11][0] + '\t' + ' ' + info[11][1], bg='gray12', fg='white')
    tddef_label.config(font=("Courier", 12, "bold"),  text=info[12][0] + '\t' + ' ' + info[12][1], bg='gray12', fg='white')
    subavg_label.config(font=("Courier", 12, "bold"),  text=info[13][0] + ' ' + info[13][1], bg='gray12', fg='white')


def display_image(image_url):
    global photo
    try:
        image_byt = urlopen(image_url).read()
        image_b64 = base64.encodebytes(image_byt)
        photo.config(data=image_b64)

        photo = photo.zoom(23)
        photo = photo.subsample(40)

        fighter_pic = frame.create_image(100, 100, image=photo, anchor='ne')
        frame.move(fighter_pic, 385, 100)
    except urllib.error.HTTPError:
        error_label = tk.Label(frame, text='Picture\nnot\nfound', fg='red')
        error_label.place(x = 320, y = 300)
        error_label.configure(font=("Courier", 12, "bold"))

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = int(screen_width/2)  # 500
window_height = int(screen_height*0.75)  # 770

root.geometry(f'{window_width}x{window_height}')
root.title('UFC Stats')
root.resizable(width=False, height=False)

photo = tk.PhotoImage()

frame = tk.Canvas(root, width=window_width, height=window_height, bg = 'gray12')
frame.pack(side='top', fill='both', expand='yes')

empty_label = tk.Label(frame, width=19, height=5, bg='red')
empty_label.grid(row=0, column=0)

heading = tk.Label(frame, bg='gray12', fg='white')
heading.config(font=("Courier", 44, "bold"))
heading.grid(row=0, column=1, sticky='nsew')

empty_label2 = tk.Label(frame, width=19, height=5, bg='red')
empty_label2.grid(row=0, column=2)

logo = tk.PhotoImage()
image_byt = urlopen("https://upload.wikimedia.org/wikipedia/commons/d/d7/UFC_Logo.png").read()
image_b64 = base64.encodebytes(image_byt)
logo.config(data=image_b64)

logo = logo.subsample(13)

logo_pic = frame.create_image(100, 100, image=logo, anchor='ne')
frame.move(logo_pic, 220, -90)

subheading = tk.Label(frame, text='Fighter Statistics', bg='gray12', fg='white')
subheading.config(font=("Courier", 15, "bold"))
subheading.grid(row=1, column=1, sticky='nsew')

name_label = tk.Label(frame)
name_label.grid(row=2, column=1)
name_label.config(font=("Arial", 12, "bold"),  bg='gray12', fg='red')

record_label = tk.Label(frame)
record_label.grid(row=3, column=1, sticky='nsew')
record_label.config(font=("Arial", 12, "bold"),  bg='gray12', fg='red')

height_label = tk.Label(frame,  height=2, bg='gray12', fg='white')
height_label.grid(row=5, column=0, columnspan=2, sticky='w', padx=15)
height_label.config(font=("Courier", 12, "bold"))

weight_label = tk.Label(frame,  height=2, bg='gray12', fg='white')
weight_label.grid(row=6, column=0, columnspan=2, sticky='w', padx=15)
weight_label.config(font=("Courier", 12, "bold"))

reach_label = tk.Label(frame,  height=2, bg='gray12', fg='white')
reach_label.grid(row=7, column=0, columnspan=2, sticky='w', padx=15)
reach_label.config(font=("Courier", 12, "bold"))

stance_label = tk.Label(frame,  height=2, bg='gray12', fg='white')
stance_label.grid(row=8, column=0, columnspan=2, sticky='w', padx=15)
stance_label.config(font=("Courier", 12, "bold"))

dob_label = tk.Label(frame,  height=2, bg='gray12', fg='white')
dob_label.grid(row=9, column=0, columnspan=2, sticky='w', padx=15)
dob_label.config(font=("Courier", 12, "bold"))

slpm_label = tk.Label(frame,  height=2, bg='gray12', fg='white')
slpm_label.grid(row=10, column=0, columnspan=2, sticky='w', padx=15)
slpm_label.config(font=("Courier", 12, "bold"))

stracc_label = tk.Label(frame,  height=2, bg='gray12', fg='white')
stracc_label.grid(row=11, column=0, columnspan=2, sticky='w', padx=15)
stracc_label.config(font=("Courier", 12, "bold"))

sapm_label = tk.Label(frame,  height=2, bg='gray12', fg='white')
sapm_label.grid(row=12, column=0, columnspan=2, sticky='w', padx=15)
sapm_label.config(font=("Courier", 12, "bold"))

strdef_label = tk.Label(frame,  height=2, bg='gray12', fg='white')
strdef_label.grid(row=13, column=0, columnspan=2, sticky='w', padx=15)
strdef_label.config(font=("Courier", 12, "bold"))

tdavg_label = tk.Label(frame,  height=2, bg='gray12', fg='white')
tdavg_label.grid(row=14, column=0, columnspan=2, sticky='w', padx=15)
tdavg_label.config(font=("Courier", 12, "bold"))

tdacc_label = tk.Label(frame,  height=2, bg='gray12', fg='white')
tdacc_label.grid(row=15, column=0, columnspan=2, sticky='w', padx=15)
tdacc_label.config(font=("Courier", 12, "bold"))

tddef_label = tk.Label(frame,  height=2, bg='gray12', fg='white')
tddef_label.grid(row=16, column=0, columnspan=2, sticky='w', padx=15)
tddef_label.config(font=("Courier", 12, "bold"))

subavg_label = tk.Label(frame,  height=2, bg='gray12', fg='white')
subavg_label.grid(row=17, column=0, columnspan=2, sticky='w', padx=15)
subavg_label.config(font=("Courier", 12, "bold"))

empty_label3 = tk.Label(frame, bg='gray12')
empty_label3.grid(row=18, column=0)

label = tk.Label(frame, text='Fighter Name', bg='gray12', fg='white')
label.config(font=("Courier", 11, "bold"))
label.grid(row=19, column=0, sticky='w', padx=15)

entry_selection = tk.Entry(frame)
entry_selection.bind('<Return>', enter)
entry_selection.grid(row=19, column=1, sticky='ew', padx=4)

enter_button = tk.Button(frame, height=1, text='>', command=enter)
enter_button.grid(row=19, column=2, sticky='ew', padx=20)

root.mainloop()