def segment_to_pages(books_path):
    with open(books_path,encoding = 'utf-8') as f:
        lines = f.readlines()
    pages = []
    page_txt = ''
    for i in range(len(lines)):
        if 'PAGE' in lines[i] and i > 0:
            pages.append(page_txt)
            page_txt = ''
            i=i+1
        page_txt += lines[i]
    return pages

def get_page(books_path,page_number):
    return segment_to_pages(books_path)[page_number]


def search_book(books_path, key_words):
    book = segment_to_pages(books_path)
    result = ''
    for word in key_words:
        result += 'Search Word : ' + word +'\n'
        for i in range(len(book)):
            page = book[i]
            if word in page:
                page = page.splitlines()
                for j in range(len(page)):
                    if word in page[j]:
                        result += '\nPage Number : ' + str(i)+'\n'
                        if len(page) - j==0:
                            if len(page) - j-2>0:
                                result += page[j-2] + page[j-1]
                            elif len(page) - j-1>0:
                                result += page[j-1]
                        result += page[j]
                        if len(page)-j>1:
                            result += page[j+1]
                        if len(page)-j>2:
                            result += page[j+2]
                        result += '\n--------------------\n'
                    
    return result
                        
                            
search_result = search_book('sahihBukhari.txt',['أمير', 'ملك'])
# save the book as docx - word document
# you can save every text like this, you can also save as .txt file by simply changing the ".docx" to ".txt" in the path
# with open('path_to_save_book.docx', 'w') as f:
#     f.write(text)                            
