from tkinter import *
from tkinter import ttk


def copy():
    input = text_in.get("1.0", "end")
    contents = parse(input)
    text_out.insert("1.0", contents)


def clear():
    text_in.delete("1.0", "end")
    text_out.delete("1.0", "end")


def parse(contents):
    clean_whitespace = contents.strip()
    split_lines = clean_whitespace.splitlines()
    stripped_lines = [item.strip() for item in split_lines]
    answers = stripped_lines[1::2]

    row = ""
    for answer in answers:
        row += answer + ";"
    return row


root = Tk()
content = ttk.Frame(root)
text_in = Text(content, width=80, height=20)
text_out = Text(content, width=80, height=10)
button_format = ttk.Button(content, text="do thing", command=copy)
button_clear = ttk.Button(content, text="Clear Fields", command=clear)

content.grid(column=0, row=0)
text_in.grid(column=0, row=1, columnspan=12, rowspan=1)
text_out.grid(column=0, row=2, columnspan=12, rowspan=1)
button_format.grid(column=0, row=0, sticky=(N, W))
button_clear.grid(column=1, row=0, sticky=(N, W))


root.mainloop()
