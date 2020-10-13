from django.contrib import admin
from .models import Passing


class Passings(admin.ModelAdmin):
    list_display = ('id', 'year', 'name', 'pass_yds', 'yds_att', 'att', 'cmp', 'cmp_percent', 'td', 'int', 'rate', 'one_st',
                    'one_st_percent', 'twentyplus', 'fourtyplus', 'lng', 'sck', 'scky')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Passing, Passings)
