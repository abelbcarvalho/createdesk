from src.com.bcarsoft.view.CreateDesk import CreateDesk
from tkinter import Tk

def main():
    root = Tk()
    root.title('Create Desktop Icon')
    CreateDesk(root)
    root.resizable(width=False, height=False)
    # center the window
    root.withdraw()
    root.update_idletasks()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x, y))
    root.deiconify()
    # end center the window
    root.mainloop()

if __name__ == '__main__':
    main()
