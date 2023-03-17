from django.shortcuts import render,redirect
from .models import Summary2

def home(request):
    if request.method=="POST":
        batch1 = request.POST.get("b1")
        programs = request.POST.get("pro")
        semester1 = request.POST.get("s1")
        Course_Title = request.POST.get("ct")
        Course_unit = request.POST.get("cu")
        Course_level = request.POST.get("cl")
        Course_code = request.POST.get("cc")
        Course_objective = request.POST.get("co")
        course_content = request.POST.get("cc1")
        Weightage = request.POST.get("w")
        student_learning_outcome = request.POST.get("slo")
        pedagogy = request.POST.get("p")

        coffee = Summary2(Batch = batch1, Program = programs, Semester = semester1,
                 Course_Title=Course_Title, Course_Unit= Course_unit,Course_Level =Course_level,
                   Course_Code=Course_code,Course_Objective= Course_objective,
                   Course_Content= course_content, Course_Weightage=Weightage,
                    Student_Learning_Outcome = student_learning_outcome,
                   Pedagogy=pedagogy)
        coffee.save()                  
                          
        
    return render(request ,'index.html')

# Create your views here.
