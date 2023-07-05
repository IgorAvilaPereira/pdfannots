import platform
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
from tkinter import ttk

import pdfannots
from pdfannots.cli import main_igor



class Main():
    def __init__(self):
        self.fileName = None
        self.window = Tk()
        self.window.title('GUI TKinter to pdfannots')
        self.window.resizable(0,0)
        # self.window.geometry("600x600")  

        self.menubar = Menu(self.window)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Select a PDF File", command=self.eventUpload)
        self.filemenu.add_command(label="Export Annotations", command=self.eventSaveOutput)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.eventQuit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About...", command=self.about)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.window.config(menu=self.menubar)

        # self.button1 = Button(self.window, text='Upload PDF File', command=self.eventUpload)
        # self.button2 = Button(self.window, text='Quit', command=self.eventQuit)
        # self.button3 = Button(self.window, text='Save Output', command=self.eventSaveOutput)

        self.v = Scrollbar(self.window, orient='vertical')                     
        self.textArea = Text(self.window, yscrollcommand=self.v.set)     

        if platform.system() == "Linux":
            # print("Linux")
            self.separator = "/"
        elif platform.system() == "Windows":
            # print("Windows")
            self.separator = "\\"
        else:
            # print("Mac")         
            self.separator = "/"  

    def about(self):
        messagebox.showinfo("GUI TKinter to pdfannots - About", "Developed by Igor Avila Pereira\ngithub.com/IgorAvilaPereira")

    def show(self):
        self.v.config(command=self.textArea.yview)
        self.v.pack(side=RIGHT, fill='y')   
        # self.button1.pack()         
        # self.button3.pack() 
        # self.button2.pack()         
        self.textArea.pack() 
        self.window.mainloop()

    def eventQuit(self):
        self.window.quit()

    def eventSaveOutput(self):        
        folder_selected = filedialog.askdirectory()                
        if (len(folder_selected) > 0 and self.fileName is not None):
        # if (self.fileName is not None):
            # output_file = folder_selected + '/export.md'        
            try:
                output_file = folder_selected + self.separator +self.fileName.replace(".pdf", ".md").replace(" ", "_")        
                if (len(self.textArea.get("1.0","end-1c"))>0):
                    with open(output_file, 'w') as f:
                        f.write(self.textArea.get("1.0","end-1c"))
                    messagebox.showinfo("GUI TKinter to pdfannots", "Sucess!")
                else:
                    messagebox.showwarning("GUI TKinter to pdfannots", "Please, upload a pdf file!")
            except:
                messagebox.showwarning("GUI TKinter to pdfannots", "Incorrect folder!")                
        else:
            # messagebox.showwarning("pdfannots", "Choose a folder or ")
            messagebox.showwarning("GUI TKinter to pdfannots", "Choose a folder or upload a pdf file!")

    def eventUpload(self):
        filename = filedialog.askopenfilename()        
        # print(filename)
        if (len(filename) > 0):
            extension = filename.split('.', 1)       
            vetFile = filename.split(self.separator)       
            self.fileName = vetFile[-1]    
            dir = self.separator.join(vetFile[1:-1])+self.separator
            if(extension[1] == 'pdf'):
                self.textArea.delete('1.0', END)
                messagebox.showinfo("pdfannots", "Wait....")
                try:                     
                    # print(self.separator+dir+self.fileName)
                    f = main_igor(self.separator+dir+self.fileName)
                    # print("python3 pdfannots.py "+self.separator+dir+"'"+self.fileName+"'")
                    # print(f)
                    # exit(0)             

                    # version = platform.python_version()
                    # if "3" in version:   
                    #     os.system("python3 pdfannots.py "+self.separator+dir+"'"+self.fileName+"' > "+self.fileName.replace(".pdf", ".md").replace(" ", "_"))
                    #     # print("python 3")
                    #     print("python3 pdfannots.py "+self.separator+dir+"'"+self.fileName+"' > "+self.fileName.replace(".pdf", ".md").replace(" ", "_"))
                    # else:
                    #     os.system("python pdfannots.py "+self.separator+dir+"'"+self.fileName+"' > "+self.fileName.replace(".pdf", ".md").replace(" ", "_"))                            
                    #     # print("python 2")   
                                         
                    # f = open(self.fileName.replace(".pdf", ".md").replace(" ", "_"), "r")
                    
                    # for line in f:
                    self.textArea.insert(END, f)
                        
                    # if os.path.exists(self.fileName.replace(".pdf", ".md").replace(" ", "_")):
                    #     os.remove(self.fileName.replace(".pdf", ".md").replace(" ", "_"))                
                    
                    messagebox.showinfo("GUI TKinter to pdfannots", "Sucess!")
                except:
                    messagebox.showwarning("GUI TKinter to pdfannots", "Can't open pdf file or python version not supported!")
            else:
                messagebox.showwarning("GUI TKinter to pdfannots", "Choose a PDF file")
                self.textArea.delete('1.0', END)
        # else:
        #     messagebox.showwarning("pdfannots", "Choose a file")

if __name__ == '__main__':
    window = Main()
    window.show()
