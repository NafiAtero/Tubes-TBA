import grammar



class Variable:
    def __init__(self, var_name, var_type, var_value):
        self.var_name = var_name
        self.var_type = var_type
        self.var_value = var_value
        
    def __repr__(self):
        return f'{self.var_name}'
        
    def update_value(self, new_value):
        self.var_value = new_value
        
class Syntax_Analyzer:
    def __init__(self, token_list):
        self.token_list = token_list

        self.output_string = ""
        self.current_state = ""
        self.variable_list = []
        self.current_token_idx = 0
        self.current_token = self.token_list[self.current_token_idx]
        
        self.mainloop()
        
    def mainloop(self) :
        while self.current_token_idx < len(self.token_list):
            if self.current_token == "\n": self.read_next_token()
            elif self.current_token == "if": self.syntax_if()
            elif self.current_token == "var": self.syntax_var()
            elif self.current_token == "print": self.print_function()
            elif self.current_token in self.variable_list: pass
            elif self.current_token in grammar.other_dividers: self.read_next_token()
            else: 
                self.output_string += "SYNTAX ERROR. current token: " + self.current_token + "\n"
                self.current_token_idx = len(self.token_list)
            
    def read_next_token(self):
        self.current_token_idx += 1
        if self.current_token_idx < len(self.token_list):
            self.current_token = self.token_list[self.current_token_idx]
        
        
    def syntax_error(self, message=""):
        self.output_string += "SYNTAX ERROR. " + message + " current token: " + self.current_token + "\n"
        self.current_token_idx = len(self.token_list)
        
    # is token integer
    def is_integer(self, token):
        try:
            int(token)
            return True
        except:
            return False
        
    # is token string
    def is_string(self, token):
        if token[0] == '"' and token[-1] == '"': return True
        elif token[0] == "'" and token[-1] == "'": return True
        else: return False
    
    # is variable declared
    def is_declared(self, var_name, returns=False):
        for i in range(len(self.variable_list)):
            if self.variable_list[i].var_name == var_name:
                if returns: return self.variable_list[i]
                else: return True
        return False
        
    # print function
    def print_function(self):
        self.read_next_token()
        if self.current_token == "(":
            self.read_next_token()
            # print string
            if self.is_string(self.current_token) and self.token_list[self.current_token_idx+1] == ")":
                self.output_string += self.current_token[1:-1] + "\n"
            # print variable
            elif self.is_declared(self.current_token) and self.token_list[self.current_token_idx+1] == ")":
                if self.is_declared(self.current_token, True).var_type == "string":
                    self.output_string += self.is_declared(self.current_token, True).var_value[1:-1] + "\n"
                else:
                    self.output_string += self.is_declared(self.current_token, True).var_value + "\n"
            else: 
                self.syntax_error("invalid variable")    
                return
            self.read_next_token()
            self.read_next_token()
        else: self.syntax_error()
        
    def syntax_var(self):
        self.read_next_token() # read var type
        if self.current_token in grammar.data_type:
            new_var_type = self.current_token
        else: 
            self.syntax_error("invalid var type")
            return
        self.read_next_token() # read var name
        if self.is_declared(self.current_token): # var name already exists
            self.syntax_error("variable " + self.current_token + " already exists")
        if self.current_token[0] in grammar.alphabet:
            new_var_name = self.current_token
        else: 
            self.syntax_error("invalid var name")
            return
        self.read_next_token()
        if self.current_token == "=":
            self.read_next_token() # read var value
            new_var_val = self.current_token
            self.read_next_token()
        
        if self.current_token in grammar.end_of_line:
            new_var = Variable(new_var_name, new_var_type, new_var_val)
            self.variable_list.append(Variable(new_var_name, new_var_type, new_var_val))
            self.read_next_token()
            
            
                
            
    def syntax_condition(self):
        print("condition")
        # BOOL
        if self.current_token in grammar.boolean: 
            return self.current_token
        # VAR
        elif self.current_token in self.variable_list: 
            var_1 = self.is_declared(self.current_token, True)
            self.read_next_token()
            operator = self.current_token
            self.read_next_token()
            var_2 = self.is_declared(self.current_token, True)
            # int relational operation
            if operator in grammar.operator_relational:
                if self.is_integer(var_1) and self.is_integer(var_2):
                    if relational_operator == "<":
                        if int(var_1.var_value) < int(var_2.var_value): return "true"
                        else: return "false"
                    if relational_operator == "<=":
                        if int(var_1.var_value) <= int(var_2.var_value): return "true"
                        else: return "false"
                    if relational_operator == "==":
                        if int(var_1.var_value) == int(var_2.var_value): return "true"
                        else: return "false"
                    if relational_operator == ">":
                        if int(var_1.var_value) > int(var_2.var_value): return "true"
                        else: return "false"
                    if relational_operator == ">=":
                        if int(var_1.var_value) >= int(var_2.var_value): return "true"
                        else: return "false"
                    if relational_operator == "!=":
                        if int(var_1.var_value) != int(var_2.var_value): return "true"
                        else: return "false"
                else: 
                    self.syntax_error("can't compare non integers")
                    return "false"
            # == string
            elif self.is_string(var_1.var_value) and self.is_string(var_2.var_value):
                if var_1.var_value[1:-1] == var_2.var_value[1:-1]: return "true"
                else: return "false"
            
            # syntax error
            else: 
                self.syntax_error()
                return "false"
                
                
                
        
    def syntax_if(self):
        self.read_next_token()
        # read condition
        condition = self.syntax_condition()
        
        # (
        self.read_next_token()
        if self.current_token != "(":
            self.syntax_error()
            return
        self.read_next_token()
        # if condition true
        if condition == "true": 
            self.mainloop()
        
        # if condition false
        else: 
            while self.current_token != ")":
                self.read_next_token()

        # )
        if self.current_token != "(":
            self.syntax_error()
            return
        self.read_next_token()
        


