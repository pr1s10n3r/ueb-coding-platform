class Script:

    new_line = "\n"
    env_filename = "env.txt"
    bash_filename = "bash.sh"

    def resolve(self, program_dir, input):
        with open("%s/%s" % (program_dir, self.env_filename), "w") as env_file:
            env_file.write("TIME = 0")

        with open("%s/%s" % (program_dir, self.bash_filename), "w") as bash_file:
            lines = []
            lines.append("#!/bin/bash")
            lines.append(self.new_line)
            lines.append("start=$(date -u +%s%N)")
            lines.append(self.new_line)
            lines.append("printf $1 | java $2")
            lines.append(self.new_line)
            lines.append("end=$(date -u +%s%N)")
            lines.append(self.new_line)
            lines.append("TIME=\"$((($end-$start)/1000000))\"")
            lines.append(self.new_line)
            lines.append("sed -i -r \"s/^(TIME =).*/\\1 $TIME/\" env.txt")
            bash_file.writelines(lines)

