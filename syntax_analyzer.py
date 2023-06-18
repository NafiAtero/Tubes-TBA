import grammar

class Variable:
    def __init__(self, var_name, var_type, var_value):
        self.var_name = var_name
        self.var_type = var_type
        self.var_value = var_value
        
    def __repr__(self):
        return "{self.var_name}"
        
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
            elif self.current_token == "var": pass
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
        
        
    def syntax_error(self):
        self.output_string += "SYNTAX ERROR\n"
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
        
    # print function
    def print_function(self):
        self.read_next_token()
        if self.current_token == "(":
            self.read_next_token()
            if self.is_string(self.current_token) and self.token_list[self.current_token_idx+1] == ")":
                self.output_string += self.current_token[1:-1] + "\n"
            elif self.current_token in self.variable_list and self.token_list[self.current_token_idx+1] == ")":
                self.output_string += self.variable_list[self.variable_list.index(self.current_token)].var_value + "\n"
            else: 
                self.syntax_error()    
                return
            self.read_next_token()
            self.read_next_token()
        else: self.syntax_error()
            
    def syntax_condition(self):
        # BOOL
        if self.current_token in grammar.boolean: 
            return self.current_token
        # VAR
        elif self.current_token in self.variable_list: 
            var_1 = self.current_token
            self.read_next_token()
            operator = self.current_token
            self.read_next_token()
            var_2 = self.current_token
            # int relational operation
            if operator in grammar.operator_relational:
                if self.is_integer(var_1) and self.is_integer(var_2):
                    if relational_operator == "<":
                        if int(var_1) < int(var_2): return "true"
                        else: return "false"
                    if relational_operator == "<=":
                        if int(var_1) <= int(var_2): return "true"
                        else: return "false"
                    if relational_operator == "==":
                        if int(var_1) == int(var_2): return "true"
                        else: return "false"
                    if relational_operator == ">":
                        if int(var_1) > int(var_2): return "true"
                        else: return "false"
                    if relational_operator == ">=":
                        if int(var_1) >= int(var_2): return "true"
                        else: return "false"
                    if relational_operator == "!=":
                        if int(var_1) != int(var_2): return "true"
                        else: return "false"
                else: 
                    self.syntax_error()
                    return "false"
            # == string
            elif self.is_string(var_1) and self.is_string(var_2):
                if var_1[1:-1] == var_2[1:-1]: return "true"
                else: return "false"
            
            # syntax error
            else: 
                self.syntax_error()
                return "false"
                
                
                
        
    def syntax_if(self):
        self.read_next_token()
        # read condition
        condition = self.syntax_condition(self)
        
        # (
        self.read_next_token()
        if self.current_token != "(":
            self.syntax_error()
            return
        self.read_next_token()
        # if condition true
        if condition == "true": 
            #TODO ifloop    arithmetic, print
            pass
        
        # if condition false
        else: 
            while self.current_token != ")":
                self.read_next_token()

        # )
        if self.current_token != "(":
            self.syntax_error()
            return
        self.read_next_token()
        


