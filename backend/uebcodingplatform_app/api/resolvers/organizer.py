from django.core.files.storage import FileSystemStorage
import datetime, os

class Organizer:

    filename = "main.java"
    tmpdir = "/tmp/"
    dtformat = ("%Y%m%d%H%M%S")

    def resolve(self, file):
        now = datetime.datetime.now()
        folder_name = now.strftime(self.dtformat)
        folder_path = os.path.join(self.tmpdir, folder_name)
        os.makedirs(folder_path)
        try:
            fs = FileSystemStorage(location=folder_path)
            fs.save(self.filename, file)
        except:
            print("Something was wrong trying to save the file")
        return (folder_path, self.filename)
