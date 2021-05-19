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
    name_label.place(x=frame.winfo_width()/2, y=100, anchor="center")
    name_label.config(font=("Arial", 12, "bold"), text=entry_selection.get(), bg='gray12', fg='red')

    record_label.place(x=frame.winfo_width()/2, y=120, anchor="center")
    record_label.config(font=("Arial", 12, "bold"), text=info[len(info) - 1], bg='gray12', fg='red')

    height_label = tk.Label(frame, text=info[0][0] + '\t' + ' ' + info[0][1], bg='gray12', fg='white')
    height_label.place(x=20, y=170)
    height_label.config(font=("Courier", 12, "bold"))

    weight_label = tk.Label(frame, text=info[1][0] + '\t' + ' ' + info[1][1], bg='gray12', fg='white')
    weight_label.place(x=20, y=210)
    weight_label.config(font=("Courier", 12, "bold"))

    reach_label = tk.Label(frame, text=info[2][0] + '\t' + ' ' + info[2][1], bg='gray12', fg='white')
    reach_label.place(x=20, y=250)
    reach_label.config(font=("Courier", 12, "bold"))

    stance_label = tk.Label(frame, text=info[3][0] + '\t' + ' ' + info[3][1], bg='gray12', fg='white')
    stance_label.place(x=20, y=290)
    stance_label.config(font=("Courier", 12, "bold"))

    dob_label = tk.Label(frame, text=info[4][0] + '\t' + ' ' + info[4][1], bg='gray12', fg='white')
    dob_label.place(x=20, y=330)
    dob_label.config(font=("Courier", 12, "bold"))

    slpm_label = tk.Label(frame, text=info[5][0] + '\t' + ' ' + info[5][1], bg='gray12', fg='white')
    slpm_label.place(x=20, y=370)
    slpm_label.config(font=("Courier", 12, "bold"))

    stracc_label = tk.Label(frame, text=info[6][0] + ' ' + info[6][1], bg='gray12', fg='white')
    stracc_label.place(x=20, y=410)
    stracc_label.config(font=("Courier", 12, "bold"))

    sapm_label = tk.Label(frame, text=info[7][0] + '\t' + ' ' + info[7][1], bg='gray12', fg='white')
    sapm_label.place(x=20, y=450)
    sapm_label.config(font=("Courier", 12, "bold"))

    strdef_label = tk.Label(frame, text=info[8][0] + '\t' + ' ' + info[8][1], bg='gray12', fg='white')
    strdef_label.place(x=20, y=490)
    strdef_label.config(font=("Courier", 12, "bold"))

    tdavg_label = tk.Label(frame, text=info[10][0] + '\t' + ' ' + info[10][1], bg='gray12', fg='white')
    tdavg_label.place(x=20, y=530)
    tdavg_label.config(font=("Courier", 12, "bold"))

    tdacc_label = tk.Label(frame, text=info[11][0] + '\t' + ' ' + info[11][1], bg='gray12', fg='white')
    tdacc_label.place(x=20, y=570)
    tdacc_label.config(font=("Courier", 12, "bold"))

    tddef_label = tk.Label(frame, text=info[12][0] + '\t' + ' ' + info[12][1], bg='gray12', fg='white')
    tddef_label.place(x=20, y=610)
    tddef_label.config(font=("Courier", 12, "bold"))

    subavg_label = tk.Label(frame, text=info[13][0] + ' ' + info[13][1], bg='gray12', fg='white')
    subavg_label.place(x=20, y=650)
    subavg_label.config(font=("Courier", 12, "bold"))


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
root.geometry('500x770')
root.title('UFC Stats')
root.resizable(width=False, height=False)

photo = tk.PhotoImage()

frame = tk.Canvas(root, width=500, height=770, bg = 'gray12')
frame.pack(side='top', fill='both', expand='yes')

name_label = tk.Label(frame)
record_label = tk.Label(frame)

# heading = tk.Label(frame, text='UFC', bg='gray12', fg='white')
# heading.config(font=("Courier", 44, "bold"))
# heading.place(x=190, y=0)

logo = tk.PhotoImage()
image_byt = urlopen("https://upload.wikimedia.org/wikipedia/commons/d/d7/UFC_Logo.png").read()
image_b64 = base64.encodebytes(image_byt)
logo.config(data=image_b64)

logo = logo.zoom(23)
logo = logo.subsample(310)

logo_pic = frame.create_image(100, 100, image=logo, anchor='ne')
frame.move(logo_pic, 220, -90)

subheading = tk.Label(frame, text='Fighter Statistics', bg='gray12', fg='white')
subheading.config(font=("Courier", 15, "bold"))
subheading.place(x=140, y=60)

label = tk.Label(frame, text='Fighter Name', bg='gray12', fg='white')
label.config(font=("Courier", 10, "bold"))
label.place(x=10, y=725)

entry_selection = ttk.Entry(frame, width=30, font=("Courier 12"))
entry_selection.bind('<Return>', enter)
entry_selection.place(x=120, y=725)

enter_button = tk.Button(frame, width=4, height=1, text='>', command=enter)
enter_button.place(x=447, y=724)

root.mainloop()
