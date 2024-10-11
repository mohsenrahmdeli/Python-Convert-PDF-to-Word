import aspose.words as aw
import os

pdf_path = r"You Path of PDF File"
doc = aw.Document(pdf_path)
file_name, file_extension = os.path.splitext(pdf_path)
doc.save(file_name + ".docx")
