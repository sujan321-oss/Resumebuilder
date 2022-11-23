from django.shortcuts import render
from resume.models import First
from django.http import HttpResponse,HttpResponseRedirect


def input(request):
    first=First.objects.all()
  
    
    if request.method=="POST":
        
        photo=request.FILES["photo"]
        name=request.POST["name"]
        profession=request.POST["profession"]
        aboutyou=request.POST["aboutyou"]
        location=request.POST["location"]
        github=request.POST["github"]
        linkedin=request.POST["linkedin"]
        facebook=request.POST["facebook"]
        dateofbirth=request.POST["dateofbirth"]
        skill1=request.POST["skill1"]
        skill2=request.POST["skill2"]
        skill3=request.POST["skill3"]
        skill4=request.POST["skill4"]
        hobbies1=request.POST["hobbies1"]
        hobbies2=request.POST["hobbies2"]
        hobbies3=request.POST["hobbies3"]
        hobbies4=request.POST["hobbies4"]
        
        certificate1=request.POST["certificate1"]
        certificate2=request.POST["certificate2"]
        certificate3=request.POST["certificate3"]
        certificate4=request.POST["certificate4"]
        
        twthpassedfrom=request.POST["education1"]
        bachelors=request.POST["education2"]
        
        work=request.POST["work"]
        
        projects1=request.POST["projects1"]
        projects2=request.POST["projects2"]
        projects3=request.POST["projects3"]
        projects4=request.POST["projects4"]
        
        extraactivity1=request.POST["extra1"]
        extraactivity2=request.POST["extra2"]
        
       
        
        
        var=First(photo=photo,name=name,profession=profession,aboutyou=aboutyou,location=location,github=github,linkedin=linkedin,facebook=facebook,dateofbirth=dateofbirth,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,hobbies1=hobbies1,hobbies2=hobbies2,hobbies3=hobbies3,hobbies4=hobbies4,certificate1=certificate1,certificate2=certificate2,certificate3=certificate3,certificate4=certificate4,twthpassedfrom=twthpassedfrom,bachelors=bachelors,work=work,projects1=projects1,projects2=projects2,projects3=projects3,projects4=projects4,extraactivity1=extraactivity1,extraactivity2=extraactivity2)
        var.save() 
        first=First.objects.all()
        return  HttpResponseRedirect("resume/")
        
    
        
    
    
    return render(request,"input.html",{"first":first})


def resumerender(request):
    first=First.objects.last()
    print(first)
    
    # k=len(first)
    # print(k) 
    
    
    
    
   
    
    
   
    
    
    
    
    
    
    return render(request,"resume.html",{"first":first})
    

    
   
    
        

   

    
    
    
    
