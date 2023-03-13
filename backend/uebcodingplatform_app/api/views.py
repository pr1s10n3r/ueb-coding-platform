from rest_framework import status, viewsets
from rest_framework.response import Response
from api.serializers import DummySerializer
from django.core.files.storage import FileSystemStorage
from api.resolvers.complexity import Complexity
from api.resolvers.organizer import Organizer
from api.resolvers.script import Script
from api.resolvers.docker import Docker
from api.resolvers.measurer import Measurer
from api.resolvers.cleaner import Cleaner

class DummyViewSet(viewsets.ViewSet):
    def list(self, req):
        return Response('Ueb')

    def create(self, req):
        complexity = Complexity()
        organizer = Organizer()
        script = Script()
        docker = Docker()
        measurer = Measurer()
        cleaner = Cleaner()

        serializer = DummySerializer(data=req.data)
        if serializer.is_valid():
            data_dict = serializer.validated_data
            program_input = data_dict["input"]
            program_function = data_dict["function"]
            program_dir, filename = organizer.resolve(data_dict["file"])
            full_path = program_dir + "/" + filename
            complexity_comp = complexity.resolve(full_path, program_function)
            script.resolve(program_dir, program_input)
            docker.resolve("11", program_input, program_dir, filename, script.bash_filename)
            measurer.resolve(program_dir, script.env_filename)
            cleaner.resolve(program_dir)
            return Response({'status': 'it works'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
