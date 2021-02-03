from tkinter import *
from password import generate_password
import pyqrcode
from PIL import Image, ImageTk
import pyperclip


BACKGROUND_COLOR = "#2c061f"
LABEL_FONT       = ('calibre', 10, 'bold')


def copy_password(password):
    """Used to copy password to clipboard"""

    # using pyperclip copy method --> copy the password to clipboard
    pyperclip.copy(password)

    # show a success message to the user & disabling the copy button
    copy_button.config(text="✔ Copied", bg=BACKGROUND_COLOR, fg="white")
    copy_button.config(state=DISABLED)


def show_qrcode(password):
    """Used to show QR Code"""

    # getting the entire text from the entry widget
    text         = website_entry.get()

    # generate qr code with random password & user entered text as file name
    qr_code      = pyqrcode.create(content=f"{password}")
    # saving the qr code Images(QR Codes) folder
    qr_code.png(f"Images(QR Codes)/{text}.png", scale=3)

    # load the image from folder & create a label display it in the app
    load_image   = Image.open(f"Images(QR Codes)/{text}.png")
    render_image = ImageTk.PhotoImage(load_image)
    qr_label     = Label(image=render_image)
    qr_label.img = render_image
    qr_label.config(width=100, height=100)
    qr_label.grid(row=5, column=0, columnspan=2)

    # finally disabling the Qr button
    qr_button.config(text="✔ QR Code", bg=BACKGROUND_COLOR, fg="white")
    qr_button.config(state=DISABLED)


# ---------------------Copy & QR button---------------------------------
def show_copy_qr_buttons(password):
    """Used to show copy & qr button  """
    global copy_button, qr_button
    # copy button
    copy_button = Button()
    copy_button.config(text="Copy to Clipboard", font=LABEL_FONT, command=lambda: copy_password(password))
    copy_button.grid(row=4, column=0, pady=20, sticky="nsew")

    # Qr button
    qr_button = Button()
    qr_button.config(text="Generate QR Code", font=LABEL_FONT, command=lambda: show_qrcode(password))
    qr_button.grid(row=4, column=1, pady=20, sticky="nsew")


# -------------------Password---------------------------------
def get_password():
    """Used to get random password"""
    if website_entry.get() != '':

        # generating the password from generate_password() method from password.py file
        password_generated = generate_password()

        # inserting the password in app
        password_generated_label = Label()
        password_generated_label.config(text=password_generated, bg=BACKGROUND_COLOR, fg="white")
        password_generated_label.config(font=("Times", 18, "italic"))
        password_generated_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # showing the copy to clipboard & Qr code buttons
        show_copy_qr_buttons(password_generated)

        # changing the text & disabling it (generate password button)
        generate_password_button.config(text="✔ Password Generated")
        generate_password_button.config(state=DISABLED)

        # disabling the entry widget also
        website_entry.config(state=DISABLED)

    else:
        warning_label = Label()
        warning_label.config(text="⚠ Please Enter Website Name", bg=BACKGROUND_COLOR, fg="#c70039")
        warning_label.config(font=("Arial", 15, "italic"))
        warning_label.grid(row=3, column=0, columnspan=2, pady=15)
        window.after(1000, warning_label.grid_remove)


# ------------------------------------UI------------------------------
# creating a window,setting its size, title, bg color
window = Tk()
window.title("Password Generator")
window.geometry("340x430")
window.resizable(0, 0)
window.config(bg=BACKGROUND_COLOR)

app_title = Label()
app_title.config(text="Password Generator", font=("Arial", 20, "bold"), bg=BACKGROUND_COLOR, fg="white")
app_title.grid(row=0, column=0, columnspan=2, pady=20, padx=30)

# -----------------------Website Label, Entry----------------------------------
website_label = Label()
website_label.config(text="Enter Website Name", bg=BACKGROUND_COLOR, fg="white", font=LABEL_FONT)
website_label.grid(row=1, column=0)

website_entry = Entry()
website_entry.config(font=('Arial', 13, 'normal'), bg=BACKGROUND_COLOR, fg="#fcf8ec", borderwidth=5)
website_entry.grid(row=1, column=1)

# ----------------------Generate password button------------------------------
generate_password_button = Button()
generate_password_button.config(text="Generate Password", command=get_password)
generate_password_button.grid(row=2, column=0, columnspan=2, pady=15)

window.mainloop()
