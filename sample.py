import tkinter as tk
from PIL import Image, ImageTk

# Custom Styles
style = {
    "bg_color": "#800000",  # Maroon background
    "text_color": "#FFFFFF",  # White text color
    "button_color": "#FFD700",  # Gold button background for visibility
    "button_text_color": "#800000",  # Maroon button text color
    "button_font": ("Arial", 12, "bold"),
}

# Main Window
root = tk.Tk()
root.title("Library System")
root.geometry("800x600")

# Header Frame
header = tk.Frame(root, bg=style["bg_color"], height=100)
header.pack(fill="x")

# Load and resize logo image
try:
    logo_image = Image.open(
        r"C:\Users\JANREY\OneDrive\Desktop\pngkey.com-phillies-logo-png-528919.png"
    )  # Replace with your logo image path
    logo_image = logo_image.resize((90, 90), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(header, image=logo_photo, bg=style["bg_color"])
    logo_label.image = logo_photo
    logo_label.place(x=10, y=5)

    # Adding a symmetric icon on the other end
    right_logo_label = tk.Label(header, image=logo_photo, bg=style["bg_color"])
    right_logo_label.image = logo_photo
    right_logo_label.place(
        x=1535 - 90 - 10, y=5
    )  # Corrected to 800 - icon_width - padding
except FileNotFoundError:
    print("Error: Logo image not found. Please check the file path.")

# Adding text to the header
university_label = tk.Label(
    header,
    text="Polytechnic University of the Philippines",
    fg=style["text_color"],
    bg=style["bg_color"],
    font=("Arial", 16, "bold"),
)
university_label.place(relx=0.5, y=10, anchor="n")

library_label = tk.Label(
    header,
    text="LIBRARY",
    fg=style["text_color"],
    bg=style["bg_color"],
    font=("Arial", 14, "bold"),
)
library_label.place(relx=0.5, y=40, anchor="n")

# Buttons Frame below header
button_frame = tk.Frame(root, bg=style["bg_color"], height=50)
button_frame.pack(fill="x")

# Load icon images
try:
    home_icon = Image.open(r"C:\Users\JANREY\OneDrive\Desktop\home.png")
    home_icon = home_icon.resize((30, 30), Image.LANCZOS)  # Adjust size as needed
    home_icon_photo = ImageTk.PhotoImage(home_icon)

    my_books_icon = Image.open(r"C:\Users\JANREY\OneDrive\Desktop\my books.jpg")
    my_books_icon = my_books_icon.resize(
        (30, 30), Image.LANCZOS
    )  # Adjust size as needed
    my_books_icon_photo = ImageTk.PhotoImage(my_books_icon)

    readerboards_icon = Image.open(r"C:\Users\JANREY\OneDrive\Desktop\readerboards.jpg")
    readerboards_icon = readerboards_icon.resize(
        (30, 30), Image.LANCZOS
    )  # Adjust size as needed
    readerboards_icon_photo = ImageTk.PhotoImage(readerboards_icon)

    # Home Button
    home_button = tk.Button(
        button_frame,
        image=home_icon_photo,
        command=lambda: print("Home button clicked"),
        bg=style["button_color"],
        fg=style["button_text_color"],
        font=style["button_font"],
    )
    home_button.image = home_icon_photo  # Keep a reference
    home_button.pack(side="left", padx=10, pady=5)

    # My Books Button
    my_books_button = tk.Button(
        button_frame,
        image=my_books_icon_photo,
        command=lambda: print("My Books button clicked"),
        bg=style["button_color"],
        fg=style["button_text_color"],
        font=style["button_font"],
    )
    my_books_button.image = my_books_icon_photo  # Keep a reference
    my_books_button.pack(side="left", padx=5, pady=5)

    # Readerboards Button
    readerboards_button = tk.Button(
        button_frame,
        image=readerboards_icon_photo,
        command=lambda: print("Readerboards button clicked"),
        bg=style["button_color"],
        fg=style["button_text_color"],
        font=style["button_font"],
    )
    readerboards_button.image = readerboards_icon_photo  # Keep a reference
    readerboards_button.pack(side="left", padx=5, pady=5)

except FileNotFoundError:
    print("Error: Icon image not found. Please check the file paths.")

# Load background image
try:
    background_image = Image.open(
        r"C:\Users\JANREY\OneDrive\Desktop\output-onlinepngtools.png"
    )  # Replace with your background image path
    background_image = background_image.resize(
        (800, 450), Image.LANCZOS
    )  # Adjust the height to fit below button_frame
    background_photo = ImageTk.PhotoImage(background_image)
    # Content Frame
    content = tk.Frame(root)
    content.pack(fill="both", expand=True)

    # Background Image Label
    background_label = tk.Label(content, image=background_photo)
    background_label.image = background_photo  # Keep a reference
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Overlay Frame
    overlay = tk.Frame(content, bg="black")
    overlay.place(x=0, y=0, relwidth=1, relheight=1)

except FileNotFoundError:
    print("Error: Background image not found. Please check the file path.")

# Run the application
root.mainloop()
