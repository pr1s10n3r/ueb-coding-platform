from django.core.files.storage import FileSystemStorage
import uuid, os

class Organizer:

    filename = "main.java"
    tmpdir = "/tmp/"

    def resolve(self, file):
        folder_path = os.path.join(self.tmpdir, str(uuid.uuid4()))
        os.makedirs(folder_path)
        try:
            fs = FileSystemStorage(location=folder_path)
            fs.save(self.filename, file)
        except:
            print("Something was wrong trying to save the file")
        return (folder_path, self.filename)
