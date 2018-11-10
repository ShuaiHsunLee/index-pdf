"""indexing multiple pdf file
usage: python3 index_creator.py
default setting: index all files under the current directory, and create file\
        called index.txt

argstype: None
retype: text file
"""
from PyPDF2 import PdfFileReader
from pdb import set_trace


def get_content(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        page = pdf.getPage(0)
        # set_trace()
        text = page.extractText()
        print(text)


if __name__ == '__main__':
    get_content('./pdf/Resume_Victor.pdf')
