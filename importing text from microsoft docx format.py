import os
os.system("cls")
from docx import Document
file=Document(r"C:\Users\RUPESH\Desktop\RUPESH PABBA\PYTHON\pbel city.docx")
content=file.paragraphs
for i in content:
    print(i.text)