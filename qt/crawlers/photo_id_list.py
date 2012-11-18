import subprocess
import os
from fhp.models.photo import Photo

i = 0

with open("ids") as id_file:
    for line in id_file.readlines():
        i += 1
        try:
            photo_id = int(line.rstrip())
        except:
            print "skipping line:"
            continue
        if i % 10000 == 0:
            print photo_id
            print i
        if os.path.isfile("photos/%s.jpg" % photo_id):
            continue
        try:
            photo = Photo(photo_id)
        except Exception, e:
            print "skipping photo %s" % photo_id
            print e
            continue
        url = photo.image_url_size(100)
        process_call = "wget --output-document=photos/%s.jpg %s" % (photo.id, url)
        subprocess.call(process_call, shell=True)
