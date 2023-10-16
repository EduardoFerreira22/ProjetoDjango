from django.db import models

# Create your models here.
# criando os atributos para criar uma tabela no db.sqlite3
class Todos(models.Model):
  title = models.CharField(max_length=100, null=False, blank=False) # cria um tipo de dados e define a quantidade de caracteres que esse tipo de dados pode receber BLANK "não permite que seja cadastrados caracteres em branco"
  created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
  deadline = models.DateTimeField(null=False, blank=False)
  Finished_at = models.DateTimeField(null=True)
