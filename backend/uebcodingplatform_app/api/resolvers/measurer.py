class Measurer:

    def resolve(self, program_dir, env_filename):
        time = 0;
        with open("%s/%s" % (program_dir, env_filename)) as env_file:
            # time
            name, value = env_file.readline().partition("=")[::2]
            time = float(value)

            #output
            name, value = env_file.readline().partition("=")[::2]
            output = str(value)

        return time, output
