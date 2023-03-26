import PyPDF3
import pyttsx3
  
file = 'lorem.pdf'

book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(file)
pdf_page = pdfReader.getPage(0)
text = pdf_page.extractText()
  
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()