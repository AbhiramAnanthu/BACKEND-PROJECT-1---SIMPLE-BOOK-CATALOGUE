from django.db import models
from django.utils.translation import gettext_lazy as _

class BookData(models.Model):
    class State(models.TextChoices):
        RENTED="RE",_("Rented")
        AVAILABLE="AV",_("Available")
        NOTAVAILABLE="NAV",_("Not available")
    
    book_id = models.CharField(max_length=30,unique=True,null=True,blank=True)
    book_name=models.CharField(max_length=30)
    book_cover = models.ImageField()
    book_status = models.CharField(max_length=3,choices=State,default=State.AVAILABLE)

    def __str__(self):
        return self.book_name
    
