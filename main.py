from tkinter import *
from tkinter import ttk
import usaddress
from collections import OrderedDict


class Data:
    def __init__(
        self,
        date,
        name,
        email,
        street_address,
        city,
        state,
        zip,
        phone,
        other_names,
        kids,
        home,
        own_rent,
        yard,
        dogs,
        cats,
        fixed,
        available,
        dog_of_interest,
        asrd_cp,
        ideal_traits,
        experience,
        hrs_alone,
        return_reason,
    ):
        self.date = date
        self.name = name
        self.email = email
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.other_names = other_names
        self.kids = kids
        self.home = home
        self.own_rent = own_rent
        self.yard = yard
        self.dogs = dogs
        self.cats = cats
        self.fixed = fixed
        self.available = available
        self.dog_of_interest = dog_of_interest
        self.asrd_cp = asrd_cp
        self.ideal_traits = ideal_traits
        self.experience = experience
        self.hrs_alone = hrs_alone
        self.return_reason = return_reason


def actions():
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
    questions = stripped_lines[0::2]
    answers = stripped_lines[1::2]

    d = dict()
    for q, a in zip(questions, answers):
        d[q] = a

    full_address = d["Address"]
    tags, address_type = usaddress.tag(full_address)
    street_address = (
        tags["AddressNumber"]
        + " "
        + tags["StreetName"]
        + " "
        + tags["StreetNamePostType"]
    )
    city = tags["PlaceName"]
    state = tags["StateName"]
    zipcode = tags["ZipCode"]

    data = Data(
        d["Submitted At"],
        d["Name (first, middle initial, last)"],
        d["Email"],
        street_address,
        city,
        state,
        zipcode,
        d["Phone"],
        "",
        "",
        d[
            "In which do you live? Single-family house, duplex, trailer home, condo, apartment, or other (specify)"
        ],
        d["Own or rent?"],
        "",
        d["If other dogs, what breed(s), age(s) and gender(s)?"]
        if d.get("If other dogs, what breed(s), age(s) and gender(s)?")
        else "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    )

    delimited_string = ""
    for prop, value in vars(data).items():
        delimited_string += value + ";"

    return delimited_string


root = Tk()
root.title("Rescue Formatter")

content = ttk.Frame(root)
text_in = Text(content, width=80, height=20)
text_out = Text(content, width=80, height=10)
button_format = ttk.Button(content, text="do thing", command=actions)
button_clear = ttk.Button(content, text="Clear Fields", command=clear)

content.grid(column=0, row=0)
text_in.grid(column=0, row=1, columnspan=12, rowspan=1)
text_out.grid(column=0, row=2, columnspan=12, rowspan=1)
button_format.grid(column=0, row=0, sticky=(N, W))
button_clear.grid(column=1, row=0, sticky=(N, W))


root.mainloop()
