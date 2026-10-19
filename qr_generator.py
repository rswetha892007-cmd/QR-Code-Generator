import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk


def generate_qr():
    url = url_entry.get().strip()

    if not url:
        messagebox.showerror("Error", "Please enter a URL!")
        return

    try:
        qr = qrcode.make(url)
        qr.save("generated_qr.png")

        img = Image.open("generated_qr.png")
        img = img.resize((200, 200))
        photo = ImageTk.PhotoImage(img)

        qr_label.config(image=photo)
        qr_label.image = photo

        messagebox.showinfo("Success", "QR Code generated successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def save_qr():
    try:
        qr = qrcode.make(url_entry.get().strip())

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Images", "*.png")]
        )

        if file_path:
            qr.save(file_path)
            messagebox.showinfo("Success", "QR Code saved successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x450")
root.configure(bg="#f0f4f8")

title = tk.Label(
    root, text="QR Code Generator",
    font=("Arial", 18, "bold"), bg="#f0f4f8"
)
title.pack(pady=15)

tk.Label(
    root, text="Enter a URL:",
    font=("Arial", 12), bg="#f0f4f8"
).pack()

url_entry = tk.Entry(root, width=35, font=("Arial", 11))
url_entry.pack(pady=10)

tk.Button(
    root, text="Generate QR Code",
    command=generate_qr, bg="#2563eb", fg="white"
).pack(pady=8)

qr_label = tk.Label(root, bg="#f0f4f8")
qr_label.pack(pady=10)

tk.Button(
    root, text="Save QR Code as PNG",
    command=save_qr, bg="#16a34a", fg="white"
).pack(pady=8)

root.mainloop()