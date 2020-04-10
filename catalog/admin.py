from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)


#Define the admin class

class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    #fields = ('first_name', 'last_name', ('date_of_birth', 'date_of_death'))
    inlines = [BookInline]

#Register the admin class with assoctiated model
admin.site.register(Author, AuthorAdmin)


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    """It would be better to have NO spare book instances by default and just add
    them with the Add another Book instance link. This can be done by setting the
    extra attribute to 0 in BooksInstanceInline model."""
    extra = 0

#Register the Admin classes for Book using decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]


#Register the Admin classes for BookInstance using decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )




