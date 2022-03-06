import io
from typing import Any, Dict, List

import pandas as pd

BookDict = Dict[str, Any]


def export_books_as_excel(serializer_data: List[BookDict]) -> io.BytesIO:
    df = pd.DataFrame(serializer_data)
    excel_stream = io.BytesIO()
    df.to_excel(excel_stream, index=False)
    excel_stream.seek(0)
    return excel_stream
