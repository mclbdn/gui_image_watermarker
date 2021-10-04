import tkinter as tk
from tkinter import filedialog
from PIL import Image

watermark = ""

def upload_watermark():
    global watermark
    watermark = filedialog.askopenfilename(filetypes=(("GIF Files", ".gif"), ("JPEG Files", ".JPEG"), ("PNG Files", ".PNG")))
    print('Selected watermark:', watermark)

def upload_image():
    image = filedialog.askopenfilename(filetypes=(("GIF Files", ".gif"), ("JPEG Files", ".JPEG"), ("PNG Files", ".PNG")))
    print('Selected image:', image)

    with Image.open(image) as img:
        with Image.open(watermark) as wtrmrk:
            image_copy = img.copy().convert("RGBA")
            wtrmrk = wtrmrk.convert("RGBA")
            wtrmrk.thumbnail((200,200))
            position = ((image_copy.width - wtrmrk.width), (image_copy.height - wtrmrk.height))
            image_copy.paste(wtrmrk, position, wtrmrk)
            image_copy.show()

root = tk.Tk()
root.title("Image Watermarker")
root.geometry("400x300")

label = tk.Label(text="Please upload a picture as JPEG, JPG...")
label.pack()

upload_watermark_btn = tk.Button(text="1) Upload a watermark", command=upload_watermark)
upload_watermark_btn.pack(pady=20)

upload_image_btn = tk.Button(text="2) Upload an image", command=upload_image)
upload_image_btn.pack()

root.mainloop()

# https://www.tutorialspoint.com/python/tk_button.htm
# https://auth0.com/blog/image-processing-in-python-with-pillow/