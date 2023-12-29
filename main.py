import tkinter
import customtkinter
from pytube import YouTube
import threading

def startDownload():

    global finishLabel #Declare finishLabel as a global variable

    def download_thread():
        try:
            ytLink = link.get()
            ytObject = YouTube(ytLink)
            video = ytObject.streams.get_highest_resolution()

            title.configure(text=ytObject.title, text_color="white")
            finishLabel.configure(text="")

            video.download()
            finishLabel.configure(text="Downloaded!") 

        except:
            finishLabel.configure(text="Invalid link. Download error", text_color ="red")

    # Create a thread for the download operation
    download_thread = threading.Thread(target=download_thread)
    download_thread.start()

#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Video Downloader")

#Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#Run app
app.mainloop()