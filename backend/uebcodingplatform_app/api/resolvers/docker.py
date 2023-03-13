import docker

class Docker:

    working_dir = "/mnt/vol1"
    image_container = "openjdk"
    bash_command = "bash"

    def resolve(self, java_version, program_input, program_dir, program_name, bash_filename):
        client = docker.from_env()
        image = "%s:%s" % (self.image_container, java_version)
        command = "%s %s '%s' '%s'" % (self.bash_command, bash_filename, program_input, program_name)
        volume =  "%s:%s" % (program_dir, self.working_dir)
        client.containers.run(image, command, volumes=[volume], working_dir=self.working_dir)
