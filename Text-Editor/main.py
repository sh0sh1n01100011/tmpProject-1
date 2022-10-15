#! usr/bin/python
'# -*- coding: utf-8 -*-'


import tkinter
import sys
import os

from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
# TODO: Fix lower line or delete it
#from PIL import Image, ImageTk

# Main class of the program
class WINDOW(Tk):
    """
    Comment:
    """

    def __init__(self, *args, **kwargs):
        """
        Comment:
        """

        Tk.__init__(self, *args, **kwargs)

        # Setting the Window obj. title with .title method
        self.title("Untitled - Text Editor")

        # Set Window obj. dimensions with .geometry method
        self.geometry('800x500')

        # Using chosen image as icon and readying it for the Text Editor
        #text_editor_icon = ImageTk.PhotoImage(Image.open('icons/editor-icon.png'))
        #iconphoto(False, text_editor_icon)

        # Setting the Resizable properties for the Window obj.
        # Main frame - resizable properties
        container = Frame(self, height=400, width=600)
        container.pack(side=TOP, fill=BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # TODO SET MIN HEIGHT AND MIN WIDTH

        # TODO Toolbar
        # Temporal frame for other functions like supporting number labels for text lines.
        shortcutbar = Frame(container, height=10, width=600, bg="light sea green")
        shortcutbar.pack(fill=X, expand=NO)

        # TODO Figure out how the hell this does work in the end.
        ln_label = Label(container, width=2, bg='red')
        ln_label.pack(side=LEFT, anchor="nw", fill=Y)

#        # TODO Numeric Frame
#        num_label = Label(container, height=24, width=2, bg="light green")
#        num_label.pack(side=LEFT, fill=Y, expand=True, anchor="nw")

        # TODO Bottom information
#        information_label = Frame(container, height=10, width=600, bg="light grey")
#        information_label.pack(side=TOP, fill=X, expand=True)

        # Section for the scrollbars and the text widget itself
        text_widget = Text(container)
        text_widget.pack(expand=YES, fill=BOTH)

        # Section for the vertical scrollbar
        vertical_scrollbar = Scrollbar(text_widget)

        # Actual implementation of the Scrollbar and Text widgets
        text_widget.configure(yscrollcommand=vertical_scrollbar.set)

        # Sets orientation of the scrollbar widget
        vertical_scrollbar.config(command=text_widget.yview)
        # Sets position of the scrollbar widget
        vertical_scrollbar.pack(side=RIGHT, fill=Y)



        # Options Menu
        options = OPTIONS(self)
        self.config(menu=options)

# TODO: Create a new class for the file explorer of the editor

class OPTIONS(Menu):

    """
    Comment:
    """


    def __init__(self, *args, **kwargs):
        """
        Comment:
        """
        Menu.__init__(self, *args, **kwargs)

        self.title = title
        # TODO Add the missing icons to all the commmand options that require it
        file_menu = Menu(self, tearoff=False)
        self.add_cascade(label="File", underline=0, menu=file_menu)
        file_menu.add_command(label="New File", accelerator='Ctrl+N', compound=LEFT,
                              underline=0, command=self.new_file)
        file_menu.add_command(label='Open File', accelerator='Ctrl+O', underline=1, command=self.open_file)
        file_menu.add_command(label="Exit", accelerator='Esc', underline=1, command=self.quit)
        file_menu.add_command(label="Save", accelerator='Ctrl+S', underline=1, command=self.quit)
        file_menu.add_command(label="Rename", accelerator='Ctrl+R', underline=1, command=self.quit)

        edit_menu = Menu(self, tearoff=False)
        self.add_cascade(label="Edit", underline=0, menu=edit_menu)
        edit_menu.add_command(label="Undo       Ctrl+Z", underline=1, command=self.format)
        edit_menu.add_command(label="Redo       Ctrl+Y", underline=1, command=self.format)
        edit_menu.add_command(label="Cut        Ctrl+X", underline=1, command=self.format)
        edit_menu.add_command(label="Copy       Ctrl+C", underline=1, command=self.format)
        edit_menu.add_command(label="Paste      Ctrl+V", underline=1, command=self.format)
        edit_menu.add_command(label="Find All   Ctrl+F", underline=1, command=self.format)
        edit_menu.add_command(label="Select All Ctrl+A", underline=1, command=self.format)


        view_menu = Menu(self, tearoff=False)
        self.add_cascade(label="View", underline=0, menu=view_menu)
        view_menu.add_checkbutton(label="Show Line Numbers", underline=1, command=self.view)
        view_menu.add_checkbutton(label="Show Information Bar at Bottom", underline=1, command=self.view)
        view_menu.add_command(label="Hightlight Current Themes", underline=1, command=self.view)
        themes_menu = Menu(view_menu, tearoff=False)
        view_menu.add_cascade(label="Themes", menu=themes_menu)
        themes_menu.add_radiobutton(label="1. Default White")
        themes_menu.add_radiobutton(label="2. Greygarious Grey")
        themes_menu.add_radiobutton(label="3. Vivacious Violet")
        themes_menu.add_radiobutton(label="4. Light Green")
        themes_menu.add_radiobutton(label="5. Solarised")
        themes_menu.add_radiobutton(label="6. Boisterous Blue")
        themes_menu.add_radiobutton(label="7. School Green")


        settings_menu = Menu(self, tearoff=False)
        self.add_cascade(label="Settings", underline=0, menu=settings_menu)
        settings_menu.add_command(label="Tools", accelerator='Ctrl+T', underline=1, command=self.view)

        help_menu = Menu(self, tearoff=False)
        self.add_cascade(label="Help", underline=0, menu=help_menu)
        help_menu.add_command(label="Questions", underline=1, command=self.settings)

        about_menu = Menu(self, tearoff=False)
        self.add_cascade(label="About", underline=0, menu=about_menu)
        about_menu.add_command(label="Author", underline=1, command=self.help)



    # TODO Add actual functionality to all the functions
    def quit(self):
        """
        Comment:
        """
        sys.exit(0)

    def open_file(self):
        """
        Function:
        Param:
        """

        file = filedialog.askopenfilename(defaultextension='.txt',
                                  filetypes=[('All Files', '*.*'),
                                             ("Text File", "*.txt*")])

        # TODO: Make text_widget be passed on to this class along with the window
        # title 'self.title = ...' in order to ive proper functionality and try to
        # apply granulanity
        if file != '':
            self.title = (f'{os.path.basename(file)}')
            text_widget.delete(1.0, END)
            with open(file, mode='r', encoding='UTF-8') as base_file:
                text_widget.insert(1.0, base_file.read())
                base_file.close()
                return

        file = None
        return


    def new_file(self):
        """
        Comment:
        """
        # TODO Fix the variable to allow the implementation of UTF-8 encoding support
        #with open('Untitled', mode='r', encoding='utf8')
        filename = 'Unititled - Text Editor'
        #with open(filename, mode='r', encoding='UTF-8') as newFile:
        self.title(f'filename')
        text_widget.delete(1.0, END)
        return text_widget.delete

    # TODO get rid of the global variable ---> text_area
    # TODO Practice the concepts of global variable and passing tkinter
    #       elements into other functions, another alternative is to try
    #       the encapsulation method, pass it around in order to practice
    #       handlig 'text_area' as an object using it as a small class
    def save_file(self):
        """
        Comment:
        """
        # TODO get rid of the global variable ---> text_area



    def copy_text(self):
        """
        Comment:
        """
        print("Copy Text")

    def cut_text(self):
        """
        Comment:
        """
        print("Cut Text")

    def paste_text(self):
        """
        Comment:
        """
        print("Paste Text")

    def select_text(self):
        """
        Comment:
        """
        print("Select Text")

    def delete_last_char(self):
        """
        Comment:
        """
        print("Delete Last Character")

    def format(self):
        """
        Comment:
        """
        print("Formatting text")

    def view(self):
        """
        Comment:
        """
        print("Viweing")

    def settings(self):
        """
        Comment:
        """
        print("display settings")

    def help(self):
        """
        Comment:
        """
        print("print help")

    def about(about):
        """
        Comment:
        """
        print("about window")

if __name__ == '__main__':
    # Figure out what each of these functions does exactly
    app = WINDOW()
    app.update()
    app.update_idletasks()
    app.mainloop()
