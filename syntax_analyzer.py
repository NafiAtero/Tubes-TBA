import grammar

class Variable:
    def __init__(self, var_name, var_type, var_value):
        self.var_name = var_name
        self.var_type = var_type
        self.var_value = var_value
        
    def __repr__(self):
        return "{self.var_name} = {self.var_value} : {self.var_type}"
        
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
            elif self.current_token == "print": pass
            elif self.current_token in self.variable_list: pass
            else: 
                self.output_string = "SYNTAX ERROR"
                self.current_token_idx = len(self.token_list)
            
    def read_next_token(self):
        self.current_token_idx += 1
        self.current_token = self.token_list[self.current_token_idx]
        
    def syntax_error(self):
        self.output_string = "SYNTAX ERROR"
        self.current_token_idx = len(self.token_list)
        
    # is token integer
    def is_integer(self):
        try:
            int(self.current_token)
            return True
        except:
            return False
        
    # is token string
    def is_string(self):
        if self.current_token[0] == '"' and self.current_token[-1] == '"': return True
        elif self.current_token[0] == "'" and self.current_token[-1] == "'": return True
        else: return False
            
    def syntax_condition(self):
        # BOOL
        if self.current_token in grammar.boolean: 
            return self.current_token
        # VAR
        elif self.current_token in self.variable_list: 
            var_1 = self.current_token
            self.read_next_token()
            # relational operation
            if self.current_token in grammar.operator_relational:
                relational_operator = self.current_token
                self.read_next_token()
                var_2 = self.current_token
                
                
        
    def syntax_if(self):
        self.read_next_token()
        # read condition
        condition = self.syntax_condition(self)
        # if condition true
        if condition: pass
        # if condition false
        else: pass
        


