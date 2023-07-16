import cv2
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


def button_click(button_number):
    global image

    if button_number == 1:

        image = cv2.resize(image, None, fx=0.5, fy=0.5)

    elif button_number == 2:

        image = cv2.flip(image, 1)

    elif button_number == 3:

        image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    elif button_number == 4:

        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    elif button_number == 5:

        image = cv2.GaussianBlur(image, (7, 7), 0)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pil_image = Image.fromarray(image)

    pil_image = pil_image.resize((400, 400), Image.ANTIALIAS)

    img_tk = ImageTk.PhotoImage(pil_image)

    img_label.configure(image=img_tk)
    img_label.image = img_tk


def upload_image():
    global image

    filename = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                          filetypes=(("Image Files", ".jpg;.jpeg;.png"), ("All Files", ".*")))

    image = cv2.imread(filename)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pil_image = Image.fromarray(image)

    pil_image = pil_image.resize((400, 400), Image.ANTIALIAS)

    img_tk = ImageTk.PhotoImage(pil_image)

    img_label.configure(image=img_tk)
    img_label.image = img_tk

    for button in buttons:
        button.configure(state="normal")


window = Tk()
window.geometry("900x900")

buttons = []

################################################################
image_path = r"C:\Users\User\Downloads\logo.png"
image = Image.open(image_path)

# Resize the image if necessary
image = image.resize((100, 50))

# Create a Tkinter-compatible image object
tk_image = ImageTk.PhotoImage(image)

# Create the label and set the image
img_label_logo = Label(window, image=tk_image)
img_label_logo.pack()
################################################################

upload_button = Button(window, text="Upload Image", command=upload_image)
upload_button.pack()

for i in range(1, 6):
    button = Button(window, text="Button {}".format(i), state="disabled", command=lambda i=i: button_click(i))
    button.pack()
    buttons.append(button)

window.mainloop()
