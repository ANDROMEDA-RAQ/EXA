import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def browse_file():
    filename = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")]
    )
    if filename:
        file_label.config(text=filename)


def select_icon(event):
    # Assuming 'event.widget' gives us the Label that was clicked
    global selected_icon
    selected_icon = event.widget.cget("image")
    print(f"Selected icon: {selected_icon}")  # For debugging


def ok_action():
    if selected_icon:
        print(f"Confirmed icon: {selected_icon}")  # For debugging
        # Here you would handle what to do with the selected icon (e.g., use it, save it)
    else:
        print("No icon selected")


# Main window
root = tk.Tk()
root.title("Picture Upload")
root.configure(bg="maroon")

# Frame for upload section
upload_frame = tk.Frame(root, bg="maroon")
upload_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

# Label for upload section
tk.Label(upload_frame, text="Picture:", bg="maroon", fg="white").grid(
    row=0, column=0, sticky="w"
)

# Entry and Browse button
file_entry = tk.Entry(upload_frame, borderwidth=5, width=50)
file_entry.grid(row=1, column=0, sticky="w", padx=5, pady=5)
browse_button = tk.Button(upload_frame, text="Browse...", command=browse_file)
browse_button.grid(row=1, column=1, sticky="e")

# File selected label
file_label = tk.Label(root, text="", bg="maroon", fg="white")
file_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

# Instructions
instructions_label = tk.Label(
    root,
    text="Your virtual face or picture. Maximum dimensions are 85x85 and the maximum size is 30 kB.",
    bg="maroon",
    fg="white",
)
instructions_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

# Frame for icons
icon_frame = tk.Frame(root, bg="maroon")
icon_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

# Configure the root to allow the icon_frame to expand
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

# Label for icon selection
tk.Label(icon_frame, text="Or simply select an icon:", bg="maroon", fg="white").grid(
    row=0, column=0, columnspan=4, sticky="w"
)

# Icons
icons = [
    "Images\\avatar1.png",
    "Images\\avatar2.png",
    "Images\\avatar3.png",
    "Images\\avatar4.png",
    "Images\\avatar6.png",
    "Images\\avatar7.png",
    "Images\\avatar8.png",
    "Images\\avatar9.png",
]

selected_icon = None  # To store the selected icon

# Display icons
for i, icon in enumerate(icons):
    try:
        img = Image.open(icon)
        img = img.resize((85, 85), Image.LANCZOS)  # Resize to 85x85
        tk_image = ImageTk.PhotoImage(img)

        # Create a label to display the image, now selectable
        icon_label = tk.Label(
            icon_frame, image=tk_image, borderwidth=2, relief="groove", bg="maroon"
        )
        icon_label.image = tk_image  # Keep a reference to prevent garbage collection
        icon_label.grid(row=(i // 4) + 1, column=i % 4, padx=5, pady=5, sticky="nsew")
        icon_label.bind("<Button-1>", select_icon)  # Bind left click to select icon

        # Configure rows and columns to expand
        icon_frame.grid_rowconfigure((i // 4) + 1, weight=1)
        icon_frame.grid_columnconfigure(i % 4, weight=1)
    except Exception as e:
        print(f"Error loading image {icon}: {e}")
        # If image loading fails, use a placeholder text
        icon_label = tk.Label(
            icon_frame,
            text=f"Error: {icon}",
            borderwidth=2,
            relief="groove",
            width=10,
            height=5,
            bg="maroon",
            fg="white",
        )
        icon_label.grid(row=(i // 4) + 1, column=i % 4, padx=5, pady=5, sticky="nsew")

# Ok Button
ok_button = tk.Button(root, text="Ok", command=ok_action, bg="maroon", fg="white")
ok_button.grid(row=4, column=0, pady=10)

root.mainloop()
