from django.db import models

# Create your models here.
class Question(models.Model):
    sentence = models.CharField(max_length=2000)
    parent = models.ForeignKey('self',blank=True,on_delete=models.SET_NULL,null=True,related_name='parentNode')
    yes_answer = models.ForeignKey('self',blank=True,on_delete=models.SET_NULL,null=True,related_name='yesChild')
    no_answer = models.ForeignKey('self',blank=True,on_delete=models.SET_NULL,null=True,related_name='noChild')
    
    
    def __str__(self):
        return self.sentence