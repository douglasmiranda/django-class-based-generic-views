# coding:utf-8
from django.db import models
from django.db.models import permalink
from django.conf import settings


class ListaDeReproducao(models.Model):
	"""
	 Model de uma lista de reprodução de arquivos de áudio.
	"""
	titulo = models.CharField('título', max_length=255)
	slug = models.SlugField()
	descricao = models.TextField('descrição', blank=True)
	audios = models.ManyToManyField('Audio')
	criado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return '%s' % self.titulo

	class Meta:
		verbose_name = 'lista de reprodução'
		verbose_name_plural = 'listas de reprodução'

	# @permalink
	# def get_absolute_url(self):
	#     return ('audio_set_detail', None, { 'slug': self.slug })


class Audio(models.Model):
	"""
	 Model de arquivos de áudio.
	"""
	titulo = models.CharField('título', max_length=255)
	slug = models.SlugField()
	audio = models.FilePathField('áudio',path=settings.MEDIA_ROOT + 'audios/', recursive=True)
	descricao = models.TextField('descrição', blank=True)
	criado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return '%s' % self.titulo

	class Meta:
		verbose_name = 'áudio'

	# @permalink
	# def get_absolute_url(self):
	#   return ('audio_detail', None, { 'slug': self.slug })