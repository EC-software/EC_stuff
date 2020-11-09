import tabula

file = "/home/martin/repos/EC_stuff/misc/data_pdf/2020-10.pdf"

tables = tabula.read_pdf(file)  # , pages="all", multiple_tables=True)