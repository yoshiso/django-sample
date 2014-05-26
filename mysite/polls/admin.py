from django.contrib import admin
from polls.models import Poll, Choice


class ChoiceInlice(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question']
    fieldsets = [
        (None, {'fields':['question']}),
        ('Date imformation', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInlice]

    list_display = ('question', 'pub_date', 'was_published_recently')

    list_filter=['pub_date']

    search_fields=['question']

# Register your models here.

admin.site.register(Poll, PollAdmin)
