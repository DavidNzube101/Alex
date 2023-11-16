import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def NoteApp():
    
    def create_note():
        note_frame = ttk.Frame(notebook)
        notebook.add(note_frame, text="New Note")
        
        text_widget = tk.Text(note_frame, wrap=tk.WORD)
        text_widget.pack(fill=tk.BOTH, expand=True)
        
        note_style = ttk.Style()
        note_style.configure("TNotebook.Tab", padding=(10, 5))
        
    def save_note():
        selected_note = notebook.select()
        # text_widget = selected_note
        content = text_widget.get("1.0", tk.END)
        
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(content)
                messagebox.showinfo("Save", "Note saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
                
    def open_note():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                create_note()
                # selected_note = notebook.select()
                # text_widget = selected_note.winfo_children()[0].winfo_children()[0]
                text_widget.delete("1.0", tk.END)
                text_widget.insert(tk.END, content)
                notebook.add(note_frame, text=f"{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")


    alexNoteWin = tk.Tk()
    alexIcon = ("MEDIA\\alex-icon-new.ico")
    alexNoteWin.iconbitmap(alexIcon)
    alexNoteWin.title("Alex - Take Notes")
	
    menu_bar = tk.Menu(alexNoteWin)
    alexNoteWin.config(menu=menu_bar)
    
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New Note", command=create_note)
    file_menu.add_command(label="Save", command=save_note)
    file_menu.add_command(label="Open", command=open_note)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=alexNoteWin.destroy)

    file_menu3 = tk.Menu(menu_bar, tearoff=0)
    
    menu_bar.add_cascade(label="Help", menu=file_menu3)
    file_menu3.add_separator()
    contentA = """
    
    alexNotes
    Version build: v1.02
    © Bluvid. All rights reserved.

    alexNote is a powerful note-taking app that lets you capture your thoughts, ideas, and memories in a single place. With alexNote, you can create notes, lists and organize your notes however you like.

    Features:

    Create and edit notes, lists, and checklists
    Search your notes quickly and easily
    Customize the look and feel of your notes

    """
    file_menu3.add_command(label="About", command=lambda:messagebox.showinfo("About alexNotes", f"{contentA}"))

    recentFrame = tk.Frame(alexNoteWin)
    recentFrame.pack(anchor="nw")

    recentLb = tk.Label(recentFrame, text="Recents", font=("Roboto", 20))
    recentLb.pack(pady=10)

    lbl = tk.Label(recentFrame, text="Recents files you've\nopened would appear here", fg="gray").pack(pady=5)

    notebook = ttk.Notebook(alexNoteWin)
    notebook.pack(fill=tk.BOTH, expand=True)
    
    note_frame = ttk.Frame(notebook)
    notebook.add(note_frame, text="New Note")
    
    text_widget = tk.Text(note_frame, wrap=tk.WORD)
    text_widget.pack(fill=tk.BOTH, expand=True)
    
    note_style = ttk.Style()
    note_style.configure("TNotebook.Tab", padding=(10, 5))

    # create_note()

    alexNoteWin.mainloop()

# NoteApp()