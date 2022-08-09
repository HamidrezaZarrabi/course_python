from moviepy import editor
video = editor.VideoFileClip('Wildlife.wmv')
video.audio.write_audiofile('Wildlife.mp3')
