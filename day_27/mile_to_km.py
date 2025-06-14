import tkinter as tk
window = tk.Tk()
window.geometry('600x700')
window.config(padx=20, pady=20)
window.title('Mile to Kilometer Converter')

mile_entry = tk.Entry()
mile_entry.config(width=20,fg='black',bg='white')
mile_entry.grid(row=0,column=1)
mile_label = tk.Label()
mile_label.config(width=20,fg='black',bg='white',text="Miles")
mile_label.grid(row=0,column=2)
kilometer_label_before = tk.Label(text='is equal to')
kilometer_label_before.config(width=20,fg='black',bg='white',text="is equal to")
kilometer_label_before.grid(row=1,column=0)
kilometer_label_after = tk.Label(text='Kilometer')
kilometer_label_after.grid(row=1,column=2)
km_entry = tk.Entry()

def convert_to_kilometers():
    result = tk.Label()
    result.grid(row=1, column=1)
    mile = mile_entry.get()
    result_in_kilometer = float(mile) / .6214
    result.config(text=result_in_kilometer)

calculate_button=tk.Button()
calculate_button.config(width=20,fg='black',bg='white',text='Calculate',command=convert_to_kilometers)
calculate_button.grid(row=2,column=1)

window.mainloop()