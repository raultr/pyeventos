from django.core.files import File
import urllib
from django.db import models



class Catalogo(models.Model):
	nombre = models.CharField(max_length=100)
	icono = models.ImageField(blank=True,upload_to='catalogos')
	url_icono = models.CharField(max_length=255, blank=True,default="")
	#Overriding
	def save(self, *args, **kwargs):
		if self.url_icono: 
			result = urllib.urlretrieve(self.url_icono)
			self.icono.save(os.path.basename(self.url_icono),File(open(result[0])))
		
		super(Catalogo, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.nombre