import tkinter as tk
from scraper import Scraper
from urllib.request import urlopen
import urllib.error
import base64
from math import sqrt


def enter(event=None):
    name = entry_selection.get()
    retrieve_info = Scraper
    url = retrieve_info.search(Scraper, athlete_name=name)
    info = retrieve_info.text_scrape(Scraper, url=url)
    image_url = retrieve_info.image_scrape(Scraper, athlete_name=name)
    display_image(image_url)
    display_stats(info)


def display_stats(info):
    name_label.config(font=("Arial", round(0.01307*font_line), "bold"), text=entry_selection.get(), bg='gray12', fg='red')
    record_label.config(font=("Arial", round(0.01307*font_line), "bold"), text=info[len(info) - 1], bg='gray12', fg='red')
    height_label.config(font=("Courier", round(0.01307*font_line), "bold"), text=info[0][0] + '\t' + ' ' + info[0][1], bg='gray12', fg='white')
    weight_label.config(font=("Courier", round(0.01307*font_line), "bold"), text=info[1][0] + '\t' + ' ' + info[1][1], bg='gray12', fg='white')
    reach_label.config(font=("Courier", round(0.01307*font_line), "bold"), text=info[2][0] + '\t' + ' ' + info[2][1], bg='gray12', fg='white')
    stance_label.config(font=("Courier", round(0.01307*font_line), "bold"),  text=info[3][0] + '\t' + ' ' + info[3][1], bg='gray12', fg='white')
    dob_label.config(font=("Courier", round(0.01307*font_line), "bold"), text=info[4][0] + '\t' + ' ' + info[4][1], bg='gray12', fg='white')
    slpm_label.config(font=("Courier", round(0.01307*font_line), "bold"), text=info[5][0] + '\t' + ' ' + info[5][1], bg='gray12', fg='white')
    stracc_label.config(font=("Courier", round(0.01307*font_line), "bold"),text=info[6][0] + ' ' + info[6][1], bg='gray12', fg='white')
    sapm_label.config(font=("Courier", round(0.01307*font_line), "bold"), text=info[7][0] + '\t' + ' ' + info[7][1], bg='gray12', fg='white')
    strdef_label.config(font=("Courier", round(0.01307*font_line), "bold"), text=info[8][0] + '\t' + ' ' + info[8][1], bg='gray12', fg='white')
    tdavg_label.config(font=("Courier", round(0.01307*font_line), "bold"), text=info[10][0] + '\t' + ' ' + info[10][1], bg='gray12', fg='white')
    tdacc_label.config(font=("Courier", round(0.01307*font_line), "bold"), text=info[11][0] + '\t' + ' ' + info[11][1], bg='gray12', fg='white')
    tddef_label.config(font=("Courier", round(0.01307*font_line), "bold"),  text=info[12][0] + '\t' + ' ' + info[12][1], bg='gray12', fg='white')
    subavg_label.config(font=("Courier", round(0.01307*font_line), "bold"),  text=info[13][0] + ' ' + info[13][1], bg='gray12', fg='white')


def display_image(image_url):
    global photo
    try:
        image_byt = urlopen(image_url).read()
        image_b64 = base64.encodebytes(image_byt)
        photo.config(data=image_b64)

        photo = photo.subsample(round(0.00217842*font_line))

        fighter_pic = frame.create_image(100, 100, image=photo, anchor='ne')
        frame.move(fighter_pic, round(0.77*window_width), round(0.12987*window_height))
    except urllib.error.HTTPError:
        error_label = tk.Label(frame, text='Picture\nnot\nfound', fg='red')
        error_label.place(x = 320, y = 300)
        error_label.configure(font=("Courier", 12, "bold"))

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = int(screen_width*500/1920)  # 500
window_height = int(screen_height*770/1080)  # 770

print(round(0.0025974*window_height))

font_line = sqrt(window_width**2 + window_height**2)
print(font_line)
print(round(0.01307*font_line))

print(screen_width, screen_height)
print(window_width, window_height)

root.geometry("%dx%d" % (window_width, window_height))
root.title('UFC Stats')
#root.resizable(width=False, height=False)

photo = tk.PhotoImage()

frame = tk.Canvas(root, width=window_width, height=window_height, bg='gray12')
frame.pack(side='top', fill='both', expand='yes')

empty_label = tk.Label(frame, width=int(round(0.036*window_width)), height=int(round(0.005*window_height)), bg='gray12')
empty_label.grid(row=0, column=0)

# heading = tk.Label(frame, text='UFC', bg='gray12', fg='white')
# heading.config(font=("Courier", round(0.046925*font_line), "bold"))
# heading.grid(row=0, column=1, sticky='nsew')

empty_label2 = tk.Label(frame, width=int(round(0.036*window_width)), height=int(round(0.005*window_height)), bg='gray12')
empty_label2.grid(row=0, column=2)

logo = tk.PhotoImage()
image_byt = urlopen("https://upload.wikimedia.org/wikipedia/commons/d/d7/UFC_Logo.png").read()
image_b64 = base64.encodebytes(image_byt)
logo.config(data=image_b64)

logo = logo.subsample(round(0.014159741*font_line))

logo_pic = frame.create_image(100, 100, image=logo, anchor='ne')
frame.move(logo_pic, round(0.44*window_width), round(-0.11688*window_height))

subheading = tk.Label(frame, text='Fighter Statistics', bg='gray12', fg='white')
subheading.config(font=("Courier", round(0.016338*font_line), "bold"))
subheading.grid(row=1, column=1, sticky='nsew')

name_label = tk.Label(frame)
name_label.grid(row=2, column=1)
name_label.config(font=("Arial", round(0.01307*font_line), "bold"),  bg='gray12', fg='red')

record_label = tk.Label(frame)
record_label.grid(row=3, column=1, sticky='nsew')
record_label.config(font=("Arial", round(0.01307*font_line), "bold"), bg='gray12', fg='red')

height_label = tk.Label(frame, height=round(0.0025974*window_height), bg='gray12', fg='white')
height_label.grid(row=5, column=0, columnspan=2, sticky='w', padx=15)
height_label.config(font=("Courier", round(0.01307*font_line), "bold"))

weight_label = tk.Label(frame, height=round(0.0025974*window_height), bg='gray12', fg='white')
weight_label.grid(row=6, column=0, columnspan=2, sticky='w', padx=15)
weight_label.config(font=("Courier", round(0.01307*font_line), "bold"))

reach_label = tk.Label(frame, height=round(0.0025974*window_height), bg='gray12', fg='white')
reach_label.grid(row=7, column=0, columnspan=2, sticky='w', padx=15)
reach_label.config(font=("Courier", round(0.01307*font_line), "bold"))

stance_label = tk.Label(frame, height=round(0.0025974*window_height), bg='gray12', fg='white')
stance_label.grid(row=8, column=0, columnspan=2, sticky='w', padx=15)
stance_label.config(font=("Courier", round(0.01307*font_line), "bold"))

dob_label = tk.Label(frame, height=round(0.0025974*window_height), bg='gray12', fg='white')
dob_label.grid(row=9, column=0, columnspan=2, sticky='w', padx=15)
dob_label.config(font=("Courier", round(0.01307*font_line), "bold"))

slpm_label = tk.Label(frame, height=round(0.0025974*window_height), bg='gray12', fg='white')
slpm_label.grid(row=10, column=0, columnspan=2, sticky='w', padx=15)
slpm_label.config(font=("Courier", round(0.01307*font_line), "bold"))

stracc_label = tk.Label(frame, height=round(0.0025974*window_height), bg='gray12', fg='white')
stracc_label.grid(row=11, column=0, columnspan=2, sticky='w', padx=15)
stracc_label.config(font=("Courier", round(0.01307*font_line), "bold"))

sapm_label = tk.Label(frame, height=round(0.0025974*window_height), bg='gray12', fg='white')
sapm_label.grid(row=round(0.01307*font_line), column=0, columnspan=2, sticky='w', padx=15)
sapm_label.config(font=("Courier", round(0.01307*font_line), "bold"))

strdef_label = tk.Label(frame, height=round(0.0025974*window_height), bg='gray12', fg='white')
strdef_label.grid(row=13, column=0, columnspan=2, sticky='w', padx=15)
strdef_label.config(font=("Courier", round(0.01307*font_line), "bold"))

tdavg_label = tk.Label(frame, height=round(0.0025974*window_height), bg='gray12', fg='white')
tdavg_label.grid(row=14, column=0, columnspan=2, sticky='w', padx=15)
tdavg_label.config(font=("Courier", round(0.01307*font_line), "bold"))

tdacc_label = tk.Label(frame, height=round(0.0025974*window_height), bg='gray12', fg='white')
tdacc_label.grid(row=15, column=0, columnspan=2, sticky='w', padx=round(0.03*window_width))
tdacc_label.config(font=("Courier", round(0.01307*font_line), "bold"))

tddef_label = tk.Label(frame, height=round(0.0025974*window_height), bg='gray12', fg='white')
tddef_label.grid(row=16, column=0, columnspan=2, sticky='w', padx=round(0.03*window_width))
tddef_label.config(font=("Courier", round(0.01307*font_line), "bold"))

subavg_label = tk.Label(frame, height=round(0.0025974*window_height), bg='gray12', fg='white')
subavg_label.grid(row=17, column=0, columnspan=2, sticky='w', padx=round(0.03*window_width))
subavg_label.config(font=("Courier", round(0.01307*font_line), "bold"))

empty_label3 = tk.Label(frame, bg='gray12')
empty_label3.grid(row=18, column=0, sticky='w')

label = tk.Label(frame, text='Fighter Name', bg='gray12', fg='white')
label.config(font=("Courier", round(0.01198*font_line), "bold"))
label.grid(row=19, column=0, sticky='w', padx=round(0.03*window_width))

entry_selection = tk.Entry(frame)
entry_selection.bind('<Return>', enter)
entry_selection.grid(row=19, column=1, sticky='ew', padx=4)

enter_button = tk.Button(frame, height=round(0.00129870*window_height), text='>', command=enter)
enter_button.grid(row=19, column=2, sticky='ew', padx=round(0.04*window_width))

for row in range(19):
    root.grid_rowconfigure(row, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()