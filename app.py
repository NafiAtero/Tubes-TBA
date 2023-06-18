import parser

from tkinter import *
from tkinter import ttk

def parse_input():
    token_frame_textbox.config(state=NORMAL)
    output_frame_textbox.config(state=NORMAL)
    input_string = input_frame_textbox.get("1.0", END)
    output_string, token_string = parser.parse_string(input_string)
    
    token_frame_textbox.delete("1.0", END)
    token_frame_textbox.insert("1.0", token_string)
    output_frame_textbox.delete("1.0", END)
    output_frame_textbox.insert("1.0", output_string)
    token_frame_textbox.config(state=DISABLED)
    output_frame_textbox.config(state=DISABLED)

outer = Tk()
#outer.geometry("430x850")
outer.title("Lexical Analyzer/Parser")

root = Frame(outer)

# TITLE
title_frame = Frame(root, bd=3)
title_frame_main_title = Label(title_frame, text="Lexical Analyzer/Parser", font=("Arial", 18))
title_frame_text = Label(title_frame, text="bla bla bla", font=("Arial", 12))

# TITLE RENDER
title_frame_main_title.pack()
title_frame_text.pack()


# INPUT
input_frame = Frame(root, bd=3)
input_frame_title = Label(input_frame, text="Input text", font=("Arial", 14))
input_frame_textbox = Text(input_frame, height=15, width=50)

# INPUT RENDER
input_frame_title.pack()
input_frame_textbox.pack()


# TOKEN
token_frame = Frame(root, bd=3)
token_frame_title = Label(token_frame, text="Tokens", font=("Arial", 14))
token_frame_textbox = Text(token_frame, height=20, width=50)
token_frame_textbox.config(state=DISABLED)

# TOKEN RENDER
token_frame_title.pack()
token_frame_textbox.pack()


# OUTPUT
output_frame = Frame(root, bd=3)
output_frame_title = Label(output_frame, text="Output text", font=("Arial", 14))
output_frame_textbox = Text(output_frame, height=5, width=50)
output_frame_textbox.config(state=DISABLED)

# OUTPUT RENDER
output_frame_title.pack()
output_frame_textbox.pack()


# PARSE BUTTON
parse_button = Button(root, text="Parse", font=("Arial", 14), command=parse_input)


# RENDER
title_frame.grid(row=0, column=0)
input_frame.grid(row=1, column=0)
parse_button.grid(row=2, column=0)
token_frame.grid(row=3, column=0)
output_frame.grid(row=4, column=0)



root.pack()
outer.mainloop()