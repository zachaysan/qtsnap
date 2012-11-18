from fhp.models.user import User
import subprocess
import os


class UserCrawler(object):
    def __init__(self, username='zachaysan'):
        self.MAX = (1000 * 1000)
        self.i = 0
        self.usernames = set([username])
        self.finished_usernames = set([])

    def crawl_users(self):
        to_add = []
        for username in self.usernames:
            user = User(username=username)
            for u in user.friends:
                if u.username in self.finished_usernames:
                    continue
                to_add.append(u.username)
            for photo in user.favorites:
                if os.path.isfile("photos/%s.jpg" % photo.id):
                    continue
                self.i += 1
                if self.i > self.MAX:
                    break
                self.harvest_photo(photo)
            self.finished_usernames.add(username)
        for username in to_add:
            self.usernames.add(username)
        print to_add
        print "here!"
        print self.usernames
        print self.finished_usernames

                
    def harvest_photo(self, photo):
        url = photo.image_url_size(100)
        process_call = "wget --output-document=photos/%s.jpg %s" % (photo.id, url)
        subprocess.call(process_call, shell=True)

if __name__ == "__main__":
    uc = UserCrawler()
    while len(uc.usernames) > len(uc.finished_usernames):
        try:
            uc.crawl_users()
        except Exception, e:
            print e
            pass

