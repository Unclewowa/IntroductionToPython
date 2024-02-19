from io import BytesIO
import tkinter
from tkinter import Button
import requests
from PIL import Image, ImageTk

filename = ""
app = tkinter.Tk()
label1: tkinter.Label
l_width: tkinter.Label
l_height: tkinter.Label
b_cat: BytesIO
size = (640, 480)
app.geometry("640x550")


def clear_frame() -> None:
    global label1
    try:
        label1.destroy()
    except NameError:
        pass


def save_image() -> None:
    global b_cat, filename
    cat_image = Image.open(b_cat)
    cat_image.save(filename)


def load_image() -> None:
    global app, tkinter, label1, filename, l_width, l_height, b_cat
    clear_frame()
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    if r.ok:
        answer = r.json()
        r_dict = dict(answer[0])
        filename = r_dict['url'].split('/')[-1]
        cat = requests.get(r_dict['url'])
        l_name.configure(text="name:"+filename)
        l_width.configure(text="width:"+str(r_dict['width']))
        l_height.configure(text="height:"+str(r_dict['height']))
        b_cat = BytesIO(cat.content)
        cat_image = Image.open(b_cat)
        cat_image.thumbnail(size)
        ci = ImageTk.PhotoImage(cat_image)
        label1 = tkinter.Label(image=ci)
        label1.image = ci
        label1.place(x=0, y=50)


if __name__ == '__main__':
    btn = Button(app, text='Show cat', command=load_image)
    save_btn = Button(app, text='Save', command=save_image)
    btn.grid(column=0, row=2)
    save_btn.grid(column=1, row=2)
    l_name = tkinter.Label(text="name:")
    l_name.grid(column=3, row=2)
    l_width = tkinter.Label(text="width: 0")
    l_width.grid(column=4, row=2)
    l_height = tkinter.Label(text="width: 0")
    l_height.grid(column=5, row=2)

    app.mainloop()
