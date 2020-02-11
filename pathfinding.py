from tkinter import messagebox

from window.main_window import MainWindow


def run():
    try:
        mw = MainWindow()
        mw.main_loop()
    except Exception as e:
        messagebox.showerror('Error', e)
    except:
        messagebox.showerror('Error', 'Unknown error occurred')


if __name__ == '__main__':
    run()
