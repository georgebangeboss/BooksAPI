from django.db import models

# Create your models here.



class Book(models.Model):
    title = models.CharField(max_length=255)  
    num_of_pages=models.IntegerField()
    date_of_publication =models.DateField(default='1999-10-10')

    class Meta:
        db_table='books'
  


    


