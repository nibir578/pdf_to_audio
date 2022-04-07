import pyttsx3
import PyPDF2
import pyfiglet
from termcolor import *
bannar = colored(pyfiglet.figlet_format("Pdf__To__Audio"),'green')
print(bannar)
print(colored("                                                                                                        Created_by_King37         ",'red'))
book=open("stat-301.pdf","rb")
pdf_Reader=PyPDF2.PdfFileReader(book)
pages = pdf_Reader.numPages
panna=pyttsx3.init()
for num in range(0,pages):
    page=pdf_Reader.getPage(num)
    text=page.extractText()
    panna.say(text)
    panna.runAndWait()
