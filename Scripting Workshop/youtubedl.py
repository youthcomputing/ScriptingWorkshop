from pytube import YouTube as Youtube
link = input('link to youtube video: ')
yt = Youtube(link)
yt.streams.filter(progressive=True, file_extension='mp4', res='720p').first().download()


print('downloaded', link)
