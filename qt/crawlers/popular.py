from fhp.models.photo_stream import PhotoStream

p = PhotoStream()

MAX = 4
i = 0

for photo in p:
    i += 1
    if i > MAX:
        break
    print photo.image_url_size(100)
