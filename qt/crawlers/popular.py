from fhp.models.photo_stream import PhotoStream
import subprocess
import os

p = PhotoStream()

MAX = (1000 * 1000)
i = 0

for photo in p:
    if os.path.isfile("photos/%s.jpg" % photo.id):
        continue
    
    i += 1
    if i > MAX:
        break
    url = photo.image_url_size(100)
    process_call = "wget --output-document=photos/%s.jpg %s" % (photo.id, url)
    subprocess.call(process_call, shell=True)
