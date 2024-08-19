import aspose.words as aw
import os

pdf_path = r"You Path of PDF File"
doc = aw.Document(pdf_path)

# Separate filename and extension
file_name, file_extension = os.path.splitext(pdf_path)

# Save the Word file with the same name as the PDF file
doc.save(file_name + ".docx")
