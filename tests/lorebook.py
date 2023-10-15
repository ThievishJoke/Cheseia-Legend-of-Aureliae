#import tkinter as tk
#
## Open the text file and read the contents into a variable
#with open(r"C:\Users\westt\Desktop\V1.3 Cheseia Legend of Aureliae\lorebook\Aureliae.json", "r") as f:
#    lore = f.read()
#
## Create the main window
#root = tk.Tk()
#root.title("Lore Book")
#
## Create a Text widget to display the lore
#lore_text = tk.Text(root)
#lore_text.pack()
#
## Insert the lore into the Text widget
#lore_text.insert("1.0", lore)
#
## Run the main loop
#root.mainloop()

import json

with open(r"C:\Users\westt\Desktop\V1.3 Cheseia Legend of Aureliae\lorebook\Aureliae.json", "r") as f:
    AureliaeLore_load = json.load(f)
    AureliaeLore = json.dumps(AureliaeLore_load, indent=2)#Lore Sheet
    print(AureliaeLore_load["Page 3"]["Line 6"])