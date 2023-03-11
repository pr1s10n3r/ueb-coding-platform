from rest_framework import status, viewsets
from rest_framework.response import Response
from api.serializers import DummySerializer
from django.core.files.storage import FileSystemStorage
import zipfile, os, docker, os.path, shutil


class DummyViewSet(viewsets.ViewSet):
    def list(self, req):
        return Response('Ueb')

    def create(self, req):
        serializer = DummySerializer(data=req.data)
        if serializer.is_valid():
            self.updload_file(serializer.validated_data['file'])
            self.create_docker()
            return Response({'status': 'funciona'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def upload_file(self, f):
        FileSystemStorage(location="/tmp").save('main.java', f)

    def create_docker(self):
        client = docker.from_env()
        client.containers.run('openjdk:11', 'printf \'3\n3\n1\n2\n\' | java main.java', volumes=['/tmp:/mnt/vol1'], working_dir='/mnt/vol1')
