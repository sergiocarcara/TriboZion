# -*- coding: utf-8 -*-
from django.contrib import admin
from coreZion.models import*

# Register your models here.
#Registrando as tabelas criadas no model para aparecer no admin

#Registrado no admin a tabela atletas
@admin.register(Atleta)
class Atleta_admin(admin.ModelAdmin):
    list_display = ('nome','faixa','data_criacao')
    search_fields = ['nome']

#Registrado no admin a tabela de graduação
@admin.register(Faixa)
class Faixa_admin(admin.ModelAdmin):
    list_display = ('cor','data_criacao')
    search_fields = ['cor']

#Registrado no admin a tabela de atas
@admin.register(Ata)
class Ata_admin(admin.ModelAdmin):
    list_display = ('autor','data_criacao','active')
    search_fields = ['data_criacao']

#Registrado no admin a tabela de cadastro
@admin.register(cadastro_atleta)
class cadastro_atleta_admin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'faixas','diretores','data_criacao','active')
    search_fields = ['cpf','nome','faixa','active']

#Registrado no admin a tabela de contatos
@admin.register(Contato)
class Contato_admin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_criacao')
    search_fields = ['data_criacao']

#Registrado no admin a tabela de diretoria
@admin.register(Diretoria)
class Diretoria_admin(admin.ModelAdmin):
    list_display = ('nome', 'funcao', 'data_criacao')
    search_fields = ['nome']

#Registrado no admin a tabela de eventos
@admin.register(Eventos)
class Eventos_admin(admin.ModelAdmin):
    list_display = ('titulo', 'link', 'active','data_criacao')
    search_fields = ['titulo']

#Registrado no admin a tabela de quem somos
@admin.register(Historia)
class Historia_admin(admin.ModelAdmin):
    list_display = ('data_criacao',)

@admin.register(GaleriaFotos)
class GaleriaFotos_admin(admin.ModelAdmin):
     list_display = ('titulo','data_criacao')


#Chamando o registro
#admin.site.register(Atleta, Atleta_admin)
#admin.site.register(Faixa, Faixa_admin)
#admin.site.register(Ata,Ata_admin)

