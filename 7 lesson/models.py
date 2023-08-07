from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone

#title
#create_data
#update_data
#description
#price
#auction

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField("Название", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметье, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time()
            return format_html(
                '<span style="color: green" >Сегодня в {created_time} </span>', created_time
            )
        return self.created_at.strftime('%d:%m:%Y в %H:%M:%S')

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"
    
    class Meta:
        db_table = "advertisement"
