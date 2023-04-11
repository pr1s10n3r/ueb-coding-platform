import os
from rest_framework import status, viewsets
from rest_framework.response import Response
from api.serializers import DummySerializer
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
            program_time = data_dict["time"]
            program_complexity = data_dict["complexity"]
            
            program_dir, filename = organizer.resolve(data_dict["file"])
            full_path = os.path.join(program_dir, filename)
            error, complexity_comp = complexity.resolve(full_path, program_function)
            script.resolve(program_dir, program_input)
            docker.resolve("11", program_input, program_dir, filename, script.bash_filename)
            time = measurer.resolve(program_dir, script.env_filename)
            cleaner.resolve(program_dir)
            return Response({
                'function': program_function,
                'input': program_input,
                'success': True,
                'complexity': {
                    'expected': program_complexity,
                    'actual': complexity_comp
                },
                'time': {
                    'expected': program_time,
                    'actual': time
                },
                'output': 'Not implemented'
            })
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
