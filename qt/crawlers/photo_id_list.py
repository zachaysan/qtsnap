import subprocess
import os
from fhp.models.photo import photo

with open("ids") as id_file:
    for line in id_file.readlines():
        try:
            photo_id = int(line.rstrip())
        except:
            print "skipping line:"
            continue
        if photo_id % 100 == 0:
            print photo_id
        if os.path.isfile("photos/%s.jpg" % photo.id):
            continue
        url = photo.image_url_size(100)
        process_call = "wget --output-document=photos/%s.jpg %s" % (photo.id, url)
        subprocess.call(process_call, shell=True)
