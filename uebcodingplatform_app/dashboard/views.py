from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
import zipfile, os, docker, os.path, shutil

def index(req):
    print('Hola hola')
    if req.method =='POST':
        form = UploadFileForm(req.POST, req.FILES)
        if form.is_valid():
            handle_upload(req.FILES['file'])
            name_app = unzip_file('/home/dev/1.zip')
            copy_start(name_app)
            create_docker(name_app)
            clean_dirs(name_app)
            return HttpResponseRedirect('success')
    else:
        print('Nos jodimos')
        form = UploadFileForm()

    return render(req, 'dashboard/index.html', {'form': form})

def success(req):
    return render(req, 'dashboard/successpage.html')

def handle_upload(f):
    with open('/home/dev/1.zip', 'wb+') as destinaation:
        for chunk in f.chunks():
            destinaation.write(chunk)
    print('done!')

def unzip_file(filename) -> str:
    with open(filename, 'r+b') as file:
        zip_obj = zipfile.ZipFile(file)
        for name in zip_obj.namelist():
            if name.endswith('/'):
                name_app = name
                os.mkdir(os.path.join('/home/dev/data/', name))
            else:
                with open('/home/dev/data/'+ name, 'wb') as outfile:
                    outfile.write(zip_obj.read(name))
    return name_app

def copy_start(name_app):
    filename = 'start.sh'
    shutil.copy2('/home/dev/' + filename, '/home/dev/data/'+ name_app + filename)

def create_docker(name_app):
    client = docker.from_env()
    client.containers.run('openjdk:11', 'bash start.sh', volumes=['/home/dev/data:/mnt/vol1'], working_dir='/mnt/vol1/'+name_app)

def clean_dirs(name_app):
    path = '/home/dev/data/' + name_app
    shutil.rmtree(path, ignore_errors=True)
    os.remove('/home/dev/1.zip')
