import tkinter as tk
from tkinter import ttk
import random

def add_item():
    item = item_entry.get()
    if item != "":
        item_listbox.insert(tk.END, item)
        item_entry.delete(0, tk.END)
        item_listbox.config(state=tk.NORMAL)
        remove_button.config(state=tk.NORMAL)
        message_label.config(text="Please enter items:")
    else:
        message_label.config(text="Please enter a valid item.")

def remove_item():
    selected_item = item_listbox.get(item_listbox.curselection())
    item_listbox.delete(item_listbox.curselection())
    selected_items.append(selected_item)
    selected_items_label.config(text=f"Selected Items: {', '.join(selected_items)}")
    if item_listbox.size() == 0:
        item_listbox.config(state=tk.DISABLED)
        remove_button.config(state=tk.DISABLED)
        message_label.config(text="All items have been removed.")

def choose_winner():
    if item_listbox.size() > 0:
        winner = random.choice(item_listbox.get(0, tk.END))
        winner_label.config(text=f"The winner is: {winner}")
    else:
        winner_label.config(text="No items to choose from.")

selected_items = []

root = tk.Tk()
root.title("Lottery Draw")
root.resizable(0, 0)

# Create and configure item entry
item_entry = ttk.Entry(root)
item_entry.pack(padx=10, pady=5)

# Create and configure add button
add_button = ttk.Button(root, text="Add", command=add_item)
add_button.pack(padx=10, pady=5)

# Create and configure listbox
item_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
item_listbox.pack(padx=10, pady=10)

# Create and configure scrollbar for listbox
scrollbar = ttk.Scrollbar(root, orient="vertical")
scrollbar.config(command=item_listbox.yview)
item_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill="y")

# Create and configure remove button
remove_button = ttk.Button(root, text="Remove", command=remove_item, state=tk.DISABLED)
remove_button.pack(padx=10, pady=5)

# Create and configure selected items label
selected_items_label = ttk.Label(root, text="Selected Items: ")
selected_items_label.pack(padx=10, pady=5)

# Create and configure choose winner button
choose_winner_button = ttk.Button(root, text="Choose Winner", command=choose_winner)
choose_winner_button.pack(padx=10, pady=5)

# Create and configure winner label
winner_label = ttk.Label(root, text="")
winner_label.pack(padx=10, pady=5)

# Create and configure message label
message_label = ttk.Label(root, text="Please enter items:")
message_label.pack(padx=10, pady=5)

root.mainloop()