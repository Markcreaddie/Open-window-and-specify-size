import tkinter as tk


def get_size():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    return screen_width, screen_height


if __name__ == "__main__":
    get_size()
