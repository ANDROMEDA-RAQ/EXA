import tkinter as tk
from PIL import Image, ImageTk

# Custom style for buttons with rounded corners
class RoundButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(relief="flat", borderwidth=0)

# Your existing code here...

def on_login_student():
    print("Log In as Student button clicked!")

def on_login_admin():
    print("Log In as Admin button clicked!")

def on_sign_up():
    print("Sign Up with Your PUP ID button clicked!")

# Initialize the Tkinter app
root = tk.Tk()
root.title("Library System")
root.geometry("500x600")

# Load background image
try:
    background_image = Image.open(r"C:\Users\JANREY\OneDrive\Desktop\download.png")  # Change this path to your landscape image
    background_image = background_image.resize((1600, 1600), Image.LANCZOS)  # Resize to fit window size
    background_photo = ImageTk.PhotoImage(background_image)
except FileNotFoundError:
    print("Error: Background image not found. Please check the file path.")
    background_photo = None

# Setting background image
background_label = tk.Label(root, image=background_photo)
if background_photo:
    background_label.image = background_photo  # Keep reference to avoid garbage collection
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add the red header background
header_frame = tk.Frame(root, bg="#800000", height=300)
header_frame.pack(fill="x")

# Add university logo
canvas = tk.Canvas(header_frame, width=100, height=100, bg="#800000", highlightthickness=0)
canvas.pack(pady=20)

# Load and display image
try:
    logo_image = Image.open(r"C:\Users\JANREY\OneDrive\Desktop\pngkey.com-phillies-logo-png-528919.png").resize((100, 100))  # Resize for consistency
    logo = ImageTk.PhotoImage(logo_image)
    canvas.create_image(50, 50, image=logo)
    canvas.image = logo  # Prevent garbage collection
except FileNotFoundError:
    print("Error: Logo image not found. Please check the file path.")

# University and Library Text
university_name = tk.Label(header_frame, text="Polytechnic University of the Philippines", 
                           bg="#800000", fg="white", font=("Helvetica", 14))
university_name.pack()

library_label = tk.Label(header_frame, text="LIBRARY", bg="#800000", 
                         fg="white", font=("Helvetica", 24, "bold"))
library_label.pack()

# Buttons for Login and Register
login_student_button = RoundButton(root, text="LOG IN AS STUDENT", command=on_login_student, 
                                 bg="#800000", fg="white", font=("Helvetica", 16), padx=35, pady=15)
login_student_button.place(relx=0.5, rely=0.5, anchor='center')  

login_admin_button = RoundButton(root, text="LOG IN AS ADMIN", command=on_login_admin, 
                               bg="#800000", fg="white", font=("Helvetica", 16), padx=50, pady=15)
login_admin_button.place(relx=0.5, rely=0.6, anchor='center')  # Adjusted for new button

# New button for Sign Up
sign_up_button = RoundButton(root, text="SIGN UP YOUR PUP ID", command=on_sign_up, 
                           bg="#008000", fg="white", font=("Helvetica", 16), padx=25, pady=15)
sign_up_button.place(relx=0.5, rely=0.7, anchor='center')  # Positioned below the login buttons

# Start the GUI loop
root.mainloop()