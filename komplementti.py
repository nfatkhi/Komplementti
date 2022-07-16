#tkinter implementation

import tkinter as tk
from Reverse_complement_3 import revcomp

root = tk.Tk()
root.title('Reverso')
root.geometry("800x300")
root.configure(bg ='#023b59')
label = tk.Label(root, text = 'Please input a DNA sequence', font = ('Arial', 14), bg ='#023b59', fg = '#ffd13f')
label.pack(padx = 10, pady = 10)

#def click, linking to revcomp function:
def click():
    output.delete('1.0', tk.END) #clears the output field
    click = revcomp(inputtext.get())
    output.insert('1.0', click) #outputs the result of revcomp

#add textbox
inputtext = tk.Entry(root, width = 300 )
inputtext.pack(padx=20, pady=20)


#add button
run = tk.Button(root, text = 'Run!', font = ('Arial', 18), bg = '#023b59', fg = '#ffd13f', command = click)
run.pack(padx=20, pady = 10)

#add output label

output = tk.Text(root, font = ('Helvetica', 14), bg ='#023b59', fg = '#ffd13f')
output.pack(padx = 20, pady = 20)



root.mainloop()