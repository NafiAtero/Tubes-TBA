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
                break
            
    def read_next_token(self):
        self.current_token_idx += 1
        self.current_token = self.token_list[self.current_token_idx]
        
    def syntax_error(self):
        self.output_string = "SYNTAX ERROR"
        break
        
            
    def syntax_condition(self):
        self.read_next_token()
        if self.current_token in grammar.boolean:
            return self.current_token
        elif self.current_token in self.variable_list: pass
        
    def syntax_if(self):
        pass
        


