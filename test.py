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

window_width = (500/1920)*int(screen_width)  # 500
window_height = (770/1080)*int(screen_height)  # 770

root.geometry(f'{int(window_width)}x{int(window_height)}')
root.title('UFC Stats')
root.resizable(width=False, height=False)

photo = tk.PhotoImage()

frame = tk.Canvas(root, width=window_width, height=window_height, bg = 'gray12')
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

logo = logo.subsample(int(0.026*window_width))

logo_pic = frame.create_image(100, 100, image=logo, anchor='ne')
frame.move(logo_pic, int(0.44*window_width), int(-0.1169*window_height))

subheading = tk.Label(frame, text='Fighter Statistics', bg='gray12', fg='white')
subheading.config(font=("Courier", int(0.03*window_width), "bold"))
subheading.place(x=int(0.28*window_width), y=int(0.078*window_height))

label = tk.Label(frame, text='Fighter Name', bg='gray12', fg='white')
label.config(font=("Courier", int(0.02*window_width), "bold"))
label.place(x=int(0.02*window_width), y=int(0.941*window_height))

entry_selection = tk.Entry(frame, width=int(0.06*window_width), font=(f"Courier {int(0.024*window_width)}"))
entry_selection.bind('<Return>', enter)
entry_selection.place(x=int(0.24*window_width), y=int(0.941*window_height))

enter_button = tk.Button(frame, width=int(0.008*window_width), height=1, text='>', command=enter)
enter_button.place(x=int(0.894*window_width), y=int(0.940*window_height))

root.mainloop()