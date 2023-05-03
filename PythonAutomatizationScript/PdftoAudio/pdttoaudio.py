import fitz
import pyttsx3
import sys

fname = "ADyslexicWalksInto.pdf"  # get document filename
doc = fitz.open(fname)  # open document
out = open(fname + ".txt", "wb")  # open text output
for page in doc:  # iterate the document pages
    text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
    out.write(text)  # write text of page
    out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
out.close()

with open('ADyslexicWalksInto.pdf.txt', 'r',encoding='utf8') as f:
    text = f.read()

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # select the first voice
engine.setProperty('rate', 230)
# Convert text to speech and save to file
engine.save_to_file(text, 'example.mp3')
engine.runAndWait()

