import tkinter as tk

import tksheet
import datetime
top = tk.Tk()
top.geometry("900x300")
sheet = tksheet.Sheet(top)


sheet.pack(fill="both",expand=True)

sheet.set_sheet_data([(1, 'Raj Kumar', 'M', 93, datetime.date(2000, 11, 17), 9586774748, 'Science'), (3, 'Ankit Sharma', 'M', 76, datetime.date(2000, 2, 2), 8567490078, 'Science'), (4, 'Radhika Gupta', 'F', 78, datetime.date(1999, 12, 3), 9818675444, 'Humanities'), (5, 'Payal Goel', 'F', 82, datetime.date(1998, 4, 21), 9845639990, 'Vocational'), (6, 'Diksha Sharma', 'F', 80, datetime.date(1999, 12, 17), 9897666650, 'Humanities'), (7, 'Gurpreet Kaur', 'F', 65, datetime.date(2000, 1, 4), 7560567890, 'Science'), (9, 'Shreya Anand', 'F', 70, datetime.date(1999, 10, 8), 8876543988, 'Vocational'), (10, 'Prateek Mittal', 'M', 75, datetime.date(2000, 12, 25), 9999967543, 'Science')])

# table enable choices listed below:

sheet.enable_bindings(("single_select",

                       "row_select",

                       "column_width_resize",

                       "arrowkeys",

                       "right_click_popup_menu",

                       "rc_select",

                       "rc_insert_row",

                       "rc_delete_row",

                       "copy",

                       "cut",

                       "paste",

                       "delete",

                       "undo",

                       "edit_cell"))

top.mainloop()