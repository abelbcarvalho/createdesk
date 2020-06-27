from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from ..model.Desk import Desk
from ..facade.Facade import Facade
from tkinter import messagebox


class CreateDesk:
    font_title = ('Dialog','15','italic')
    font_normal = ('Dialog','12','normal')
    font_small = ('Dialog','11','normal')

    def __init__(self, master: None):
        # main frame
        self.frame_main = Frame(master)
        self.frame_main.pack()
        # head frame
        self.frame_head = Frame(self.frame_main)
        self.frame_head['padx'] = 70
        self.frame_head['pady'] = 20
        self.frame_head.pack(side=TOP)
        # head
        self.head_title = Label(self.frame_head, text='Create Your Desktop Launcher')
        self.head_title['font'] = self.font_title
        self.head_title.pack()
        # data part ------------------------------------------------------------------
        self.frame_data = Frame(self.frame_main)
        self.frame_data['padx'] = 70
        self.frame_data['pady'] = 4
        self.frame_data.pack()
        self.frame_open_launcher = Frame(self.frame_main)
        self.frame_open_launcher['padx'] = 70
        self.frame_open_launcher.pack()
        self.frame_open_path = Frame(self.frame_main)
        self.frame_open_path['padx'] = 70
        self.frame_open_path.pack()
        self.frame_open_icon = Frame(self.frame_main)
        self.frame_open_icon['padx'] = 70
        self.frame_open_icon.pack()
        self.frame_data1 = Frame(self.frame_main)
        self.frame_data1['padx'] = 70
        self.frame_data1.pack()
        self.frame_button = Frame(self.frame_main)
        self.frame_button['padx'] = 70
        self.frame_button['pady'] = 20
        self.frame_button.pack(side=BOTTOM)
        # lable for spinner
        self.spni_version = Label(self.frame_data,text='Version*')
        self.spni_version['font'] = self.font_normal
        self.spni_version.pack()
        # application version
        self.desk_version = Spinbox(self.frame_data,from_=1,to_=3)
        self.desk_version['font'] = self.font_normal
        self.desk_version['width'] = 29
        self.desk_version.pack()
        # label for name
        self.entry_name_label = Label(self.frame_data, text='Name*')
        self.entry_name_label['font'] = self.font_normal
        self.entry_name_label.pack()
        # application name
        self.desk_name = Entry(self.frame_data)
        self.desk_name['width'] = 30
        self.desk_name['font'] = self.font_normal
        self.desk_name.pack()
        # lable for comment
        self.entry_comment_label = Label(self.frame_data, text='Comment')
        self.entry_comment_label['font'] = self.font_normal
        self.entry_comment_label.pack()
        # application comment
        self.desk_comment = Entry(self.frame_data)
        self.desk_comment['width'] = 30
        self.desk_comment['font'] = self.font_normal
        self.desk_comment.pack()
        # secound part -----------------------------------------------------
        self.cmb_language_label = Label(self.frame_data, text='Select Language')
        self.cmb_language_label['font'] = self.font_normal
        self.cmb_language_label.pack()
        # application language
        self.cmb_language = ttk.Combobox(self.frame_data,width=29,textvariable=StringVar(),
                                         state="readonly")
        self.cmb_language['font'] = self.font_normal
        self.cmb_language['values'] = ('Language','Java','Python')
        self.cmb_language.current(0)
        self.cmb_language.pack()
        # laucher way
        self.entry_laucher_label = Label(self.frame_open_launcher, text='Launcher Path*')
        self.entry_laucher_label['font'] = self.font_normal
        self.entry_laucher_label.pack()
        # application launcher
        self.desk_laucher = Entry(self.frame_open_launcher)
        self.desk_laucher['font'] = self.font_normal
        self.desk_laucher['width'] = 26
        self.desk_laucher.pack(side=LEFT)
        # button for laucher
        self.btn_launch = Button(self.frame_open_launcher)
        self.btn_launch['text'] = 'Open'
        self.btn_launch['width'] = 2
        self.btn_launch['font'] = self.font_small
        self.btn_launch['pady'] = -1
        self.btn_launch['padx'] = 10
        self.btn_launch['command'] = self.open_launcher
        self.btn_launch.pack(side=LEFT)
        # directory path
        self.entry_path_label = Label(self.frame_open_path, text='Directory Path')
        self.entry_path_label['font'] = self.font_normal
        self.entry_path_label.pack()
        # application path
        self.desk_path = Entry(self.frame_open_path)
        self.desk_path['font'] = self.font_normal
        self.desk_path['width'] = 26
        self.desk_path.pack(side=LEFT)
        # button for path
        self.btn_path = Button(self.frame_open_path)
        self.btn_path['text'] = 'Open'
        self.btn_path['width'] = 2
        self.btn_path['font'] = self.font_small
        self.btn_path['pady'] = -1
        self.btn_path['padx'] = 10
        self.btn_path['command'] = self.open_path
        self.btn_path.pack(side=LEFT)
        # icon path
        self.entry_icon_label = Label(self.frame_open_icon, text='Icon Path')
        self.entry_icon_label['font'] = self.font_normal
        self.entry_icon_label.pack()
        # application icon
        self.desk_icon = Entry(self.frame_open_icon)
        self.desk_icon['font'] = self.font_normal
        self.desk_icon['width'] = 26
        self.desk_icon.pack(side=LEFT)
        # button for icon
        self.btn_icon = Button(self.frame_open_icon)
        self.btn_icon['text'] = 'Open'
        self.btn_icon['width'] = 2
        self.btn_icon['font'] = self.font_small
        self.btn_icon['pady'] = -1
        self.btn_icon['padx'] = 10
        self.btn_icon['command'] = self.open_icon
        self.btn_icon.pack(side=LEFT)
        # terminal boolean
        self.cmb_terminal_label = Label(self.frame_data1, text='Terminal*')
        self.cmb_terminal_label['font'] = self.font_normal
        self.cmb_terminal_label.pack()
        # application terminal
        self.cmb_terminal = ttk.Combobox(self.frame_data1,width=29,textvariable=StringVar(),
                                         state="readonly")
        self.cmb_terminal['font'] = self.font_normal
        self.cmb_terminal['values'] = ('Select*','True','False')
        self.cmb_terminal.current(0)
        self.cmb_terminal.pack()
        # type
        self.cmb_type_label = Label(self.frame_data1, text='Type*')
        self.cmb_type_label['font'] = self.font_normal
        self.cmb_type_label.pack()
        # application type
        self.cmb_type = ttk.Combobox(self.frame_data1,width=29,textvariable=StringVar(),
                                     state="readonly")
        self.cmb_type['font'] = self.font_normal
        self.cmb_type['values'] = ('Select*','Application')
        self.cmb_type.current(0)
        self.cmb_type.pack()
        # categories
        self.entry_categories_label = Label(self.frame_data1, text='Categories')
        self.entry_categories_label['font'] = self.font_normal
        self.entry_categories_label.pack()
        # application categories
        self.desk_categories = Entry(self.frame_data1)
        self.desk_categories['font'] = self.font_normal
        self.desk_categories['width'] = 30
        self.desk_categories.bind("<KeyRelease>", self.fix_category)
        self.desk_categories.pack()
        # frame button ---------------------------------------------------------------
        # create button
        self.btn_create = Button(self.frame_button)
        self.btn_create['text'] = 'Create'
        self.btn_create['width'] = 7
        self.btn_create['font'] = self.font_normal
        self.btn_create['command'] = self.create_desk
        self.btn_create.pack()
    
    def create_desk(self):
        """This method takes info and done the operation"""
        desk = Desk()
        facd = Facade()
        # take data
        try:
            desk.version = float(self.desk_version.get())
            desk.name = self.desk_name.get()
            desk.comment = self.desk_comment.get()
            if self.cmb_language.current() == 1:
                desk.execute = 'javac ' + self.desk_laucher.get()
            elif self.cmb_language.current() == 2:
                desk.execute = 'python3 ' + self.desk_laucher.get()
            else:
                desk.execute = self.desk_laucher.get()
            desk.icon = self.desk_icon.get()
            if self.cmb_terminal.current() == 0:
                messagebox.showerror('Error With Terminal','You Don\'t Specified Terminal')
                return
            if self.cmb_terminal.current() == 1:
                desk.terminal = 'true'
            elif self.cmb_terminal.current() == 2:
                desk.terminal = 'false'
            if self.cmb_type.current() == 0:
                messagebox.showerror('Error With Type','No Type Selected')
                return
            desk.typee = self.cmb_type.get()
            desk.categories = self.desk_categories.get()
            if facd.set_desktop_launch(desk):
                messagebox.showinfo('Success With Creation','Desktop Launcher Created')
            else:
                messagebox.showerror('Error With Creation','Desktop Launcher Not Created')
        except ValueError:
            messagebox.showerror('Invalid Data','An Error Was Found')
    
    def open_launcher(self):
        """Inserts path launcher"""
        file = askopenfilename(title="Select Executable")
        self.desk_laucher.delete(0, END)
        self.desk_laucher.insert(0, file)
    
    def open_path(self):
        """Inserts path directory"""
        file = askdirectory(title="Select Path")
        self.desk_path.delete(0, END)
        self.desk_path.insert(0, file)
    
    def open_icon(self):
        """Inserts path directory"""
        file = askopenfilename(title="Select Icon")
        self.desk_icon.delete(0, END)
        self.desk_icon.insert(0, file)
    
    def fix_category(self, event):
        """Event for checks the key released"""
        word = self.desk_categories.get()
        if not word[0].isalpha():
            self.desk_categories.delete(0, END)
            return
        word = list(word)
        for i in range(word.__len__()):
            if not word[i].isalpha() and not word[i].__eq__(';'):
                word[i] = ';'
        ct = ''
        for i in word:
            ct += i
        self.desk_categories.delete(0, END)
        self.desk_categories.insert(0, ct)
