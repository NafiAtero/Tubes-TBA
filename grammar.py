# WHITESPACE
whitespace = [" ", "\t", ""]

#DIVIDER
punctuator = ["{", "}", "(", ")"]
string_identifier = ['"', "'"]
operator_relational = ["<", "<=", "==", ">=", ">", "!="]
operator_arithmetic = ["+", "-", "*", "/"]
end_of_line = [";", "\n"]
other_dividers = ["=", ":=", "!"]
divider = punctuator + string_identifier + operator_arithmetic + operator_relational + end_of_line + other_dividers

#ALPHABET
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#KEYWORDS
boolean = ["true", "false"]
syntax = ["if", "var"]
data_type = ["string", "int", "bool"]



