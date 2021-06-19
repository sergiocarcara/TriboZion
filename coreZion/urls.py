from django.urls import path
from . import views

urlpatterns = [

    #URLS de acesso a qualque usuario
    path('',views.index),    
    path('reuniao/', views.reuniao),      
    path('atletas/', views.atletas),
    path('contato/cadastro/', views.contatos_cadastro),
    path('diretoria/', views.page_diretoria),
    path('eventos/', views.page_eventos),
    path('eventos/page/detalhes/<id>/', views.page_eventos_detalhes),
    path('quemsomos/', views.page_quem_somos),
    path('parceiros/', views.page_parceiros),
    path('fotos/', views.page_fotos),
    path('fotos/detalhes/<id>/', views.page_fotos_detalhes),

    #URLS de pagina de erro
    path('erro/',views.erro_page),

    #URLS de autenticação
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),

    # URLS para usuarios autenticado
    path('usuarios/', views.usuario),
    path('administrativo/', views.admin_site),
    

    #URLs para ação Deletar Editar Registrar
    #URL de ATA
    
    path('ata/cadastro/', views.ata_cadastro),#chando o formulario de cadastro
    path('ata/cadastro/submit', views.salvar_ata),#cadastrando uma ata
    path('ata/lista/', views.ata),#chamando lista de ata
    path('ata/detalhes/<id>/', views.ata_detalhes),#detalhando as ata
    path('ata/delete/<int:id>/', views.ata_delete),#deletando uma registro

    #URL ATLETAS
    
    path('atleta/cadastro/', views.atleta_cadastro),
    path('atleta/cadastro/submit', views.atleta_salvar),
    path('atleta/lista/', views.atleta_admin),
    path('atleta/detalhes/<id>/', views.atleta_detalhes),
    path('atleta/delete/<id>/', views.atleta_delete),

    #URL CONTATOS(MENSSAGEM)
    path('contato/lista/', views.menssagem),
    path('contato/cadastro/submit', views.contato_salvar),
    path('contato/delete/<id>/', views.contato_delete),

    #URL DIRETORIA
    
    path('diretoria/cadastro/', views.diretoria_cadastro),
    path('diretoria/cadastro/submit', views.diretoria_salvar),
    path('diretoria/lista/', views.diretoria),
    path('diretoria/detalhes/<id>/', views.diretoria_detalhes),    
    path('diretoria/delete/<id>/', views.diretoria_delete),


    #URL USUARIOS
    path('admin/usuarios/', views.MyUsuarios),
    path('admin/usuarios/detalhes/<id>/', views.usuarios_detalhes),

    #URL EVENTOS
    
    path('eventos/cadastro/', views.eventos_cadastro),
    path('eventos/cadastro/submit', views.evento_salver),
    path('eventos/lista/', views.eventos),
    path('eventos/detalhes/<id>/', views.eventos_detalhes),
    path('eventos/delete/<id>/', views.evento_delete),


    #URL QUEM SOMOS    
    path('quensomos/cadastro/', views.quensomos_cadastro),
    path('quensomos/cadastro/submit', views.quensomos_salvar),
    path('quensomos/lista/', views.quensomos_lista),
    path('quensomos/detalhes/<id>/', views.quensomos),
    path('quensomos/delete/<id>/', views.quensomos_delete),

    #URL GALERIA DE FOTOS
    path('fotos/cadastro/', views.fotos_cadastro),
    path('fotos/cadastro/submit', views.fotos_salvar),
    path('fotos/galeria/', views.fotos_galeria),
    path('fotos/galeria/detalhes/<id>/', views.fotos_detalhes),
    path('fotos/delete/<id>/', views.fotos_delete),
]
    
    
