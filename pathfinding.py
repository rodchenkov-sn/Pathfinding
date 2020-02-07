from tkinter import messagebox

from window.main_window import MainWindow


def run():
    try:
        mw = MainWindow(750, 750)
        mw.main_loop()
    except Exception as e:
        messagebox.showerror('Error', e)


if __name__ == '__main__':
    run()
