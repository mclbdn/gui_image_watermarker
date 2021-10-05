import tkinter as tk
from tkinter import Frame, filedialog
from PIL import Image

watermark = ""


def upload_watermark():
    global watermark
    watermark = filedialog.askopenfilename(
        filetypes=(("GIF Files", ".gif"), ("JPEG Files", ".JPEG"), ("PNG Files", ".PNG"))
    )
    print("Selected watermark:", watermark)


def upload_image():
    image = filedialog.askopenfilename(
        filetypes=(("GIF Files", ".gif"), ("JPEG Files", ".JPEG"), ("PNG Files", ".PNG"))
    )
    print("Selected image:", image)

    with Image.open(image) as img:
        with Image.open(watermark) as wtrmrk:
            image_copy = img.copy().convert("RGBA")
            wtrmrk = wtrmrk.convert("RGBA")
            wtrmrk.thumbnail((200, 200))
            position = ((image_copy.width - wtrmrk.width), (image_copy.height - wtrmrk.height))
            image_copy.paste(wtrmrk, position, wtrmrk)
            image_copy.show()


root = tk.Tk()
root.title("Image Watermarker")
root.geometry("400x200")

top = Frame(root)
top.pack(side="top")
label = tk.Label(text="Upload an image in JPEG, GIF or PNG formats")
label.pack(in_=top, side="top", pady=20)

upload_watermark_btn = tk.Button(text="1) Upload a watermark", command=upload_watermark)
upload_watermark_btn.pack(in_=top, side="left")

upload_image_btn = tk.Button(text="2) Upload an image", command=upload_image)
upload_image_btn.pack(in_=top, side="right")

root.mainloop()
