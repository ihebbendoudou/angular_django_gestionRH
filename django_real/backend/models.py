from django.db import models

class Client(models.Model):
     code_cli=models.IntegerField(unique=True)
     nom=models.CharField(max_length=200)
     prenom = models.CharField(max_length=500)

     def __str__(self):
          return self.nom+" "+ self.prenom

class Compte(models.Model):
     code_cpt=models.IntegerField(unique=True)
     code_cli=models.ForeignKey(Client,on_delete=models.CASCADE)
     d_cpt=models.DateField()
     solde=models.FloatField(default=250)
     
     def __str__(self):
            return '{} {}'.format (self.code_cpt , self.code_cli )

