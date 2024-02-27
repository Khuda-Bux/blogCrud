
from django.urls import path
from myapp import views
urlpatterns = [
    path('show/',views.show_data,name='show'),
    path('<int:id>/',views.Update_data,name='update'),
    path('delete/<int:id>',views.delete_data,name='delete'),
    path('set/',views.setsession,name='set'),
    path('get/',views.getsession,name='get'),
    path('del/',views.delete_session,name='del'),
    path('login/',views.login,name='login'),
    path('djangologin/',views.DjnagLogin,name='djangologin'),
    path('sign/',views.sign_up,name='sign'),
    path('home/',views.home,name='home'),






]