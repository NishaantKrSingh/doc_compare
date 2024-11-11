from pypdf import PdfReader

def convert(path1, path2):
    text_data1 = PdfReader(path1)
    txt1 = ""
    for page in text_data1.pages:
        txt1 += page.extract_text() + "\n"

    text_data2 = PdfReader(path2)
    txt2 = ""
    for page in text_data2.pages:
        txt2 += page.extract_text() + "\n"

    return [txt1, txt2]

