from fhp.models.photo_stream import PhotoStream
import subprocess
p = PhotoStream()

MAX = 10
i = 0

for photo in p:
    i += 1
    if i > MAX:
        break
    url = photo.image_url_size(100)
    process_call = "wget --output-document=%s.jpg %s" % (photo.id, url)
    subprocess.call(process_call, shell=True)
