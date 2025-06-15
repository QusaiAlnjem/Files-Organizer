import os
import sys
import shutil
import webbrowser
import filecmp
import hashlib
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from send2trash import send2trash
from numpy import random

def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and PyInstaller .exe """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class FilesOrganierGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self._set_appearance_mode('dark')
        self.title("Files Organizer Software")
        self.geometry("900x650")
        self.icon_path = resource_path(r"images\\main-icon.ico")
        self.iconbitmap(self.icon_path)
        
        # images
        play = Image.open(resource_path(r"images\\play.png"))
        self.play = ctk.CTkImage(light_image = play)
        options = Image.open(resource_path(r"images\\justified.png"))
        self.options = ctk.CTkImage(light_image=options, size=(45,45))
        questions = Image.open(resource_path(r"images\\qa.png"))
        self.questions = ctk.CTkImage(light_image=questions, size=(45,45))
        close = Image.open(resource_path(r"images\\cross.png"))
        self.close = ctk.CTkImage(dark_image=close,size=(27,27))

        self.dark_theme = Image.open(resource_path(r"images\\dark-image.jpg"))
        self.blue_theme = Image.open(resource_path(r"images\\blue-image.jpg"))
        
        insta = Image.open(resource_path(r"images\\instagram.png"))
        self.insta = ctk.CTkImage(dark_image=insta,size=(38,38))
        tiktok = Image.open(resource_path(r"images\\tik-tok.png"))
        self.tiktok = ctk.CTkImage(dark_image=tiktok,size=(40,40))
        youtube = Image.open(resource_path(r"images\\youtube.png"))
        self.youtube = ctk.CTkImage(dark_image=youtube,size=(40,40))
        github = Image.open(resource_path(r"images\\github.png"))
        self.github = ctk.CTkImage(dark_image=github,size=(40,40))
        linkedin = Image.open(resource_path(r"images\\linkedin.png"))
        self.linkedin = ctk.CTkImage(dark_image=linkedin,size=(39,39))

        self.pages = {}
        self.create_pages()
        self.show_page("welcome")

    def create_pages(self):
        """ ********************* FIRST PAGE FRAME ********************* """  
        self.pages["welcome"] = ctk.CTkFrame(self)

        # Grid Layout
        self.pages["welcome"].columnconfigure((0,1,2), weight=1, uniform='a')
        self.pages["welcome"].rowconfigure((0,1,2,3,4,5,6,7,8), weight=1, uniform='a')
        # Background
        self.background_canvas = tk.Canvas(self.pages["welcome"],bd=0, highlightthickness=0, relief='ridge')
        self.background_canvas.grid(column=0, columnspan=3, row=0, rowspan=9, sticky='nsew')
        self.background_canvas.bind('<Configure>', self.stretch_background)
        # Frames
        self.middle_frame = tk.Canvas(self.pages["welcome"],bd=0,background='#141417',
                                          highlightthickness=0,relief='ridge')
        self.top_frame = ctk.CTkFrame(self.pages["welcome"],corner_radius=0,
                                        bg_color='#141417',fg_color='#141417')

        # --- Middle Frame Items --- #
        self.welcome_message = ctk.CTkLabel(self.middle_frame,text="Welcome!🤩",
                                            text_color='#fa1684',font=ctk.CTkFont("Arial", 20, 'bold'))
        self.username_message = ctk.CTkLabel(self.middle_frame,text="👤Username",
                                            text_color='#3460d9',font=ctk.CTkFont("Arial", 17))
        self.username_entry = ctk.CTkEntry(self.middle_frame,200,25,15,1,
                                           border_color='#fa1684',
                                           fg_color='#3460d9',
                                           bg_color='#141417')
        self.password_message = ctk.CTkLabel(self.middle_frame,text="🔒Password",
                                            text_color='#3460d9',font=ctk.CTkFont("Arial", 17))
        self.password_entry = ctk.CTkEntry(self.middle_frame,200,25,15,1,
                                           border_color='#fa1684',
                                           fg_color='#3460d9',
                                           bg_color='#141417')
        self.login_button = ctk.CTkButton(self.middle_frame, 65, 35, 20,1,
                                         text="Login🔑",
                                         font=ctk.CTkFont("Arial", 18),
                                         border_color='#fa1684',
                                         fg_color='#3460d9',
                                         bg_color='#141417',
                                         command=self.show_main_page)
        # Page Layout
        self.top_frame.grid(column=0, columnspan=3, row=0, sticky='nsew')
        self.middle_frame.grid(column=1, row=2, rowspan=4, sticky='nsew')
        #------------ PACKING ON THE SCREEN ------------#
        self.welcome_message.pack(padx=5,pady=15,side='top',anchor='nw')
        self.username_message.pack(padx=5,pady=10,side='top',anchor='nw')
        self.username_entry.pack(padx=5,side='top',anchor='nw')
        self.password_message.pack(padx=5,pady=10,side='top',anchor='nw')
        self.password_entry.pack(padx=5,side='top',anchor='nw')
        self.login_button.pack(padx=5,pady=25,side='top',anchor='nw')

        # --- Top Frame Items --- #
        self.follow = ctk.CTkLabel(self.top_frame,text="Follow Me On",
                                   text_color='#3460d9',font=ctk.CTkFont("Arial", 23))
        self.insta_button = ctk.CTkButton(self.top_frame,0,0,image=self.insta,fg_color='#141417',
                                          text='',command=lambda: self.open_link(self.insta_button))
        self.tiktok_button = ctk.CTkButton(self.top_frame,0,0,image=self.tiktok,fg_color='#141417',
                                          text='',command=lambda: self.open_link(self.tiktok_button))
        self.youtube_button = ctk.CTkButton(self.top_frame,0,0,image=self.youtube,fg_color='#141417',
                                          text='',command=lambda: self.open_link(self.youtube_button))
        self.github_button = ctk.CTkButton(self.top_frame,0,0,image=self.github,fg_color='#141417',
                                          text='',command=lambda: self.open_link(self.github_button))
        self.linkedin_button = ctk.CTkButton(self.top_frame,0,0,image=self.linkedin,fg_color='#141417',
                                          text='',command=lambda: self.open_link(self.linkedin_button))
        #------------ PACKING ON THE SCREEN ------------#
        self.follow.pack(padx=50, side='left')
        self.insta_button.pack(padx=50, side='left')
        self.tiktok_button.pack(side='left')
        self.youtube_button.pack(padx=50, side='left')
        self.github_button.pack(side='left')
        self.linkedin_button.pack(padx=50, side='left')

        """ ********************* SECOND PAGE FRAME ********************* """
        self.pages["main"] = ctk.CTkFrame(self)
        # Grid Layout
        self.pages["main"].columnconfigure((0,1,2,3,4), weight=1, uniform='a')
        self.pages["main"].rowconfigure((0,1,2,3,4,5,6,7), weight=1, uniform='a')
        # Background
        self.page2_background_canvas = tk.Canvas(self.pages["main"],bd=0, highlightthickness=0, relief='ridge')
        self.page2_background_canvas.grid(column=0, columnspan=5, row=0, rowspan=8, sticky='nsew')
        self.page2_background_canvas.bind('<Configure>', self.page2_stretch_background)

        # ------- Animated Panels -------- #
        self.right_panel = SlidePanel(self.page2_background_canvas, 0.05, 1, x=0.52,
                                       fg_color='#003054', bg_color='#005ea8')
        self.left_panel = SlidePanel(self.page2_background_canvas, 0.05, 1, x=0.18,
                                      fg_color='#003054', bg_color='#005ea8')
        #------------------------------------------------------------#
        # RIGHT PANEL ITEMS *Paths*
        self.options_button = ButtonAnimation(self.page2_background_canvas, 'right', 1, 0.935,
                                            width=0,height=0,image=self.options,text='',fg_color="#005ea8",
                                            command=lambda: [self.right_panel.animate_up(),self.options_button.hide()])
        self.close_button_right = ctk.CTkButton(self.right_panel,0,0,image=self.close,text='',fg_color='#003054',
                                            command=lambda: [self.right_panel.animate_down(), self.options_button.show()])
        self.close_button_right.pack(padx=2, pady=2, side='top', anchor='ne')
        
        #-------------------------------------------------------------------------- #
        # ------------------------ FOLDERS & FILES ENTRIES ------------------------ #
        #-------------------------------------------------------------------------- #
        self.title_main_monitored_folder = ctk.CTkLabel(self.right_panel, height=0,
                                            text="Main Folder To Organize",
                                            text_color='#02a5f0',
                                            font=ctk.CTkFont("Arial", 16, 'bold'))
        self.main_monitored_folder = ctk.CTkEntry(self.right_panel, 200,28,15,0, fg_color='#005ea8',bg_color='#003054', 
                                                  placeholder_text="Example: \"C:\\Users\\HP\\Downloads\"",
                                                  placeholder_text_color='grey',
                                                  font=ctk.CTkFont("Arial", 12, 'bold'))
        self.title_picturesfile = ctk.CTkLabel(self.right_panel, height=0,
                                            text="Pictures Folder",
                                            text_color='#02a5f0',
                                            font=ctk.CTkFont("Arial", 16, 'bold'))
        self.picturesfile = ctk.CTkEntry(self.right_panel, 200,28,15,0, fg_color='#005ea8',bg_color='#003054', 
                                                  placeholder_text="Example: \"C:\\Users\\HP\\Pictures\"",
                                                  placeholder_text_color='grey',
                                                  font=ctk.CTkFont("Arial", 12, 'bold'))
        self.title_musicfile = ctk.CTkLabel(self.right_panel, height=0, text="Sounds Files Folder",
                                            text_color='#02a5f0', font=ctk.CTkFont("Arial", 16, 'bold'))
        self.musicfile = ctk.CTkEntry(self.right_panel, 200,28,15,0, fg_color='#005ea8',bg_color='#003054', 
                                                  placeholder_text="Example: \"C:\\Users\\HP\\Music\"",
                                                  placeholder_text_color='grey',
                                                  font=ctk.CTkFont("Arial", 12, 'bold'))
        self.title_videosfile = ctk.CTkLabel(self.right_panel, height=0, text="Videos Folder",
                                            text_color='#02a5f0', font=ctk.CTkFont("Arial", 16, 'bold'))
        self.videosfile = ctk.CTkEntry(self.right_panel, 200,28,15,0, fg_color='#005ea8',bg_color='#003054', 
                                                  placeholder_text="Example: \"C:\\Users\\HP\\Videos\"",
                                                  placeholder_text_color='grey',
                                                  font=ctk.CTkFont("Arial", 12, 'bold'))
        self.title_documentsfile = ctk.CTkLabel(self.right_panel, height=0, text="Documents Folder",
                                            text_color='#02a5f0', font=ctk.CTkFont("Arial", 16, 'bold'))
        self.documentsfile = ctk.CTkEntry(self.right_panel, 200,28,15,0, fg_color='#005ea8',bg_color='#003054', 
                                                  placeholder_text="Example: \"C:\\Users\\HP\\Documents\"",
                                                  placeholder_text_color='grey',
                                                  font=ctk.CTkFont("Arial", 12, 'bold'))
        self.submit_button = ctk.CTkButton(self.right_panel, 65, 30, 8, fg_color='#0283bf',
                                         text="Submit",font=ctk.CTkFont("Arial", 20, 'bold'),
                                         command=self.calling_control)
        self.run_button = ctk.CTkButton(self.right_panel, 65, 30, 8, fg_color='#0283bf',
                                         text="Run",image=self.play,state='disabled',
                                         font=ctk.CTkFont("Arial", 20, 'bold'),
                                         command=self.show_loading_page)
        #------------ PACKING ON THE SCREEN ------------#
        self.title_main_monitored_folder.pack(side='top', anchor='n')
        self.main_monitored_folder.pack(pady=15, side='top', anchor='n')
        #-----------------------------------------
        self.title_picturesfile.pack(pady=15, side='top', anchor='n')
        self.picturesfile.pack(side='top', anchor='n')
        #-----------------------------------------
        self.title_musicfile.pack(pady=15, side='top', anchor='n')
        self.musicfile.pack(side='top', anchor='n')
        #-----------------------------------------
        self.title_videosfile.pack(pady=15, side='top', anchor='n')
        self.videosfile.pack(side='top', anchor='n')
        #-----------------------------------------
        self.title_documentsfile.pack(pady=15, side='top', anchor='n')
        self.documentsfile.pack(side='top', anchor='n')
        #-----------------------------------------
        self.submit_button.pack(pady=30, side='top', anchor='n')
        self.run_button.pack(side='top', anchor='n')
        #---------------------------------------------------------------------------------------
        # LEFT PANEL ITEMS *Instructions*
        self.questions_button = ButtonAnimation(self.page2_background_canvas, 'left', 0, 0.07,
                                            width=0,height=0,image=self.questions,text='',fg_color="#003054",
                                            command=lambda: [self.left_panel.animate_up(),self.questions_button.hide()])
        self.close_button_left = ctk.CTkButton(self.left_panel,0,0,image=self.close,text='',fg_color='#003054',
                                            command=lambda: [self.left_panel.animate_down(), self.questions_button.show()])
        self.close_button_left.pack(padx=2, pady=2, side='top', anchor='nw')

        self.how_to_use = ctk.CTkLabel(self.left_panel, text_color='white', font=ctk.CTkFont("Arial", 15, 'bold'),
                                       text='💡How To Use?')
        self.description1 = ctk.CTkLabel(self.left_panel, text_color='white', font=ctk.CTkFont("Arial", 14),
                                       text='Copy the path of the required folder and\npaste it in the blank, For instance,\n"Main Folder To Organize"\ntells you to give him the path of\nthe folder that you want to organize\nthen enter the paths where you want\nto store the files in, for example\nin "Pictures Folder" enter the path of the\nfolder where you want to store\npictures in such as .jpg .png\n\nAfter filling all the blanks click\nsubmit to make sure the paths\nare valid to use, then run to begin.')
        self.what = ctk.CTkLabel(self.left_panel, text_color='white', font=ctk.CTkFont("Arial", 15, 'bold'),
                                       text='💭What Is Path?')
        self.description2 = ctk.CTkLabel(self.left_panel, text_color='white', font=ctk.CTkFont("Arial", 14),
                                       text='Path is the location of the file in the\ncomputer that shows the directories\nthat contain the file, path = location.\n\nYou can find the path of directory\nby clicking "right click" on the\ndirectory, then click "copy as path"\nThat\'s It!')
        self.how_to_use.pack(padx=3,pady=3,side='top', anchor='nw')
        self.description1.pack(padx=3,pady=5,side='top', anchor='nw')
        self.what.pack(padx=3,pady=5,side='top', anchor='nw')
        self.description2.pack(padx=3,pady=2,side='top', anchor='nw')
        #---------------------------------------------------------------------------------------
        """ ********************* THIRD PAGE FRAME ********************* """
        self.pages["loading"] = ctk.CTkFrame(self)
        self.updated_text = ''
        self.program_log = ctk.CTkScrollableFrame(self.pages["loading"],850,790,label_text='Operations Applied')
        self.loglab = ctk.CTkLabel(self.program_log, font=ctk.CTkFont("Arial", 17, 'bold'), text=self.updated_text)
        self.note = ctk.CTkLabel(self.pages["loading"], text="for a better view\nmaximize the screen", font=ctk.CTkFont("Arial", 22, 'bold'))
        
        self.note.place(relx=0.005, rely=0.05, anchor='nw')
        self.program_log.place(relx=0.5,rely=0.5, anchor='c')
        self.loglab.pack(side='top')
#-----------------------------------------------------------------------------------------------------#
    def open_link(self,button):
        if button == self.insta_button:
            url = "https://www.instagram.com/qusainjeim"
        elif button == self.tiktok_button:
            url ="https://www.tiktok.com/@q.us1"
        elif button == self.youtube_button:
            url = "https://www.youtube.com/@q.us1"
        elif button == self.github_button:
            url = "https://github.com/QusaiAlnjem"
        elif button == self.linkedin_button:
            url = "https://www.linkedin.com/in/qusaialnjem"
        webbrowser.open(url)

    def stretch_background(self, event):
        # size
        width = event.width
        height = event.height

        resized_image = self.dark_theme.resize((width,height))
        self.resized_tk = ImageTk.PhotoImage(resized_image)
        self.background_canvas.create_image(0,0,image=self.resized_tk,anchor='nw')
    
    def page2_stretch_background(self, event):
        # size
        width = event.width
        height = event.height

        resized_image = self.blue_theme.resize((width,height))
        self.resized_tk2 = ImageTk.PhotoImage(resized_image)
        self.page2_background_canvas.create_image(0,0,image=self.resized_tk2,anchor='nw')

    def calling_control(self):
        folders = self.check_validity()
        self.BACKEND = Organizer_BackEnd(folders)

    def check_validity(self):
        self.entries = [self.main_monitored_folder.get().replace('"',''),self.picturesfile.get().replace('"',''),self.musicfile.get().replace('"',''),self.videosfile.get().replace('"',''),self.documentsfile.get().replace('"','')]
        valid = [i for i in self.entries if os.path.exists(i)]
        unvalid = [i for i in self.entries if not os.path.exists(i)]

        if len(valid) == 5:
            self.submit_button.configure(text='All Are Valid✅',state='disabled')
            self.main_monitored_folder.configure(state='disabled')
            self.picturesfile.configure(state='disabled')
            self.musicfile.configure(state='disabled')
            self.videosfile.configure(state='disabled')
            self.documentsfile.configure(state='disabled')
            self.run_button.configure(state='normal')
            return valid
        else:
            unvalid = '\n'.join(unvalid)
            self.submit_button.configure(text='Not Valid❌', text_color='#b80e06', state='disabled')
            self.warning_frame = ctk.CTkFrame(self.page2_background_canvas,corner_radius=0, fg_color='#b80e06')
            self.warning_message = ctk.CTkLabel(self.warning_frame, text_color='white',
                                                text=f"The following paths are not valid:\n{unvalid}",
                                                font=ctk.CTkFont("Arial", 14, 'bold'))
            self.warning_message.pack(side='top')
            self.warning_frame.place(relx=0.5,rely=0, anchor='n')
            self.warning_frame.after(5000,self.remove_warning_frame)

    def remove_warning_frame(self):
        self.warning_frame.destroy()  # Destroy the frame to remove it
        self.submit_button.configure(text='Submit', text_color='white', state='normal')
    
    def update(self, add):
        self.updated_text += add + '\n'
        self.loglab.configure(text=self.updated_text)

    def show_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()
        self.pages[page_name].pack(fill=tk.BOTH, expand=True)
    
    def show_main_page(self):
        self.show_page("main")
    
    def show_loading_page(self):
        self.show_page("loading")
        self.BACKEND.functions_player()

class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos, x, **kwargs):
        super().__init__(parent, **kwargs)
        self.x = x
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.master = parent
        self.pos = self.start_pos
        self.in_start_pos = True
        self.switch = True

        self.place(relx=self.x, rely=self.start_pos, relwidth=0.3, relheight=0.9, in_=self.master)
 
    def animate_up(self):
        if self.pos > self.start_pos and self.in_start_pos == False:
            self.pos -= 0.017
            self.place(relx=self.x, rely=self.pos, relwidth=0.3, relheight=0.9, in_=self.master)
            self.after(10,self.animate_up)
        else:
            self.in_start_pos = True
    
    def animate_down(self):
        if self.pos < self.end_pos and self.in_start_pos == True:
            self.pos += 0.017
            self.place(relx=self.x, rely=self.pos, relwidth=0.3, relheight=0.9, in_=self.master)
            self.after(10,self.animate_down)
        else:
            self.in_start_pos = False


class ButtonAnimation(ctk.CTkButton):
    def __init__(self, master, side, ixpos, fxpos, **kwargs):
        super().__init__(master, **kwargs)
        self.initial_xpos = ixpos
        self.final_xpos = fxpos
        self.side = side
        self.pos = self.initial_xpos

        if self.side == 'right':
            self.place(relx=self.initial_xpos, rely=0.02, anchor='nw')
        if self.side == 'left':
            self.place(relx=self.initial_xpos, rely=0.02, anchor='ne')
    
    def show(self):
        if self.pos > self.final_xpos and self.side == 'right':
            self.pos -= 0.0013
            self.place(relx=self.pos, rely=0.02, anchor='nw')
            self.after(10,self.show)
        
        if self.pos < self.final_xpos and self.side == 'left':
            self.pos += 0.0013
            self.place(relx=self.pos, rely=0.02, anchor='ne')
            self.after(10,self.show)
        
    def hide(self):
        if self.pos < self.initial_xpos and self.side == 'right':
            self.pos += 0.0013
            self.place(relx=self.pos, rely=0.02, anchor='nw')
            self.after(10,self.hide)

        if self.pos > self.initial_xpos and self.side == 'left':
            self.pos -= 0.0013
            self.place(relx=self.pos, rely=0.02, anchor='ne')
            self.after(10,self.hide)
        

class Organizer_BackEnd():
    def __init__(self, folders:list):
        self.it = 0   # it represent the calling number of a function to handle the files transfer
        self.main_folder = folders[0]
        self.pictures = folders[1]
        self.sounds = folders[2]
        self.videos = folders[3]
        self.documents = folders[4]
        self.extensions_dest = {
        ".exe": self.documents,
        ".msi": self.documents,
        ".txt": self.documents,
        ".vtt": self.documents,
        ".srt": self.documents,
        ".pdf": self.documents,
        ".pptx": self.documents,
        ".docx": self.documents,
        ".accdb": self.documents,
        ".pub": self.documents,
        ".csv": self.documents,
        ".xlsx": self.documents,
        ".html": self.documents,
        ".sql": self.documents,
        ".psd": self.documents,
        ".aep": self.documents,
        ".ai": self.documents,
        ".mov": self.videos,
        ".mp4": self.videos,
        ".avi": self.videos,
        ".png": self.pictures,
        ".jpg": self.pictures,
        ".jpeg": self.pictures,
        ".gif": self.pictures,
        ".mp3":self.sounds,
        ".wav":self.sounds,
        ".zip":"extract",
        ".tar":"extract",
        ".gz":"extract",
        ".xz":"extract",
        ".bz2":"extract"
    }
    
    def functions_player(self):
        APP.update(f"\nOrganizing Directory: {self.main_folder}\n")
        self.extract_file(self.main_folder)
        self.find_duplicate_files(self.main_folder)
        APP.update("\n Modifying And Moving Files...\n")
        self.Modify(self.main_folder, self.it)
        APP.update("\nOrganizing Process Has Finished.")
    
    def all_directories(self, directory:str) -> list:
        directories = []
        for root , dirs , _ in os.walk(directory):
            for dir in dirs:
                dir = os.path.join(root , dir)
                directories.append(dir)
        
        return directories

    def all_files(self, directory:str) -> list:
        Files = []
        for root , _ , files in os.walk(directory):
            for f in files:
                f = os.path.join(root , f)
                Files.append(f)
        
        return Files

    def find_duplicate_files(self, directory:str) -> None:
        
        all_dirs = self.all_directories(directory)
        
        """ We want to avoid the directories that contains .exe files
            because in most cases the directory(contains .exe file)
            will contain an important files to execute a program.
            so, our code will check for .exe files in a directory """
        
        dirs_to_remove = set() # a set to store the directories to avoid

        for D in all_dirs:
            for _, _, files in os.walk(D): 
                if any(file.endswith(".exe") for file in files):
                    dirs_to_remove.add(D)
                    break  # Stop checking this directory once we find a .exe file

        all_dirs = [D for D in all_dirs if not any(D.startswith(dr) # avoid any element that starts with any of
                                        for dr in dirs_to_remove)]  # dirs_to_remove elements(to avoid subdirectories)
        """-----------------------------------------------------------------------------"""
        APP.update("Searching For Duplicate Folders...")

        check_duplicates = True # it's true if we want to check duplicates for this path

        checked_dirs = []  # directories already checked or being checked
        send2trash_directories = [] # directories to remove
        dir_count_checked = 0 # how many directories we checked so far in the loop?
        loop = True 
        if all_dirs:
            while loop:
                for current_dir in all_dirs: # loop on all_dirs
                    if check_duplicates and current_dir not in checked_dirs:
                        checked_dirs.append(current_dir) # add the dir to the checked dirs
                        check_duplicates = False # set to false to starts checking for our dir
                    elif not check_duplicates: # if check_duplicates == False
                        # Compare directories
                        check = filecmp.dircmp(checked_dirs[-1], current_dir)
                        common = len(check.common_files) # find the lengths of the common files 
                        left = len(check.left_list)      # to check if the dir is fully copied
                        right = len(check.right_list)    
                        if common in (left , right) and common != 0:
                            APP.update("Duplicates Found!")
                            if checked_dirs[-1] not in send2trash_directories and os.path.exists(current_dir):
                                send2trash_directories.append(checked_dirs[-1])
                                APP.update(f"{checked_dirs[-1]} Removed\n")
                            else:
                                send2trash_directories.append(current_dir)
                                APP.update(f"{current_dir} Removed\n")

                check_duplicates = True # after checking for the first dir, set to true to start checking the next one
                dir_count_checked += 1
                if dir_count_checked == len(all_dirs): # break the loop if we finished all dirs
                    loop = False
        
            for d in send2trash_directories:
                send2trash(d)
    #------------------------------------------------------------------------------------#
        APP.update("Searching For Duplicate Files...")
        filtered_files = self.all_files(directory)
        filtered_files = [f for f in filtered_files if not any(f.startswith(dr) 
                                    for dr in dirs_to_remove)] 
        checked_files = []
        send2trash_files = []
        file_count_checked = 0
        loop = True
        if filtered_files:
            while loop:
                for current_file in filtered_files: # loop on filtered_files
                    if check_duplicates and current_file not in checked_files:
                        checked_files.append(current_file) 
                        check_duplicates = False 
                    elif not check_duplicates and os.path.basename(current_file)!="desktop.ini": # if check_duplicates == False
                        # Compare files
                        current_file_hash = hashlib.md5(open(current_file, 'rb').read(1000)).hexdigest()
                        checked_file_hash = hashlib.md5(open(checked_files[-1], 'rb').read(1000)).hexdigest()
                        if current_file_hash == checked_file_hash:
                            APP.update(f"{os.path.basename(checked_files[-1])} IS A DUPLICATE WITH {os.path.basename(current_file)}")
                            
                            send2trash_files.append(checked_files[-1])
                            APP.update(f"{checked_files[-1]} Removed\n")

                check_duplicates = True # after checking for the first dir, set to true to start checking the next one
                file_count_checked += 1
                if file_count_checked == len(filtered_files): # break the loop if we finished all dirs
                    loop = False

            for f in send2trash_files:
                send2trash(f)

        APP.update("Searching For Duplicates Process Has Finished!")

    def rename_file(self, path) -> str:
        if os.path.isdir(path):
            new_name = path + f"{random.randint(low=0 , high=9)}"
            return new_name
        elif os.path.isfile(path):
            new_name = os.path.splitext(path)[0] + f"{random.randint(low=0 , high=9)}"
            new_name = new_name + os.path.splitext(path)[1]
            return new_name
        
    def create_dir(self, path:str , name:str) -> str:
        new_path = os.path.join(path , name)
        if os.path.exists(new_path) == False:
            os.mkdir(new_path)
            APP.update(f"New directory is created: {new_path}")
            return new_path
        else:
            renamedir = self.rename_file(new_path , name)
            os.mkdir(renamedir)
            APP.update(f"New directory is created: {renamedir}")
            return renamedir

    def extract_file(self, path:str) -> None:
        loop = True
        for root,_,files in os.walk(path):
            while loop:
                for file in files:
                    file_path = os.path.join(root, file)
                    extension = os.path.splitext(file_path)[1]
                    if os.path.isfile(file_path) and self.extensions_dest.get(extension)== "extract":
                        unpacked_path = os.path.splitext(path)[0] # to store the unpacked folder
                        shutil.unpack_archive(file_path , unpacked_path)
                        send2trash(file_path) # unpacked_path become the new folder and file_path is useless now
                        APP.update(f"file {file_path} Unpacked")

                loop = False
        APP.update("Extracting Process Has Finished!\n")

    def find_destination(self, destination:str, extension:str , it:int) -> str:
        it += 1
        for entry in os.scandir(destination):
            if entry.is_dir() and not entry.is_junction(): # not is_junction used to remove the junction hidden files
                # Recursively search in subdirectories
                path , it = self.find_destination(entry.path, extension , it)
                if path:
                    it -= 1
                    return path , it
            elif entry.is_file() and os.path.splitext(entry.name)[1] == extension:
                it -= 1
                return entry.path.removesuffix("\\" + entry.name) , it
        it -= 1
        if it == 0:
            # if no dir is found, create a new one
            return self.create_dir(destination , extension.removeprefix('.'))
        else:
            return None , it
        
    def move_file(self, sourcedir:str , destdir:str) -> None:
        filename = os.path.basename(sourcedir)
        duplicate_check = os.path.join(destdir , filename)
        new_file_name = ""
        if os.path.exists(duplicate_check):
            file_size1 = os.stat(sourcedir).st_size
            file_size2 = os.stat(duplicate_check).st_size
            if file_size1 == file_size2:
                send2trash(duplicate_check)
                APP.update(f"Duplicate Found! {filename} In {destdir} Sent To Recycle Bin")
            else:
                new_file_name = self.rename_file(sourcedir)
                os.rename(sourcedir , new_file_name)
                APP.update(f"Similar Names Detected! {os.path.basename(sourcedir)} Changed To {os.path.basename(new_file_name)}")
        
        if os.path.exists(sourcedir):
            shutil.move(sourcedir, destdir)
            APP.update(f"File {filename} Moved From {sourcedir} To {destdir}")
        elif os.path.exists(new_file_name):
            shutil.move(new_file_name, destdir)
            APP.update(f"File {os.path.basename(new_file_name)} Moved From {new_file_name} To {destdir}")

    def Modify(self, maindir:str , it:int):
        it += 1 # increase for each recursive call
        if any(os.scandir(maindir)):
            with os.scandir(maindir) as dir:
                for entry in dir:
                    # Directory
                    if entry.is_dir() and not entry.is_junction():
                        dir_ext , it = self.Modify(entry.path , it) # trying to find what file extensions in the directory
                        if dir_ext:
                            it -= 1
                            if it == 1: # it = 1 means we left the subdirectories and we are in the main directory
                                destination = self.extensions_dest.get(dir_ext)
        
                                if destination == self.documents:
                                    find = self.find_destination(destination , dir_ext , 0)
                                    dest = find if len(find) > 2 else find[0]
                                    self.move_file(entry.path , dest)
                                
                                elif destination in (self.videos, self.pictures, self.sounds):
                                    self.move_file(entry.path , destination)

                                else:
                                    APP.update(f"{dir_ext} Extension Is Not Supported!")
                            else:
                                return dir_ext , it
                    # File
                    # desktop.ini is a built-in hidden file within most of the dirs that tells the dir how to behave
                    elif entry.is_file() and entry.name != 'desktop.ini':
                        if it == 1:
                            file_ext = os.path.splitext(entry.path)[1]
                            destination = self.extensions_dest.get(file_ext)
                            
                            if destination == self.documents: # i want to apply find_destination() on documents only
                                find = self.find_destination(self.documents , file_ext , 0)
                                dest = find if len(find) > 2 else find[0]
                                self.move_file(entry.path , dest)
                            
                            elif destination in (self.videos, self.pictures, self.sounds):
                                self.move_file(entry.path , destination)

                            else:
                                APP.update(f"{file_ext} Extension Is Not Supported!")
                        else:
                            return os.path.splitext(entry.path)[1] , it
        else:
            if it != 1:
                it -= 1
                send2trash(maindir)
                APP.update(f"Directory {maindir} Sent To Recycle Bin")
                return None , it # 0 instead of None
            else:
                APP.update("\nTarget Directory Is Empty!")
        
        if it != 1: # to avoid the closing of the function which leads to unpacking error (gives None)
            it -= 1
            return None , it

if __name__ == "__main__":
    APP = FilesOrganierGUI()
    APP.mainloop()
