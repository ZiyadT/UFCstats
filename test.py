import tkinter as tk
from urllib.request import urlopen
import io
import base64
from bs4 import BeautifulSoup

def enter():
    pass

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(screen_height, screen_width)

window_width = (500/1920)*int(screen_width)
window_height = (770/1080)*int(screen_height)

root.geometry(f'{int(window_width)}x{int(window_height)}')
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

entry_selection = tk.Entry(frame, width=30, font=("Courier 12"))
entry_selection.bind('<Return>', enter)
entry_selection.place(x=120, y=725)

enter_button = tk.Button(frame, width=4, height=1, text='>', command=enter)
enter_button.place(x=447, y=724)

root.mainloop()