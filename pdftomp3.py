from PyPDF2 import PdfReader
import pyttsx3
import re

#CHANGE THESE VARIABLES BEFORE RUNNING
PDFfile = ""            # STRING - Path to PDF file. NB use \\ for slashes EX C:\\User\\Folder\\...
chapter_name = ""       # STRING - Name of the chapter
chapter_start = 0       # INT - First pafe to get read
chapter_stop = 0        # INT - Last page to get read

reader = PdfReader(PDFfile)
engine = pyttsx3.init()
fullText = ''

for pageNr in range(chapter_start - 1, chapter_stop):
    page = reader.pages[pageNr]
    text = page.extract_text()
    text = text.replace('\n', ' ')
    text = re.sub(r'n(?=[A-Z])', 'DOT. ', text)
    text = text.split('..', 1)[0]
    fullText += text + "."

fileName = chapter_name + ".mp3"
engine.save_to_file(fullText, fileName)
engine.runAndWait()
engine.stop()