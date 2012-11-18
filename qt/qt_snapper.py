import Image
import numpy
import os
from collections import namedtuple
import sys

def get_edge_pixels(image):
    pixel_array = numpy.array(image, dtype=numpy.int16)
    north = numpy.copy(pixel_array[0])
    east = numpy.copy(pixel_array[:,-1])
    south = numpy.copy(pixel_array[-1])
    west = numpy.copy(pixel_array[:,0])
    del(pixel_array)
    return numpy.array([north, east, south, west])

def get_photos():
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            p = os.path.join(root, f)
            if p[-4:] == ".jpg":
                yield p



def main():
    photos = {}
    for image_filename in get_photos():
        try:
            image = Image.open(image_filename)
        except Exception, e:
            print "skipping %s" % image_filename
            print e
        try:
            photo_id = int(image_filename.split("/")[-1][:-4])
            
            photo = get_edge_pixels(image)
            photos[photo_id] = photo
        except Exception, e:
            print "skipping %s" % image_filename
            print e
    target_photo_id = 2891405
    tp = photos[target_photo_id]
    target_photo = numpy.array([tp[2],tp[3],tp[0],tp[1]], dtype=numpy.int16)
    best = None
    best_photo_id = [None, None, None, None]

    for photo_id in photos:
        if photo_id == target_photo_id:
            continue
        candidate_photo = photos[photo_id]
        try:
            color_diff = numpy.subtract(candidate_photo, target_photo)
            abs_color_diff = numpy.absolute(color_diff)
            diff_count = numpy.sum(numpy.sum(abs_color_diff, axis=1, dtype=numpy.uint32), dtype=numpy.uint32, axis=1)
            if best is None:
                best = diff_count
            axis_match = numpy.less(diff_count, best)
            if numpy.any(axis_match):
                i = 0
                for elem in axis_match:
                    if elem:
                        best_photo_id[i] = photo_id
                    i += 1

        except Exception, e:
            print e
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
            print(exc_type, fname, exc_tb.tb_lineno)
    print target_photo_id
    print best_photo_id

if __name__ == "__main__":
    main()
