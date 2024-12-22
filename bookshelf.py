import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3

# Create or connect to the database
conn = sqlite3.connect("book_database.db")
c = conn.cursor()

# SQL command to create the table
create_table_sql = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    cover_path TEXT
);
"""

# Create table if it doesn't exist
c.execute(create_table_sql)
conn.commit()

# Sample data insertion - excluding the books you want to delete
books = [
    (
        "The Information Superhighway Beyond the Internet",
        "Otte,Peter",
        r"Images\the information superhighway beyond the internet.png",
    ),
    (
        "Using Microsoft Office",
        "QUE Corporation",
        r"Images\Word processing.png",
    ),
    (
        "Word Processing Applications and Living Online",
        "Rex Books",
        r"Images\Word processing.png",
    ),
]

for book in books:
    # Check if the book already exists before inserting
    c.execute(
        "SELECT id FROM books WHERE title = ? AND author = ? AND cover_path = ?", book
    )
    existing_book = c.fetchone()

    if not existing_book:
        # Insert the book only if it does not already exist in the database
        c.execute(
            "INSERT INTO books (title, author, cover_path) VALUES (?, ?, ?)", book
        )

conn.commit()


class BookDatabaseApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Database")

        # Create a canvas with a scrollbar
        self.canvas = tk.Canvas(master)
        self.scrollbar = ttk.Scrollbar(
            master, orient="vertical", command=self.canvas.yview
        )
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Bind mouse wheel to canvas for scrolling
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # Fetch and display books
        self.display_books()

    def display_books(self):
        c.execute("SELECT * FROM books")
        for book in c.fetchall():
            book_id, title, author, cover_path = book
            self.add_book_item(title, author, cover_path)

    def add_book_item(self, title, author, cover_path):
        book_frame = ttk.Frame(self.scrollable_frame, borderwidth=1, relief="solid")
        book_frame.pack(pady=5, padx=5, fill="x", expand=True)

        # Load and resize the image
        try:
            img = Image.open(cover_path)
            img = img.resize((100, 150), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
        except IOError:
            print(f"Error: Could not open image at {cover_path}")
            return

        # Display cover image
        cover_label = tk.Label(book_frame, image=photo)
        cover_label.image = photo  # Keep a reference!
        cover_label.pack(side="left")

        # Display book info
        info_frame = ttk.Frame(book_frame)
        info_frame.pack(side="left", padx=10)

        title_label = ttk.Label(info_frame, text=title, font=("Helvetica", 12, "bold"))
        title_label.pack(anchor="w")

        author_label = ttk.Label(info_frame, text=f"by {author}")
        author_label.pack(anchor="w")

    def _on_mousewheel(self, event):
        # Windows and Linux use different event attributes for mouse wheel delta
        if event.delta:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            # For Mac OS, event.num gives the direction of scroll
            if event.num == 4:
                self.canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.canvas.yview_scroll(1, "units")


if __name__ == "__main__":
    root = tk.Tk()
    app = BookDatabaseApp(root)
    root.mainloop()

    # Close the database connection when done
    conn.close()
