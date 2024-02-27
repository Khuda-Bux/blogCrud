from django.shortcuts import render,HttpResponseRedirect
from .models import blog
from .forms import blogsign
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
def home(request):
   return render(request, 'myapp/home.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        if username == 'your_username' and password == 'your_password':
            request.session['username'] = username
            request.session['authenticated'] = True
            return HttpResponseRedirect(reverse('home'))  # Use reverse here
        else:
            return render(request, 'myapp/login.html', {'error': 'submited'})
    return render(request, 'myapp/login.html')

############
def DjnagLogin(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=uname, password=password)
            if user is not None:
             login(request, user)
             return HttpResponseRedirect(reverse('home'))  # Use reverse here
    else:
        fm = AuthenticationForm()
    return render(request, 'myapp/djangologin.html', {'forms': fm})
def sign_up(request):
   if request.method == "POST":
      fm = UserCreationForm(request.POST)
      if fm.is_valid():
         fm.save()
   else:     
    fm = UserCreationForm()
   return render(request, 'myapp/signup.html',{'form':fm})       


# def show_data(request):
#     myfm = list(blog.objects.values())  
#     request.session['me'] = myfm 
#     me = request.session.get('me')

#     if request.method == 'POST':
#         fm = blogsign(request.POST)  
#         if fm.is_valid():
#             fm.save()
#         else:
#          fm = blogsign()
#     else:
#         fm = blogsign()

#     return render(request, 'myapp/show_data.html', {'form': me, 'forms': fm})

###########################here i Implement Searching with filter######
# views.py
def show_data(request):
    me = blog.objects.all()
    if request.method == "GET":  
        st = request.GET.get('servicename')  
        if st:
            me = blog.objects.filter(title__icontains=st)
    if request.method == 'POST':
        fm = blogsign(request.POST)
        if fm.is_valid():
            fm.save()
        else:
            fm = blogsign()
    else:
        fm = blogsign()

    return render(request, 'myapp/show_data.html', {'form': me, 'forms': fm})




def Update_data(request, id):
    if request.method=='POST':
     pi=blog.objects.get(pk=id)
     print('dekhe is me kya hn',pi)
     fm=blogsign(request.POST, instance=pi)
     if fm.is_valid():
      fm.save()
    #   request.session.pop('me', None)      
    else:
      pi=blog.objects.get(pk=id)           
      fm=blogsign(instance=pi)
    return render(request, 'myapp/update.html',{'form':fm})

def delete_data(request, id):
    if request.method == 'POST':
        pi = blog.objects.get(pk=id)
        pi.delete()
        # Clear the session data after successful delete
        # request.session.pop('me')
        return HttpResponseRedirect('/')


def setsession(request):

   request.session['name'] = 'Ali'
   return render(request, 'myapp/setsession.html')

def getsession(request):
   if 'name' in request.session:
      name = request.session.get('name')
      print('cheack kr',name)
      return render(request, 'myapp/getsession.html')
   else:
    return HttpResponseRedirect('Your session expire....')
   
def delete_session(request):
    if 'name' in request.session:
       del request.session['name']
       return render(request,'myapp/delete.html')
# from django.shortcuts import get_object_or_404

# def delete_data(request, id):
#     if request.method == 'POST':
#         # Delete the record from the model
#         pi = get_object_or_404(blog, pk=id)
#         pi.delete()

#         # Remove the record from the session if it exists
#         me = request.session.get('me', [])
#         me = [item for item in me if item['id'] != id]  # Assuming 'id' is the key in your myfm data
#         request.session['me'] = me

#     return HttpResponseRedirect('/')

########################################################
# from django.shortcuts import render,HttpResponseRedirect
# from .models import blog
# from .forms import blogsign
# # Create your views here.
# def show_data(ILoveDjango):
#     myfm = blog.Hi_Bro.all()
#     if ILoveDjango.method == 'POST':
#         fm = blogsign(ILoveDjango.POST)

#         if fm.is_valid():
#          fm.save()
   
#         fm = blogsign()    
#     else:
#         fm = blogsign()
#     return render(ILoveDjango, 'myapp/show_data.html', {'form': myfm, 'forms': fm})


# def Update_data(request, id):
#     if request.method=='POST':
#      pi=blog.Hi_Bro.get(pk=id)
#      print('dekhe is me kya hn',pi)
#      fm=blogsign(request.POST, instance=pi)
#      if fm.is_valid():
#       fm.save()
#     else:
#       pi=blog.Hi_Bro.get(pk=id)           
#       fm=blogsign(instance=pi)
#     return render(request, 'myapp/update.html',{'form':fm})

# def delete_data(request, id):
#     if request.method=='POST':
#         pi=blog.Hi_Bro.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')
 ############################################   
# from django.shortcuts import render, HttpResponseRedirect
# from .models import blog
# from .forms import blogsign

# def show_data(request):
#     myfm = blog.Hi_Bro.all()

#     if request.method == 'POST':
#         fm = blogsign(request.POST)
#         if fm.is_valid():
#             fm.save()
#             # Save the form data to the session
#             request.session['form_data'] = fm.cleaned_data
#             return HttpResponseRedirect('/')  # Redirect to avoid form resubmission
#     else:
#         # Retrieve form data from the session
#         form_data = request.session.get('form_data', {})
#         print('here is see data sess',form_data)

#         fm = blogsign(initial=form_data)
#         print('here is see data sess',form_data)


#     return render(request, 'myapp/show_data.html', {'form': myfm, 'forms': fm})

# def Update_data(request, id):
#     if request.method == 'POST':
#         pi = blog.Hi_Bro.get(pk=id)
#         fm = blogsign(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#             # Clear the session data after successful update
#             request.session.pop('form_data', None)
#     else:
#         pi = blog.Hi_Bro.get(pk=id)
#         fm = blogsign(instance=pi)

#     return render(request, 'myapp/update.html', {'form': fm})

# def delete_data(request, id):
#     if request.method == 'POST':
#         pi = blog.Hi_Bro.get(pk=id)
#         pi.delete()
#         # Clear the session data after successful delete
#         request.session.pop('form_data', None)
#         return HttpResponseRedirect('/')

