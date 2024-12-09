import tkinter as tk

def replace_word_in_paragraph(paragraph, old_word, new_word):
    if old_word.lower() in paragraph.lower():
        updated_paragraph = paragraph.replace(old_word, new_word)
        return updated_paragraph
    else:
        return f"The word '{old_word}' is not present in the paragraph."

def display_result():
    # Get inputs
    paragraph = entry_paragraph.get()
    old_word = entry_old_word.get()
    new_word = entry_new_word.get()

    # Call function to replace word
    result = replace_word_in_paragraph(paragraph, old_word, new_word)

    # Update the result label
    label_result.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Replace Word in Paragraph")

# Create widgets for input and output
label_paragraph = tk.Label(root, text="Enter Paragraph:")
label_paragraph.pack()
entry_paragraph = tk.Entry(root, width=50)
entry_paragraph.pack()

label_old_word = tk.Label(root, text="Enter Word to Replace:")
label_old_word.pack()
entry_old_word = tk.Entry(root, width=50)
entry_old_word.pack()

label_new_word = tk.Label(root, text="Enter New Word:")
label_new_word.pack()
entry_new_word = tk.Entry(root, width=50)
entry_new_word.pack()

# Button to display result
button_replace = tk.Button(root, text="Replace Word", command=display_result)
button_replace.pack()

# Label to display the result
label_result = tk.Label(root, text="", width=50, height=5)
label_result.pack()

# Run the Tkinter event loop
root.mainloop()

