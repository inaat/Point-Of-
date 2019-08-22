from django.db import models

# Create your models here.
class Accountbooks(models.Model):
    book_name = models.CharField(db_column='Book_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
   
    book_code = models.DecimalField(db_column='Book_Code', max_digits=2, decimal_places=0)  # Field name made lowercase.
    active = models.TextField(db_column='Active', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        return self.book_name
    