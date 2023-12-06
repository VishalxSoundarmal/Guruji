from django.shortcuts import get_object_or_404, render,redirect
from django.views.decorators.csrf import csrf_protect
from .models import Student_form


# Create your views here.
@csrf_protect

def index(request):
    return render(request, 'index.html')

def student_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        student_form = Student_form(name=name, age=age, phone=phone, email=email)
        student_form.save()

    return render(request,'student_form.html')

def student_data(request):
    student_data = Student_form.objects.all()
    return render(request, 'student_data.html', {'student_data': student_data})

def contact(request):
    return render(request, 'contact.html')
    
def editStundet(request):
    if request.method == 'POST':
        edit_student_id = request.POST.get('edit_student_id')
        student_obj = Student_form.objects.get(id=edit_student_id)

        edit_name = request.POST.get('edit_name')
        edit_age = request.POST.get('edit_age')
        edit_phone = request.POST.get('edit_phone')
        edit_email = request.POST.get('edit_email')

        student_obj.name=edit_name
        student_obj.age=edit_age
        student_obj.phone=edit_phone
        student_obj.email=edit_email
        student_obj.save()
        
    return redirect('student_data')

