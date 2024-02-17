import tkinter as tk
import threading
import time

class TypingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing App")

        self.text_entry = tk.Text(self.master, height=10, width=40)
        self.text_entry.pack(pady=10)

        self.typing_thread = None
        self.last_typing_time = None

        # self.start_typing_thread()

def main():
    root = tk.Tk()
    app = TypingApp(root)
    app.text_entry.bind('<Key>', app.on_typing)
    root.mainloop()

    if __name__ == "__main__":
        main()