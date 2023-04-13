import plyj.parser as plyj
from  plyj.model import *
from operator import concat

class StatementComplexity:
    def __init__(self, depth, is_log):
        
        self.depth = depth
        self.is_log = is_log

class Complexity:

    def __init__(self):
        self.complexities_weight = {
            'constant': 0,
            'logarithmic': 1,
            'linear': 2,
            'linearithmic': 3,
            'quadratic': 4,
            'cubic': 5,
            'polynomial': 6
        }
        self.methods_created_by_user = []
        self.dependencies = {}
        
    def get_methods(self, program: ClassDeclaration):
        for method in program.body:
            if isinstance(method, MethodDeclaration):
                self.methods_created_by_user.append(method.name)

    def get_method_variable(self, variable: VariableDeclaration):
        methods = []
        for variablede_declarator in variable.variable_declarators:
            if isinstance(variablede_declarator, VariableDeclarator):
                if isinstance(variablede_declarator.initializer, MethodInvocation):
                    if variablede_declarator.initializer.name in self.methods_created_by_user:
                        methods.append(variablede_declarator.initializer.name)
        return methods

    def get_methods_if(self, statement: IfThenElse):
        methods = []
        if isinstance(statement.if_true, Block):
            for true_statement in statement.if_true.statements:    
                if isinstance(true_statement, For) or isinstance(true_statement, DoWhile) or isinstance(true_statement, While) or isinstance(true_statement, ForEach):
                    methods_nested = self.get_methods_loops(true_statement)
                    methods = concat(methods, methods_nested)
                elif isinstance(true_statement, IfThenElse):
                    methods_nested = self.get_methods_if(true_statement)
                    methods = concat(methods, methods_nested)
                elif isinstance(true_statement, VariableDeclaration):
                    methods_nested = self.get_method_variable(true_statement)
                    methods = concat(methods, methods_nested)
                elif isinstance(true_statement, MethodInvocation):
                    if true_statement.name in self.methods_created_by_user:
                        methods.append(true_statement.name)
        elif isinstance(statement.if_true, MethodInvocation):
            if statement.if_true.name in self.methods_created_by_user:
                methods.append(statement.if_true.name)
        
        if isinstance(statement.if_false, Block):
            for false_statement in statement.if_true.statements:    
                if isinstance(false_statement, For) or isinstance(false_statement, DoWhile) or isinstance(false_statement, While) or isinstance(false_statement, ForEach):
                    methods_nested = self.get_methods_loops(false_statement)
                    methods = concat(methods, methods_nested)
                elif isinstance(false_statement, IfThenElse):
                    methods_nested = self.get_methods_if(false_statement)
                    methods = concat(methods, methods_nested)
                elif isinstance(true_statement, VariableDeclaration):
                    methods_nested = self.get_method_variable(true_statement)
                    methods = concat(methods, methods_nested)
                elif isinstance(false_statement, MethodInvocation):
                    if false_statement.name in self.methods_created_by_user:
                        methods.append(false_statement.name)
        elif isinstance(statement.if_false, MethodInvocation):
            if statement.if_false.name in self.methods_created_by_user:
                methods.append(statement.if_false.name)
        return methods
        
    def get_methods_loops(self, loop: For | While | DoWhile | ForEach):
        methods = []
        if isinstance(loop.body, Block):
            for loop_statement in loop.body.statements:
                if isinstance(loop_statement, For) or isinstance(loop_statement, DoWhile) or isinstance(loop_statement, While) or isinstance(loop_statement, ForEach):
                    methods_nested = self.get_methods_loops(loop_statement)
                    methods = concat(methods, methods_nested)
                elif isinstance(loop_statement, IfThenElse):
                    methods_nested = self.get_methods_if(loop_statement)
                    methods = concat(methods, methods_nested)
                elif isinstance(loop_statement, VariableDeclaration):
                    methods_nested = self.get_method_variable(loop_statement)
                    methods = concat(methods, methods_nested)
                elif isinstance(loop_statement, MethodInvocation):
                    if loop_statement.name in self.methods_created_by_user:
                        methods.append(loop_statement.name)
        elif isinstance(loop.body, MethodInvocation):
            if loop.body.name in self.methods_created_by_user:
                methods.append(loop.body.name)
        return methods

    def get_dependencies(self, method: MethodDeclaration):
        dependencies = []
        for statement in method.body:
            if isinstance(statement, For) or isinstance(statement, DoWhile) or isinstance(statement, While) or isinstance(statement, ForEach):
                dependencies_nested = self.get_methods_loops(statement)
                dependencies = concat(dependencies, dependencies_nested)
            elif isinstance(statement, IfThenElse):
                dependencies_nested = self.get_methods_if(statement)
                dependencies = concat(dependencies, dependencies_nested)
            elif isinstance(statement, VariableDeclaration):
                dependencies_nested = self.get_method_variable(statement)
                dependencies = concat(dependencies, dependencies_nested)
            elif isinstance(statement, MethodInvocation):
                if statement.name in self.methods_created_by_user:
                    dependencies.append(statement.name)
        self.dependencies[method.name] = dependencies

    def circular_dependency(self):
        for method in self.methods_created_by_user:
            dependencies = self.dependencies[method]
            for dependency in dependencies:
                if method in self.dependencies[dependency]:
                    return True
        return False
    
    def recursion(self):
        for method in self.methods_created_by_user:
            dependencies = self.dependencies[method]
            for dependency in dependencies:
                if dependency == method:
                    return True
        return False
    
    def infinity_loop(self, loop: For | While | DoWhile):
        if isinstance(loop, (While, DoWhile)):
            if isinstance(loop.predicate, Literal):
                if loop.predicate.value == True:
                    return True
        elif isinstance(loop, For):
            if loop.predicate is None:
                return True
        return False
    
    def check_infinity_loop(self, loop: Block | For | While | DoWhile | ForEach):
        if isinstance(loop, Block):
            for statement in loop.statements:
                if isinstance(statement, IfThenElse):
                    if statement.if_false is not None:
                        self.loops_depth(statement.if_false)
                elif isinstance(statement, (For, ForEach, While, DoWhile)):
                    if self.infinity_loop(statement):
                        return True
                    self.loops_depth(statement.body)
        elif isinstance(loop.body, Block):
            for statement in loop.body.statements:
                if isinstance(statement, IfThenElse):
                    self.loops_depth(statement.if_true)
                    if statement.if_false is not None:
                        self.loops_depth(statement.if_false)
                elif isinstance(statement, (For, ForEach, While, DoWhile)):
                    if self.infinity_loop(statement):
                        return True
                    self.loops_depth(statement.body)
        return False

    def loops_depth(self, loop: Block | For | While | DoWhile | ForEach):
        depth = 0
        if isinstance(loop, Block):
            for statement in loop.statements:
                if isinstance(statement, IfThenElse):
                    depth += self.loops_depth(statement.if_true)
                    if statement.if_false is not None:
                        depth += self.loops_depth(statement.if_false)
                elif isinstance(statement, (For, ForEach, While, DoWhile)):
                    depth += 1
                    depth += self.loops_depth(statement.body)
        elif isinstance(loop.body, Block):
            for statement in loop.body.statements:
                if isinstance(statement, IfThenElse):
                    depth += self.loops_depth(statement.if_true)
                    if statement.if_false is not None:
                        depth += self.loops_depth(statement.if_false)
                elif isinstance(statement, (For, ForEach, While, DoWhile)):
                    depth += 1
                    depth += self.loops_depth(statement.body)
                    
        return depth
    
    def calculate_complexity(self, method: ClassDeclaration):
        statement_complexity_lst = []
        for statement in method.body:
            is_log = False
            depth = 0
            if isinstance(statement, For) or isinstance(statement, DoWhile) or isinstance(statement, While) or isinstance(statement, ForEach):
                if self.infinity_loop(statement) or self.check_infinity_loop(statement):
                    return 'error: infinite loop detected'
            
                depth = self.loops_depth(statement) + 1
                
                if depth == 1 and len(statement.update) == 1:
                    if isinstance(statement.update[0], Unary):
                        if statement.update[0].sign != 'x++' and statement.update[0].sign != 'x--':
                            is_log = True
                    if isinstance(statement.update[0], Assignment):
                        if statement.update[0].operator != '+=' and statement.update[0].operator != '-=':
                            is_log = True
                elif depth == 2 and len(statement.update) == 1:
                    if isinstance(statement.update[0], Unary):
                        if statement.update[0].sign != 'x++' and statement.update[0].sign != 'x--':
                            is_log = True
                    if isinstance(statement.update[0], Assignment):
                        if statement.update[0].operator != '+=' and statement.update[0].operator != '-=':
                            is_log = True
                    if isinstance(statement.body, Block):
                        for statement_nested in statement.body:
                            if isinstance(statement_nested, For) or isinstance(statement_nested, DoWhile) or isinstance(statement_nested, While) or isinstance(statement_nested, ForEach):        
                                if isinstance(statement_nested.update[0], Unary) and len(statement_nested.update) == 1:
                                    if statement_nested.update[0].sign != 'x++' and statement_nested.update[0].sign != 'x--':
                                        is_log = True
                                if isinstance(statement_nested.update[0], Assignment) and len(statement_nested.update) == 1:
                                    if statement_nested.update[0].operator != '+=' and statement_nested.update[0].operator != '-=':
                                        is_log = True

            statement_complexity_lst.append(StatementComplexity(depth, is_log))

        if (len(statement_complexity_lst) > 0):
            worst_case_statement = max(statement_complexity_lst, key = lambda x: x.depth)
        
        if worst_case_statement.depth == 0:
            return 'constant'
        elif worst_case_statement.depth == 1 and worst_case_statement.is_log:
            return 'logarithmic'
        elif worst_case_statement.depth == 1 and not worst_case_statement.is_log:
            return 'linear'
        elif worst_case_statement.depth == 2 and worst_case_statement.is_log:
            return 'linearithmic'
        elif worst_case_statement.depth == 2 and not worst_case_statement.is_log:
            return 'quadratic'
        elif worst_case_statement.depth == 3:
            return 'cubic'
        elif worst_case_statement.depth > 3:
            return 'polynomial'
    
    def complexity(self, program: ClassDeclaration, target_method: str):
        method_complexity_lst = []
        dependencies = self.dependencies[target_method]
        for method in program.body:
            if isinstance(method, MethodDeclaration):
                if method.name == target_method or method.name in dependencies:
                    complexity = self.calculate_complexity(method)
                    if 'error' in complexity:
                        return complexity
                    method_complexity_lst.append((self.complexities_weight[complexity], complexity))
        worst_case_method = max(method_complexity_lst)
        return worst_case_method[1]
    
    def resolve(self, filename, target_method):
        with open(filename, 'r') as f:
            source_code = f.read()
        error = None
        result = ''
        parser = plyj.Parser()
        tree = parser.parse_string(source_code)
        for item in tree.type_declarations:
            if isinstance(item, ClassDeclaration):
                self.get_methods(item)
                for method in item.body:
                    if isinstance(method, MethodDeclaration):
                        self.get_dependencies(method)
                if self.circular_dependency():
                    error = (1, 'circular dependency')
                complexity = self.complexity(item, target_method)
                if 'error' in complexity:
                    error = (2, complexity)
                else:
                    result = complexity
        return error, result