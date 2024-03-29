class Complexity:

    def resolve(self, filename, target_func):
        stack = []
        program = []
        f = open(filename, "r")

        line = f.readline()
        while not target_func in line and line != "":
            line = f.readline()

        line = f.readline()
        while line != "":
            if "{" in line:
                stack.append("start")
            else:
                program.append(line)
            if "}" in line:
                stack.pop()
            if len(stack) == 0:
                break
            line = f.readline()
        f.close()

        java_program = "".join(program)
        loops = java_program.count("for") + java_program.count("while")
        conditionals = java_program.count("if")

        if loops == 0 and conditionals == 0:
            return "constant"
        elif loops == 1 and conditionals == 0:
            return "linear"
        elif loops > 1 and conditionals == 0:
            return "quadratic"
        else:
            return "Nlogarithmic"
