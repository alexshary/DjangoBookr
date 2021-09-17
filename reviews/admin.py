from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review


# Register your models here.
class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')


admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Review)
