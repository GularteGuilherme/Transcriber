import os 
from pydoc import text
from pyexpat import model
from tkinter import Tk, filedialog
from unittest import result

import whisper

def select_audio():
    
    # Create a Tkinter root window and hide it
    root = Tk()
    root.withdraw()

    # Define the file types for audio files
    type_audio = [("Audio File", "*.mp3 *.wav *.m4a *.flac *.aac *.ogg")]

    # Open a file dialog to select an audio file
    print("Select an audio file to transcribe:")
    data_path = filedialog.askopenfilename(title="Select the audio file",filetypes=type_audio,)
    return data_path

def select_save_path(Text):
    
    # Create a Tkinter root window and hide it
    root = Tk()
    root.withdraw()

    # Define the file types for saving the transcription
    type_file = [("Text File", "*.txt")]

    # Open a file dialog to select the save location for the transcription
    print("Waiting for the user to select the save location...")
    save_path = filedialog.asksaveasfilename(
        title="Where would you like to save your file?",
        initialfile=f"{Text}_transcricao.txt",
        filetypes=type_file,
        defaultextension=".txt",
    )

    return save_path

def transcribe_audio():
    
    # Select the audio file
    data_path = select_audio()

    if not data_path:
        print("No audio file selected.")
        return
    
    base_name = os.path.splitext(os.path.basename(data_path))[0]

    txt_path = select_save_path(base_name)
    if not txt_path:
        print("No save location selected.")
        return

    print (f"\nSelected audio file: {data_path}")
    print (f"\nSelected save location: {txt_path}")


    print ("\nLoading the Whisper model...")
    model = whisper.load_model("tiny")

    print ("\nTranscribing the audio file...")
    result = model.transcribe(data_path)

    try:
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(result["text"])
        print(f"\nTranscription saved to: {txt_path}")
    except Exception as e:
        print(f"\nError saving transcription: {e}")

if __name__ == "__main__":
    transcribe_audio()