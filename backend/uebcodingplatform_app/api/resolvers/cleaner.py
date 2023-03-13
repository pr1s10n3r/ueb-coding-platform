import shutil

class Cleaner:
    
    def resolve(self, program_dir):
        shutil.rmtree(program_dir, ignore_errors=True)
