import grammar
import syntax_analyzer

def lexical_analyzer(input_string):
    lexeme_list = []
    current_lexeme = ""
    
    i = 0
    
    while i < len(input_string):
        current_char = input_string[i]
        current_lexeme += current_char
        
        # STRING
        if current_char == '"':
            # a"
            if current_lexeme[:-1] not in grammar.whitespace:
                lexeme_list.append(current_lexeme[:-1])
                current_lexeme = current_char
            # a "
            
            i += 1
            while input_string[i] != '"':
                current_lexeme += input_string[i]
                i += 1
            current_lexeme += input_string[i]
            lexeme_list.append(current_lexeme)
            current_lexeme = ""
            i += 1
            current_char = input_string[i]
            current_lexeme += current_char
                
            

        
        # DIVIDER
        #  ()
        if input_string[i:i+2] in grammar.divider:
            if current_lexeme[:-1] not in grammar.whitespace:
                lexeme_list.append(current_lexeme[:-1])
            current_lexeme = current_char
        # a ( 
        elif current_lexeme in grammar.divider:
            lexeme_list.append(current_lexeme)
            current_lexeme = ""
        # a(
        elif current_char in grammar.divider:
            if current_lexeme[:-1] not in grammar.whitespace:
                lexeme_list.append(current_lexeme[:-1])
            lexeme_list.append(current_char)
            current_lexeme = ""            
        
        # WHITESPACE
        if current_char in grammar.whitespace:
            if current_lexeme not in grammar.whitespace:
                lexeme_list.append(current_lexeme[:-1])
            current_lexeme = ""
            
        i += 1
    
    return lexeme_list
            
    
            
def parse_string(input_string):
    token_list = lexical_analyzer(input_string)
    
    token_string = ""
    for i in token_list:
        if i == "\n": 
            token_string += "\\n" + "\n"
        else:
            token_string += i + "\n"
    
    output_string = syntax_analyzer.Syntax_Analyzer(token_list).output_string
    
    return output_string, token_string