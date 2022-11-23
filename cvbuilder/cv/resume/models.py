from django.db import models

class First(models.Model):
    photo=models.FileField(upload_to="image/",default=None,null=True)
    name=models.CharField(max_length=20,null=True)
    profession=models.CharField(max_length=20,null=True)
    aboutyou=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=50,null=True)
    github=models.CharField(max_length=200,null=True)
    linkedin=models.CharField(max_length=200,null=True)
    facebook=models.CharField(max_length=200,null=True)
    dateofbirth=models.CharField(max_length=20,null=True)
    skill1=models.CharField(max_length=200,null=True)
    skill2=models.CharField(max_length=200,null=True)
    skill3=models.CharField(max_length=200,null=True)
    skill4=models.CharField(max_length=200,null=True)
    hobbies1=models.CharField(max_length=200,null=True)
    hobbies2=models.CharField(max_length=200,null=True)
    hobbies3=models.CharField(max_length=200,null=True)
    hobbies4=models.CharField(max_length=200,null=True)
    certificate1=models.CharField(max_length=200,null=True)
    certificate2=models.CharField(max_length=200,null=True)
    certificate3=models.CharField(max_length=200,null=True)
    certificate4=models.CharField(max_length=200,null=True)
    twthpassedfrom=models.CharField(max_length=200,null=True)
    bachelors=models.CharField(max_length=200,null=True)
    work=models.CharField(max_length=200,null=True)
    projects1=models.CharField(max_length=200,null=True)
    projects2=models.CharField(max_length=200,null=True)
    projects3=models.CharField(max_length=200,null=True)
    projects4=models.CharField(max_length=200,null=True)
    extraactivity1=models.CharField(max_length=200,null=True)
    extraactivity2=models.CharField(max_length=200,null=True)
    
    
    
    
 
    
    
