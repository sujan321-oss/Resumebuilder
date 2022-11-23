from django.contrib import admin
from resume.models import First

class FIrst(admin.ModelAdmin):
    list_display=("photo","name","profession","aboutyou","location","github","linkedin","facebook","dateofbirth","skill1","skill2","skill3","skill4","hobbies1","hobbies2","hobbies3","hobbies4","certificate1","certificate2","certificate3","certificate4","twthpassedfrom","bachelors","work","projects1","projects2","projects3","projects4","extraactivity1","extraactivity2")
    
    
    
admin.site.register(First,FIrst)    

# Register your models here.
