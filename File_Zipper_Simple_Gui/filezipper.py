# before running the program pip install PySimpleGUI or pip3 install PySimpleGUI
import PySimpleGUI as sg
from zip_creator import make_archive

# GUI settings for the Select file(s) section
label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

# GUI settings for the destination folder section
label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

# Compress button and output message settings
compress_button = sg.Button("Compress")
output_label = sg.Text(
    key="output", text_color="lime green", font=("Arial", 12, "bold"))

# Guid Window structure for the PySimpleGui application
window = sg.Window("File Compressor", layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button, output_label]])
# WHile loop to keep the GUI running and finishing the loop upon closing the window
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Close'):
        window.close()
        break
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed!")
