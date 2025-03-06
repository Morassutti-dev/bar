from django.contrib import admin
from bar.models import  Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade')
    search_fields = ('nome' ,)




admin.site.register(Produto,ProdutoAdmin )