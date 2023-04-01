import os, shutil

class Script:

    new_line = "\n"
    script_dirname = "scripts"
    env_filename = "env.txt"
    bash_filename = "bash.sh"

    def resolve(self, program_dir, input):
        path_str = "%s/%s"
        script_dir = path_str % (os.path.dirname(os.path.dirname(__file__)), self.script_dirname)
        
        # env
        env_srcfile_path = path_str  % (script_dir, self.env_filename)
        env_dstfile_path = path_str % (program_dir, self.env_filename)
        shutil.copy2(env_srcfile_path, env_dstfile_path)

        # bash
        bash_srcfile_path = path_str % (script_dir, self.bash_filename)
        bash_dstfile_path = path_str % (program_dir, self.bash_filename)
        shutil.copy2(bash_srcfile_path, bash_dstfile_path)
