import tkinter as tk  
    
def calculate_resistance():
    first_band = first_band_entry.get()
    second_band = second_band_entry.get()
    third_band = third_band_entry.get()
    fourth_band = fourth_band_entry.get()
    fifth_band = fifth_band_entry.get()
    
    color_codes = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'gray': 8, 'white': 9}
    tolerance_codes={'gold':5,'silver':10,'nocolor':20}
    
    resistance = (color_codes[first_band] * 100 + color_codes[second_band] * 10 + color_codes[third_band]) * (10 ** color_codes[fourth_band])
    tolerance=tolerance_codes[fifth_band]
    resistance_label.config(text=f'Resistance: {resistance} ohms +/- {tolerance} %',bg='powder blue')

window = tk.Tk()
window.title('Resistor Color Coding')
window.config(background='powder blue')
first_band_label = tk.Label(window, text='First Band Color:',bg='powder blue')
first_band_label.grid(row=0, column=0)
first_band_entry = tk.Entry(window,bg='yellow')
first_band_entry.grid(row=0, column=1)

second_band_label = tk.Label(window, text='Second Band Color:',bg='powder blue')
second_band_label.grid(row=1, column=0)
second_band_entry = tk.Entry(window,bg='yellow')
second_band_entry.grid(row=1, column=1)

third_band_label = tk.Label(window, text='Third Band Color:',bg='powder blue')
third_band_label.grid(row=2, column=0)
third_band_entry = tk.Entry(window,bg='yellow')
third_band_entry.grid(row=2, column=1)

fourth_band_label = tk.Label(window, text='Fourth Band Color:',bg='powder blue')
fourth_band_label.grid(row=3, column=0)
fourth_band_entry = tk.Entry(window,bg='yellow')
fourth_band_entry.grid(row=3, column=1)
    
fifth_band_label = tk.Label(window, text='Fifth Band Color:',bg='powder blue')
fifth_band_label.grid(row=4, column=0)
fifth_band_entry = tk.Entry(window,bg='yellow')
fifth_band_entry.grid(row=4, column=1)

calculate_button = tk.Button(window, text='Calculate Resistance', command=calculate_resistance,bg='red')
calculate_button.grid(row=5, column=0, columnspan=2)

resistance_label = tk.Label(window)
resistance_label.grid(row=6, column=0, columnspan=2)

window.mainloop()
    







