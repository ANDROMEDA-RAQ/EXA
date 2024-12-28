import tkinter as tk

root = tk.Tk()
root.geometry("500x400")
root.title("Homepage")


def hide_indicators():
    home_indicate.config(bg="#F0F0F0")
    mybooks_indicate.config(bg="#F0F0F0")
    leadearboards_indicate.config(bg="#F0F0F0")
    profile_indicate.config(bg="#F0F0F0")


def indicate(lb):
    hide_indicators()
    lb.config(bg="#158aff")


options_frame = tk.Frame(root, bg="#800000")

home_btn = tk.Button(
    options_frame,
    text="Home",
    font=("Bold", 15),
    fg="#800000",
    bd=0,
    bg="#FFD700",
    command=lambda: indicate(home_indicate),
)
home_btn.place(x=10, y=250)

home_indicate = tk.Label(options_frame, text="", bg="#F0F0F0")
home_indicate.place(x=3, y=250, width=5, height=40)

mybooks_btn = tk.Button(
    options_frame,
    text="MyBooks",
    font=("Bold", 15),
    fg="#800000",
    bd=0,
    bg="#FFD700",
    command=lambda: indicate(mybooks_indicate),
)
mybooks_btn.place(x=10, y=300)

mybooks_indicate = tk.Label(options_frame, text="", bg="#F0F0F0")
mybooks_indicate.place(x=3, y=300, width=5, height=40)

leadearboards_btn = tk.Button(
    options_frame,
    text="Readerboards",
    font=("Bold", 15),
    fg="#800000",
    bd=0,
    bg="#FFD700",
    command=lambda: indicate(leadearboards_indicate),
)
leadearboards_btn.place(x=10, y=350)

leadearboards_indicate = tk.Label(options_frame, text="", bg="#F0F0F0")
leadearboards_indicate.place(x=3, y=350, width=5, height=40)

profile_btn = tk.Button(
    options_frame,
    text="Profile",
    font=("Bold", 15),
    fg="#800000",
    bd=0,
    bg="#FFD700",
    command=lambda: indicate(profile_indicate),
)
profile_btn.place(x=10, y=400)

profile_indicate = tk.Label(options_frame, text="", bg="#F0F0F0")
profile_indicate.place(x=3, y=400, width=5, height=40)

# This will make options_frame fill the entire left side of the window vertically
options_frame.pack(side=tk.LEFT, fill=tk.Y)
options_frame.pack_propagate(False)
options_frame.configure(width=200, height=400)

main_frame = tk.Frame(root, highlightbackground="black", highlightthickness=2)

main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
main_frame.pack_propagate(False)

root.mainloop()
