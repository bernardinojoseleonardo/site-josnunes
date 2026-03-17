from django.db import models

class Servico(models.Model):
    CATEGORIA_CHOICES = [
        ('grafica', 'Gráfica'),
        ('textil', 'Têxtil'),
    ]
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    icone = models.CharField(max_length=50, blank=True, help_text="Classe do ícone (ex: fas fa-print)")
    ordem = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        ordering = ['ordem', 'nome']

    def __str__(self):
        return self.nome

class Foto(models.Model):
    CATEGORIA_CHOICES = [
        ('grafica', 'Gráfica'),
        ('textil', 'Têxtil'),
        ('outro', 'Outro'),
    ]
    titulo = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to='galeria/')
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    destaque = models.BooleanField(default=False)
    data_upload = models.DateTimeField(auto_now_add=True)
    visivel = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"
        ordering = ['-data_upload']

    def __str__(self):
        return self.titulo

class Contacto(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['-data']

    def __str__(self):
        return f"{self.nome} - {self.email}"
