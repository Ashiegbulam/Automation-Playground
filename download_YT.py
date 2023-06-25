"""A simple software to download youtube videos"""
from pytube import YouTube
from sys import argv #argv because input will be taken frm the cmd line

link = argv[1] #second argument in the cmd line. 1st = "main"
youtube = YouTube(link)
downloads = youtube.streams.get_highest_resolution()
downloads.download(r'C:\Users\Caveman\Desktop\playground')
print("Title: ", youtube.title)
print("View: ", youtube.views)

# Note: Use this software by running it from a cmd line
# followed by the youtube link