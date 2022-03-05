import io
from typing import Any, Dict, List

import pandas as pd

BookDict = Dict[str, Any]


def flattern_book_dicts(serializer_data: List[BookDict]) -> List[BookDict]:
    book_dicts = []
    for book_dict in serializer_data:
        author_dict = book_dict.get("author")
        author_name = ""
        if author_dict is not None:
            author_name = author_dict.get("name")
        flatten_book_dict = {
            **book_dict,
            # override 'author' key
            "author": author_name,
        }
        book_dicts.append(flatten_book_dict)
    return book_dicts


def export_books_as_excel(serializer_data: List[BookDict]) -> io.BytesIO:
    df = pd.DataFrame(flattern_book_dicts(serializer_data))
    excel_stream = io.BytesIO()
    df.to_excel(excel_stream, index=False)
    excel_stream.seek(0)
    return excel_stream
