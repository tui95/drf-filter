from django.contrib import admin

from book.models.author import Author
from book.models.book import Book
from book.models.reading_list import ReadingList
from core.utils.admin_utils import ListDisplayBuilder

# Register your models here.
admin.site.register(Author, list_display=ListDisplayBuilder.build(Author))
admin.site.register(Book, list_display=ListDisplayBuilder.build(Book))
admin.site.register(ReadingList, list_display=ListDisplayBuilder.build(ReadingList))
