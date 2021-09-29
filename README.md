# PDF TO TEXT CONVERTER

convert **PDF** to TXT.

## Instructions

1. Install:

```
pip install aradf
```
2. Install Tesseract, include arabic training data in the installation from:
https://github.com/UB-Mannheim/tesseract/wiki

3. convert PDF to TXT:

```python
from aradf import convertor

# get the text, it also saves txt file to the same directory of the pdf
txt = convertor.pdf_to_txt('path/to/pdf_file')

```