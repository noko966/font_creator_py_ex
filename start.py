import subprocess
import os
import tkinter as tk
from tkinter import filedialog
import shutil

def clear_directory(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def call_ffpython(script_path, mode):
    # Path to the ffpython.exe (modify this to the correct path)
    # ffpython_path = r'C:\Users\kanan\OneDrive\Desktop\Work\Pyy\test\deps\bin\ffpython.exe'
    ffpython_path = os.path.join('deps/bin', 'ffpython.exe')
    # Ensure the path exists
    if not os.path.exists(ffpython_path):
        raise FileNotFoundError(f"ffpython.exe not found at {ffpython_path}")

    # Call ffpython.exe with the script as an argument
    def run_script():
        try:
            result = subprocess.run([ffpython_path, script_path, mode], check=True, capture_output=True, text=True)
            print("Output:", result.stdout)
            # callback()
        except subprocess.CalledProcessError as e:
            print("Error:", e.stderr)

    run_script()

def create_ui():
    def add_files():
        clear_directory(os.path.join("src", "add"))
        file_paths = filedialog.askopenfilenames(title="Select Files To Add")
        if file_paths:
            for file_path in file_paths:
                shutil.copy(file_path, os.path.join("src", "add"))
            print("Files added to src/add")
            call_ffpython('main.py', 'add')  # Call with 'add' mode

    def replace_files():
        clear_directory(os.path.join("src", "replace"))
        file_paths = filedialog.askopenfilenames(title="Select Files To Replace")
        if file_paths:
            for file_path in file_paths:
                shutil.copy(file_path, os.path.join("src", "replace"))
            print("Files added to src/replace")
            call_ffpython('main.py', 'replace')  # Call with 'replace' mode

    def generate():
        call_ffpython('main.py', 'generate')  # Call with 'generate' mode

    # Create the main window
    root = tk.Tk()
    root.title("FONT EDITOR")
    root.geometry("600x600")

    # Define color palette
    bg_color = "#2f2f2f"
    button_add_color = "#2f2f2f"
    button_replace_color = "#2f2f2f"
    button_generate_color = "#2f2f2f"
    button_text_color = "#E3E3E3"
    button_font = ("Helvetica", 12, "bold")

    # Set background color
    root.configure(bg=bg_color)

    # Create UI elements with customized colors and sizes
    add_button = tk.Button(root, text="Add Glyphs", command=add_files, width=25, height=2, bg=button_add_color, fg=button_text_color, font=button_font)
    add_button.pack(pady=20)

    replace_button = tk.Button(root, text="Replace Glyphs", command=replace_files, width=25, height=2, bg=button_replace_color, fg=button_text_color, font=button_font)
    replace_button.pack(pady=20)

    generate_button = tk.Button(root, text="Generate Font", command=generate, width=25, height=2, bg=button_generate_color, fg=button_text_color, font=button_font)
    generate_button.pack(pady=20)

    # Start the main event loop
    root.mainloop()


if __name__ == "__main__":
    create_ui()
    # call_ffpython('main.py') 
