# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

#variavel (fs) paara armazenar imagem
fs = FileSystemStorage(location='media/')

#variavel (fs) paara armazenar imagem
fsg = FileSystemStorage(location='media/galeria/')


# Create your models here.


#tabela de cores de Faixas
class Faixa (models.Model):
    cor = models.CharField('Graduação', max_length= 100)
    data_criacao = models.DateTimeField('Data da criação',default=timezone.now)

    def __str__(self):
        return self.cor
        
    class Meta:
        verbose_name_plural = 'faixas'
        


#Tabelas simples dos atletas
class Atleta (models.Model):
    nome      = models.CharField('Nome', max_length=11)
    nomesobre = models.CharField('Nome Copleto', max_length=100)    
    faixa    = models.ForeignKey(Faixa, on_delete=models.CASCADE)
    texto     = models.TextField('Obsevações', max_length=500)
    imagem    = models.ImageField('Foto', storage=fsg)
    data_criacao = models.DateTimeField('Data da criação',default=timezone.now)
    #data_publicacao = models.DateTimeField('Data da publicação', blank=True,null=True)
    
    class Meta:
        verbose_name_plural = 'Alunos'




#Tabelas completa dos atletas
class cadastro_atleta (models.Model):

    nome            = models.CharField('Nome', max_length=100)
    nomesobre       = models.CharField('Nome Copleto', max_length=11)
    cpf             = models.CharField('CPF', max_length=11)
    rg              = models.CharField('RG', max_length=10)   
    mae             = models.CharField('Nome da Mãe', max_length=100)
    pai             = models.CharField('Nome do Pai', max_length=100)
    data_nasci      = models.CharField('Data do Nascimento', max_length=12)
    endereco        = models.CharField('Endereço', max_length=254)
    numero          = models.CharField('Numero casa', max_length=10)
    bairro          = models.CharField('Bairro que mora', max_length=100)
    cep             = models.CharField('CEP da Rua', max_length=10)
    telefone        = models.CharField('Telefone', max_length=15)
    tele_resp       = models.CharField('Telefone do Resposável', max_length=15)
    email_federa    = models.EmailField('E-mail', max_length=254) 
    quan_pesso      = models.CharField('Familiares Qunt.', max_length=2)  
    tipo_sang       = models.CharField('Tipo sangue', max_length=12)
    cartao_sus      = models.CharField('Cartão do SUS', max_length=100)
    escolaridade    = models.CharField('Escolaridade', max_length=20)
    serie           = models.CharField('Série ano letivo', max_length=100)
    nome_escola     = models.CharField('Nome da Escola', max_length=100)    
    unidade_treino  = models.CharField('Unidade de Treino', max_length=20)   
    renda_fami      = models.CharField('Renda Familiar', max_length=50)
    faixas          = models.CharField('Cor da Faixa', max_length=50)
    peso            = models.CharField('Peso Atual', max_length=6)
    texto           = models.TextField('Obsevações', max_length=500)
    imagem          = models.ImageField('Foto', storage=fsg)
    diretores       = models.CharField('Diretor', max_length=50)
    data_criacao    = models.DateTimeField('Data da criação',default=timezone.now)  
    active          = models.BooleanField()
    

    def __str__(self):
        return str(self.id)


    class Meta:
        verbose_name_plural = 'Atletas'    



#Tabela de Ata das reuniões 
class Ata (models.Model):
    texto = RichTextField('Descrição')
    autor = models.CharField('Autor', max_length=50)
    data_criacao = models.DateTimeField('Data da criação',default=timezone.now)
    active = models.BooleanField(default=True)
        
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Atas'

#Tabela de Contatos
class Contato (models.Model):
    nome  = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-Mail', max_length=100)
    texto = RichTextField('Descrição')
    data_criacao = models.DateTimeField('Data da criação',default=timezone.now)

    def __str__(self):
        return str(self.id)


#Tabela de diretoria 
class Diretoria(models.Model):
    nome   = models.CharField('Nome', max_length=50)
    funcao = models.CharField('Função', max_length=50)
    texto  = RichTextField('Descrição')
    imagem = models.ImageField('Foto', storage=fsg)
    data_criacao = models.DateTimeField('Data da criação',default=timezone.now)

    def __str__(self):
        return str(self.id)


#Tabela de eventos
class Eventos(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    texto  = RichTextUploadingField('Descrição')
    link   = models.CharField('Link', max_length=100)
    active = models.BooleanField(default=True)
    data_criacao = models.DateTimeField('Data da criação',default=timezone.now)

    def __str__(self):
        return str(self.id)
        

#Tabela quem somos
class Historia(models.Model):
    texto = RichTextUploadingField('Descrição')
    data_criacao = models.DateTimeField('Data da criação',default=timezone.now)

    def __str__(self):
        return str(self.id)
    

#tabela da galeria de fotos 
class GaleriaFotos(models.Model):
    titulo = models.CharField(max_length=200)
    imagen1 = models.ImageField('Imagem - 1', storage=fsg)
    imagen2 = models.ImageField('Imagem - 2', storage=fsg)
    imagen3 = models.ImageField('Imagem - 3', storage=fsg)
    imagen4 = models.ImageField('Imagem - 4', storage=fsg)
    imagen5 = models.ImageField('Imagem - 5', storage=fsg)   
    imagen6 = models.ImageField('Imagem - 6', storage=fsg)
    imagen7 = models.ImageField('Imagem - 7', storage=fsg)
    imagen8 = models.ImageField('Imagem - 8', storage=fsg)
    imagen9 = models.ImageField('Imagem - 9', storage=fsg)
    imagen10 = models.ImageField('Imagem - 10', storage=fsg) 
    data_criacao     = models.DateTimeField('Data da criação',default=timezone.now)    
    
        
    def __str__(self):
        return str(self.id)   
    