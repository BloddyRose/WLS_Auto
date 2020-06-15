import multiprocessing 
import tkinter as tk
from tkinter import *
import time
from tkinter import messagebox
import os
import requests
import logging
import threading
import sys
import ctypes
def main():
 
    def isAdmin():
        try:
            is_admin = (os.getuid() == 0)
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin

    def download(url: str, dest_folder: str):
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)  # create folder if it does not exist

        filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
        file_path = os.path.join(dest_folder, filename)

        r = requests.get(url, stream=True)
        if r.ok:
            print("saving to", os.path.abspath(file_path))
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
        else:  # HTTP status code 4XX/5XX
            print("Download failed: status code {}\n{}".format(r.status_code, r.text))

    def thread_function(name):
        logging.info("Thread %s: starting", name)
        time.sleep(2)
        logging.info("Thread %s: finishing", name)

    if __name__ == "__main__":
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")

        logging.info("Main    : before creating thread")
        x = threading.Thread(target=thread_function, args=(1,))
        logging.info("Main    : before running thread")
        x.start()
        logging.info("Main    : wait for the thread to finish")
        # x.join()
        logging.info("Main    : all done")



    root = tk.Tk()
    root.geometry("680x400")
    root.resizable(width = False, height = False)
    
    if isAdmin():
        mess = tk.messagebox.showinfo("ADMIN RIGHTS True YAY", "ALL Wright we can begin")
    else:
        mess = tk.messagebox.showerror(" NO YAY", "No admin rights")
        root.destroy()
        sys.exit()
        exit()
    var = """"""

    def say1():
        var = """\t---Activating Virtual Support!...Please Wait---\n
                \t---Disk Management Will Run in a second do not exit---
                \t---Virtual Machine---
            """  
        os.system("powershell dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart")
        l1.config(text=str(var))
        

    def say2():
        var = """\t---Activating WLS Support!...Please Wait---\n
                \t---Disk Management Will Run in a second do not exit---
                \t---WLS 2 ---"""  
        os.system("powershell dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart")
        time.sleep(2)
        os.system("powershell dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart && wsl --set-default-version 2")
        l1.config(text=str(var))
        

    def say3():
        var = """\t---Updating Linux Kernel !...Please Wait---\n
                 \t ---Finished---
                \t---After Downloading Go to the new folder downloads and Double click and Follow Instructions---"""  
        
        l1.config(text=str(var))
        
        time.sleep(2)
        url = "https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi"
        download("https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi", dest_folder="downloads")


        
        
    def quit():
        var = """"\t---GoodBye---" 
                    \t---Thank You---"""
        l1.config(text=str(var))


    def messshow():
        msg = tk.messagebox.showinfo("HELP MENU", """\nWLS Auto is a script for installing wls.
                                                \nIn this script or gui you have 3 buttons 
                                    \nRUN OP 1: That mens activating VM support
                                    \nRUN OP 2: That mens activating WLS Support and set WLS 2 as default!
                                    \nRUN OP 3: That mens downloading Kernel Update and open it installing is made by you
                                    \nEXIT : Exit
                                    \nABOUT : HELP Menu
                                    \n
                                    \n
                                    \tVersion : 1.0 by BloddyRose
                                    """)
    

    def About():
        msg = tk.messagebox.showinfo("About Me", """
                    \nHello User first thank you for downloading my soft if you liked please leave a star on github
                    \nGithub : https://github.com/BloddyRose/WLS_Auto 
                    \nDiscord : https://discord.gg/3aByek

                    \nPS : You can use CTRL + C to copy all of the content
                                    """)


    canvas = tk.Canvas(root, bg="#263D42")
    canvas.place(relwidth=1, relheight=1)


    b1 = tk.Button(canvas, fg="black", width=10, text="RUN OP 1 ", command = say1)
    b1.place(x=20, y=50)

    b2 = tk.Button(canvas, fg="black", width=10, text="RUN OP 2", command = say2)
    b2.place(x=20, y=100)

    b3 = tk.Button(canvas, fg="black", width=10, text="RUN OP 3", command = say3)
    b3.place(x=20, y=150)

    b3 = tk.Button(canvas, fg="black", width=10, text="HELP", command = messshow)
    b3.place(x=20, y=200)

    b3 = tk.Button(canvas, fg="black", width=10, text="ABOUT ME", command = About)
    b3.place(x=20, y=300)

    bq = tk.Button(canvas, fg="black", width=10, text="EXIT", command = quit)
    bq.place(x=20, y=250)

    l1 = tk.Label(canvas, width=70, height=15, text = var)
    l1.place(x=150, y=50)



    root.mainloop()
    x = threading.Thread(target=thread_function, args=(0,))
    x.start()


if __name__ == '__main__':

    processes = []

    for i in range(0,1):
        p = multiprocessing.Process(target=main)
        processes.append(p)
        p.start()
            
    for process in processes:
        process.join()