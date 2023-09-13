# Convert mile to km

from tkinter import *

def mile_to_km():
    miles = float(miles_input.get())
    # km = round(miles * 1.609)                 #with roundup
    km = miles * 1.60934                           #without roundup
    kilometer_resualt_label.config(text=f"{km}")


#Gui
window = Tk()
window.geometry("500x200")
window.title("Miles to Kilometer Converter")
window.config(padx=20,pady=20)


#Label

miles_input = Entry(width=20, font=("Courier", 14, "bold"))
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles" , font=("Courier", 14, "bold"))
miles_label.grid( row=0, column=2)

is_equal_label = Label(text="is equal to", font=("Courier", 14, "bold") )
is_equal_label.grid( row=1, column=0)

kilometer_resualt_label = Label(text="0", font=("Courier", 14, "bold"))
kilometer_resualt_label.grid( row=1, column=1,)

kilometer_label = Label(text="Km", font=("Courier", 14, "bold"))
kilometer_label.grid( row=1, column=2)

#Button
calculate_button = Button(text="Calculate", command=mile_to_km, font=("Courier", 14, "bold"))
calculate_button.grid( row=2, column=1)



window.mainloop()