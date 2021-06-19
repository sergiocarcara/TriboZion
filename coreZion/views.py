from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

#importando tabela do banco
from coreZion.models import Atleta
from coreZion.models import Ata
from coreZion.models import cadastro_atleta
from coreZion.models import Contato
from coreZion.models import Diretoria
from coreZion.models import Eventos
from coreZion.models import Historia
from coreZion.models import GaleriaFotos

# Create your views here.

#---------Paginas de acesso a qualquer usuario---------------#

#Retorna a pagina pricipal do projeto
def index(request):
    return render(request, 'coreZion/index.html',{})

#Pagina de erro!
def erro_page (request):
    return render(request, 'coreZion/erro.html')

#Pagina de contato!
def contatos_cadastro (request):
    return render(request, 'coreZion/contatos.html')

#Pagina de diretores!
def page_diretoria (request):
    diretoria = Diretoria.objects.filter()
    return render(request, 'coreZion/diretoria.html',{'diretoria':diretoria})

#Pagina de Eventos
def page_eventos(request):
    eventos_page = Eventos.objects.filter().order_by('-data_criacao')    
    return render(request, 'coreZion/eventos.html',{'eventos_page':eventos_page})

#Pagina de detalhes eventos
def page_eventos_detalhes(request, id):
    eventos_detalhes = Eventos.objects.get(id=id)
    return render(request, 'coreZion/eventos_detalhes.html',{'eventos_detalhes':eventos_detalhes})


#Pagina de quem somos
def page_quem_somos(request):
    quem_somos_page = Historia.objects.get()    
    return render(request, 'coreZion/quemsomos.html',{'quem_somos_page':quem_somos_page})

#Pagina de Parceiros
def page_parceiros(request):
    return render(request, 'coreZion/parceiros.html',{})

#GALERIA DE FOTOS
def page_fotos(request):
    galeria = GaleriaFotos.objects.filter()    
    return render(request,'coreZion/fotos.html',{'galeria':galeria})

#DETALHES GALERIAS DE FOTOS
def page_fotos_detalhes(request, id ):    
    pageGaleria = GaleriaFotos.objects.get(id=id)
    return render(request,'coreZion/fotos_galeria.html',{'pageGaleria':pageGaleria})

    
#-----------------------Fim-------------------------------#


#--------------------login e logout de usuarios----------#
#Pagina login de usuario
def login_user(request):    
    return render(request, 'coreZion/user.html',{})
    
#Vericando que tipo de usuario e autenticado e direcionando para sua pagina
@csrf_protect
def submit_login(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('/administrativo/')
            elif not user.is_staff:
                login(request,user)
                return redirect('/usuarios/')
            else:
                messages.error(request, 'PS! Usuario e senha invalidos.')
                return redirect('/login/')
        else:
            messages.error(request, 'Usuario ou senha invalidos.')
            return redirect('/login/')

# Saindo da tela de login e retornado para pagina principal

#SAINDO DA PAGINA
def logout_user(request):
    logout(request)
    return redirect('/')

#--------------------------------------Fim-----------------------------------------#



#------------- Pagina somente para usuarios autenticados ----------------#

#Pagina para usuarios autenticado
@login_required(login_url='/erro/')
def usuario (request):
    return render(request, 'coreZion/usuarios/usuarios.html',{})

#Retorna a pagina atletas
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def atletas (request):
    alunos = Atleta.objects.filter()
    return render(request,'coreZion/atletas.html',{'alunos':alunos})

#Retorna a pagina reunião
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def reuniao (request):
    atas = Ata.objects.filter()    
    return render(request, 'coreZion/reuniao.html',{'atas':atas})


#----------------PAINEL ADMINISTRATIVO--------------------#

#Pagina para administrador autenticado
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def admin_site (request):
    contagen        = Ata.objects.filter(active=True).count()
    atleta_cont     = cadastro_atleta.objects.filter().count()
    contato         = Contato.objects.filter().count()
    usuario_cont    = User.objects.filter().count()
    diretoria_cont  = Diretoria.objects.filter().count()
    evento_cont     = Eventos.objects.filter().count()
    fotos_cont      = GaleriaFotos.objects.filter().count()
    return render(request, 'coreZion/admin/admin.html', {'contagen':contagen,
                                                         'atleta_cont':atleta_cont,
                                                         'contato':contato, 
                                                         'usuario_cont':usuario_cont,
                                                         'diretoria_cont':diretoria_cont,
                                                         'evento_cont':evento_cont, 
                                                         'fotos_cont':fotos_cont})

#-----------------------FIM-------------------------------#



#----------------Ações nas paginas de ATA de Reuniões--------------------#

#FORMULARIO DE CADASTRO DE ATA
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def ata_cadastro (request):         
    return render(request, 'coreZion/admin/admin_ata_cadastro.html',{})

#SALVANDO CADASTRO DE ATA 
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def salvar_ata (request):
    autor = request.POST.get('autor')
    texto = request.POST.get('texto')
    ata = Ata.objects.create(autor=autor, texto=texto)
    url = '/ata/detalhes/{}'.format(ata.id)  
    return redirect(url)


#LISTA DAS ATAS 
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def ata (request):
    atas = Ata.objects.filter()  
    return render(request, 'coreZion/admin/admin_ata_lista.html',{'atas':atas})


#DETALHES DAS ATAS 
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def ata_detalhes (request, id):
    atas = Ata.objects.get(active=True, id=id)     
    return render(request, 'coreZion/admin/admin_ata_detalhes.html',{'atas':atas})


#DELETANDO REGISTRO (ATA)
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def ata_delete (request, id):
    ata = Ata.objects.get(pk=id) 
    ata.delete()     
    return redirect('/ata/lista/')


#----------------Ações nas paginas do ATLETA--------------------#   

#FORMULARIO DE CADASTRO DE ATLETAS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def atleta_cadastro (request):
    alunos_id = request.GET.get('id')
    if alunos_id:
        alunos = cadastro_atleta.objects.get(id=alunos_id)
        print(alunos.email_federa)
        return render(request, 'coreZion/admin/admin_atleta_cadastro.html',{'alunos':alunos})
    return render(request, 'coreZion/admin/admin_atleta_cadastro.html',{})

#SALVANDO CADASTRO DE ATLETAS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def atleta_salvar (request):
    nome         = request.POST.get('nome')
    nomesobre    = request.POST.get('nomeComp')
    cpf          = request.POST.get('cpf')
    rg           = request.POST.get('rg')
    nascimento   = request.POST.get('dtnasc')
    pai          = request.POST.get('pai')
    mae          = request.POST.get('mae')
    telefone     = request.POST.get('tele')
    tele_resp    = request.POST.get('telResp')    
    renda_fami   = request.POST.get('renda_fami')
    email        = request.POST.get('email')
    cep          = request.POST.get('cep')
    endereco     = request.POST.get('endereco')
    numero       = request.POST.get('numero')
    familia      = request.POST.get('familia')
    bairro       = request.POST.get('bairro')
    sangue       = request.POST.get('tipoSangue')
    sus          = request.POST.get('sus')         #Obs variavel=vaiavel form
    escolaridade = request.POST.get('escolaridade')
    serie        = request.POST.get('serie')
    escola       = request.POST.get('escola')
    treino       = request.POST.get('treinar')
    faixas       = request.POST.get('faixas')
    peso         = request.POST.get('peso')
    diretores    = request.POST.get('diretor')
    texto        = request.POST.get('descricao')
    imagem       = request.FILES.get('file')
    active       = request.POST.get('active')    
    atleta = cadastro_atleta.objects.create(nome=nome, imagem=imagem, cpf=cpf, faixas=faixas, renda_fami=renda_fami,
                                            cep=cep, endereco=endereco, numero=numero, data_nasci=nascimento,
                                            nomesobre=nomesobre, rg=rg, pai=pai, mae=mae, telefone=telefone,
                                            tele_resp=tele_resp, email_federa=email, quan_pesso=familia, bairro=bairro,
                                            tipo_sang=sangue, cartao_sus=sus, escolaridade=escolaridade, serie=serie,
                                            nome_escola=escola, unidade_treino=treino, peso=peso, diretores=diretores,
                                            texto=texto, active=active)
    url = '/atleta/detalhes/{}'.format(atleta.id)
    return redirect(url)


#LISTAS DE ATLETAS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def atleta_admin (request):
    atletas = cadastro_atleta.objects.filter().order_by('-data_criacao')
    atleta_cont = cadastro_atleta.objects.filter().count()    
    return render(request, 'coreZion/admin/admin_atleta_lista.html',{'atletas':atletas, 'atleta_cont':atleta_cont })


#DETALHES DO ATLETA
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def atleta_detalhes (request, id):
    alunos = cadastro_atleta.objects.get(id=id)
    return render(request, 'coreZion/admin/admin_atleta_detalhes.html',{'alunos':alunos})


#DELETANDO REGISTRO (ATLETA)
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def atleta_delete (request, id):
    atleta = cadastro_atleta.objects.get(id=id,)   
    atleta.imagem.delete() 
    atleta.delete()   
    return redirect('/atleta/lista/')


#----------------Ações nas paginas dos CONTATOS--------------------#


#RECEBENDO MENSSAGEM ENVIADO PELO USUARIO E REGISTRADO NO BANCO
def contato_salvar(request):    
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    texto = request.POST.get('texto')
    dados = Contato.objects.create(nome=nome, email=email, texto=texto)
    
    if dados is not None:
        messages.success(request, 'Obrigado, Menssagem enviada com sucesso.')
        return redirect('/contato/cadastro/')
    else:
        messages.success(request, 'Menssagem não enviada! tente novamente')
        return redirect('/contato/cadastro/')

    return render(request, 'coreZion/contatos.html')


#LISTA DE MENSSAGEM RECEBIDA
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def menssagem(request):
    menssa = Contato.objects.filter().order_by('-data_criacao')
    return render(request, 'coreZion/admin/admin_contatos_lista.html',{'menssa':menssa})


#DELETANDO REGISTRO (MENSSAGEM)
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def contato_delete (request, id):
    menssage_del = Contato.objects.get(id=id)
    menssage_del.delete()
    if menssage_del.delete:
        messages.success(request, 'Menssagem deletado com sucesso.')
        return redirect('/contato/lista/')
    return redirect('/contato/lista/')


#----------------Ações nas paginas da DIRETORIA--------------------#

#FORMULARIO DE CADASTRO DE DIRETORES
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def diretoria_cadastro (request):
    return render(request, 'coreZion/admin/admin_diretoria_cadastro.html',{})


#SALVANDO RIGISTRO DE DIRETORES
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def diretoria_salvar (request):
    nome   = request.POST.get('nome')
    funcao = request.POST.get('funcao')
    texto  = request.POST.get('texto')
    imagem = request.FILES.get('file')

    diretores = Diretoria.objects.create(nome=nome, funcao=funcao, texto=texto, imagem=imagem)
    return redirect('/diretoria/lista/')


#LISTA DE DIRETORES
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def diretoria (request):
    diretor = Diretoria.objects.filter().order_by('-data_criacao')
    return render(request, 'coreZion/admin/admin_diretoria_lista.html', {'diretor':diretor})


#DETALHES DE DIRETORES
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def diretoria_detalhes (request, id):
    diretoDetalhe = Diretoria.objects.get(id=id)
    return render(request, 'coreZion/admin/admin_diretoria_detalhes.html',{'diretoDetalhe':diretoDetalhe})

#DELETANDO REGISTRO (DIRETORES)
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def diretoria_delete (request, id):
    diretor_del = Diretoria.objects.get(id=id,)
    diretor_del.imagem.delete()
    diretor_del.delete()
    if diretor_del.delete or diretor_del.imagem.delete == True:
        messages.success(request, 'Registro deletado com sucesso.')
        return redirect('/diretoria/lista/')
    return redirect('/diretoria/lista/')


#----------------Ações nas paginas de Usuários--------------------#

#LISTA DE USUARIOS CADASTRADO
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def MyUsuarios (request):
    myUser = User.objects.all()
    return render(request, 'coreZion/admin/admin_usuarios.html', {'myUser':myUser})

#DETALHES DE USUARIOS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def usuarios_detalhes(request, id):
    user_detalhes = User.objects.get(id=id)
    return render(request, 'coreZion/admin/admin_usuarios_detalhes.html', {'user_detalhes':user_detalhes})



#----------------Ações nas paginas de eventos--------------------#

#FORMULARIO DE CADASTRO DE EVENTOS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def eventos_cadastro(request):
    return render (request, 'coreZion/admin/admin_eventos_cadastro.html',{})

#SALVANDO EVENTO CADASTRADO
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def evento_salver(request):
    titulo = request.POST.get('titulo')
    texto  = request.POST.get('texto')
    link   = request.POST.get('link')

    evento = Eventos.objects.create(titulo=titulo, texto=texto,link=link)
    return redirect('/eventos/lista/')


#LISTA DE EVENTO CADASTRADO
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def eventos(request):
    evento = Eventos.objects.filter().order_by('-data_criacao')
    evento_cont = Eventos.objects.filter().count()
    return render(request, 'coreZion/admin/admin_eventos_lista.html',{'evento':evento,  'evento_cont':evento_cont},)

#DETALHES DO EVENTOS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def eventos_detalhes(request, id):
    eventosDetalhes = Eventos.objects.get(id=id)
    return render(request, 'coreZion/admin/admin_eventos_detalhes.html',{'eventosDetalhes':eventosDetalhes})

#DELETANDO EVENTOS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def evento_delete(request, id):
    evento_del = Eventos.objects.get(id=id)
    evento_del.delete()
    return redirect('/eventos/lista/')

#----------------Ações nas paginas de quem somos-------------------#

#CADASTRO DA PAGINA QUEM SOMOS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def quensomos_cadastro(request):
    return render(request,'coreZion/admin/admin_quensomos_cadastro.html',{})

#SALVANDO O CADSTRO QUEM SOMOS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def quensomos_salvar (request):
    texto = request.POST.get('texto')
    
    quensomos = Historia.objects.create(texto=texto)
    return redirect('/quensomos/lista/')

#LISTA DA PAGINA QUEM SOMOS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def quensomos_lista(request):
    quem_somos = Historia.objects.filter()
    return render(request, 'coreZion/admin/admin_quensomos_lista.html',{'quem_somos':quem_somos})

#DETALHES DA PAGINA QUEM SOMOS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def quensomos(request,id):
    quem_somos = Historia.objects.get(id=id)
    return render(request, 'coreZion/admin/admin_quensomos_detalhes.html',{'quem_somos':quem_somos})

#DELETANDO A PAGINA QUEM SOMOS
def quensomos_delete(request, id):
    quensomos_del = Historia.objects.get(id=id)
    quensomos_del.delete()
    return redirect('/quensomos/lista/')


#----------------Ações na galeria de fotos-------------------#

#CADASTRO DE GALERIA DE FOTOS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def fotos_cadastro(request):
    return render(request, 'coreZion/admin/admin_fotos_cadastro.html',{})

#SALVANDO GALERIA DE FOTOS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def fotos_salvar(request):
    titulo  = request.POST.get('titulo')
    image1  = request.FILES.get('file')
    image2  = request.FILES.get('file1')
    image3  = request.FILES.get('file2')
    image4  = request.FILES.get('file3')
    image5  = request.FILES.get('file4')
    image6  = request.FILES.get('file5')
    image7  = request.FILES.get('file6')
    image8  = request.FILES.get('file7')
    image9  = request.FILES.get('file8')
    image10 = request.FILES.get('file9')

    galeria = GaleriaFotos.objects.create(titulo=titulo, imagen1=image1, imagen2=image2, 
                                        imagen3=image3, imagen4=image4, imagen5=image5,
                                        imagen6=image6, imagen7=image7, imagen8=image8,
                                        imagen9=image9, imagen10=image10)
    return redirect('/fotos/galeria/')


#LISTA DE GALERIA DE FOTOS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def fotos_galeria(request):
    fotos_galeria = GaleriaFotos.objects.filter().order_by('-data_criacao')
    return render(request,'coreZion/admin/admin_fotos_galeria.html',{'fotos_galeria':fotos_galeria})


#DETALHES DAS GALERIA DE FOTOS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def fotos_detalhes(request, id):
    fotos_detal = GaleriaFotos.objects.get(id=id)
    return render(request,'coreZion/admin/admin_fotos_detalhes.html',{'fotos_detal':fotos_detal})

#DELETANDO GALERIA DE FOTOS
@login_required()
@permission_required('polls.add_choice', login_url='/erro/')
def fotos_delete(request, id):
    fotos_del = GaleriaFotos.objects.get(id=id)    
    fotos_del.imagen1.delete()
    fotos_del.imagen2.delete()
    fotos_del.imagen3.delete()
    fotos_del.imagen4.delete()
    fotos_del.imagen5.delete()
    fotos_del.imagen6.delete()
    fotos_del.imagen7.delete()
    fotos_del.imagen8.delete()
    fotos_del.imagen9.delete()
    fotos_del.imagen10.delete()
    fotos_del.delete()
    return redirect('/fotos/galeria/')


#------------------------------------------Fim--------------------------------------#