#Video editor by atabekdemurtaza 

from tkinter import * 
from moviepy.editor import * 

#variables 
clip_1 = VideoFileClip("1.mp4")
clip_2 = VideoFileClip("2.mp4")
clip_3 = VideoFileClip("3.mp4")

#Functions 
def mix():
	final_clip = concatenate_videoclips([clip_1, clip_2, clip_3])
	final_clip.write_videofile("Final_render.mp4")

def mirror():
	clip_mirror = clip_1.fx(vfx.mirror_x)
	clip_mirror.write_videofile("Final_render.mp4")

def resize():
	r = float(input('Enter your Size: '))
	clip_resize = clip_1.resize(r)
	clip_resize.write_videofile("Final_render.mp4")

def Effects_speed():
	speed = float(input('Enter your Size: '))
	clip_speed = clip_1.fx(vfx.speedx, speed)
	clip_speed.write_videofile("Final_render.mp4")

def Color():
	color = float(input("Value of Darkness: "))
	clip_color = clip_1.fx(vfx.colorx, color)
	clip_color.write_videofile("Final_render.mp4")

def trim():

	starting = int(input("Enter Starting Point here: "))
	ending = int(input("Enter Ending Point here: "))
	clip_trim = clip_1.cutout(starting, ending)
	clip_trim.write_videofile("Final_render.mp4")

def audio_file():

	import moviepy.editor as mpe
	audio_clip = mpe.AudioFileClip("audio.mp3")
	videoclip = mpe.VideoClip.set_audio(audio_clip)
	final_clip = videoclip.set_audio(audio_clip)
	final_clip.write_videofile("Final_render.mp4")

#Main screen 
root = Tk()
root.title('Video Editor')
root.geometry("750x200")
root.minsize(750, 200)
root.maxsize(750, 200)
root.configure(bg='#678983')

#Mix 
b = Button(root, text="Mix", relief=GROOVE, bg='#678983', fg="white", command=mix)
b.pack(side="left", padx=20)
b.configure(width=8, height=3)

#Mirror
b = Button(root, text="Mirror", relief=GROOVE, bg='#678983', fg="white", command=mirror)
b.pack(side="left", padx=20)
b.configure(width=8, height=3)

#Resize
b = Button(root, text="Resize", relief=GROOVE, bg='#678983', fg="white", command=resize)
b.pack(side="left", padx=20)
b.configure(width=8, height=3)

#Speed
b = Button(root, text="Speed", relief=GROOVE, bg='#678983', fg="white", command=Effects_speed)
b.pack(side="left", padx=20)
b.configure(width=8, height=3)

#Color
b = Button(root, text="Color", relief=GROOVE, bg='#678983', fg="white", command=Color)
b.pack(side="left", padx=20)
b.configure(width=8, height=3)

#Trim
b = Button(root, text="Trim", relief=GROOVE, bg='#678983', fg="white", command=trim)
b.pack(side="left", padx=20)
b.configure(width=8, height=3)

#Audio
b = Button(root, text="Audio", relief=GROOVE, bg='#678983', fg="white", command=audio_file)
b.pack(side="left", padx=20)
b.configure(width=8, height=3)

root.mainloop()

