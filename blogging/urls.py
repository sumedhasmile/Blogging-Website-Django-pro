"""blogging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Blog.views import *
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('home/', HomePage, name='Home'),
                  path('second/', SecondPage),
                  path('index/', HtmlPage),
                  path('students/', AllStudent, name='alls'),
                  path('single/', getData),
                  path('details/<int:sid>/', StudentDetail, name='sdetails'),
                  path('addition/<int:num1>/<int:num2>/', Add, name='add'),
                  path('form/', HtmlForm, name='form'),
                  path('add_category/', AddCategory, name='add_cat'),
                  path('all_category/', Adminpanel, name='all_cat'),
                  path('add_blog_old/', AddBlog, name='add_blog'),
                  path('loginid/', Login, name='login'),
                  path('home/', home, name='home'),
                  path('userpanel/', userpanel, name='userpanel'),
                  path('signupid/', Signup, name='signupid'),
                  path('cat_detailold/<int:cid>/', Category_detail, name='cat_detailold'),

                  path('edit_blog1/<int:bid>/', Edit_blog, name='edit_blog_old'),
                  path('delete_blog/<int:bid>/', deleteData, name='delete'),
                  #######New Blog #######
                  path('', newhome, name='home'),
                  path('single_post/<int:bid>/', newsingle_post, name='single'),
                  path('about_us/', newabout_us, name='about'),
                  path('blog/<int:bid>/', BlogDetails, name='blog'),
                  path('blog_comment/<int:bid>/', addcomment, name='comment'),
                  path('blog_like/<int:bid>/', LikeBlog, name='like'),
                  path('signup/', NewSignup, name='signup'),
                  path('logout/', Logout, name='logout'),
                  path('login/', NewLogin, name='newlogin'),
                  path('add_blog/', NewAddBlog, name='addblog'),
                  path('cat_detail/<int:cid>/', NewCategory_detail, name='cat_detail'),
                  path('allblogs/', NewAllblogs, name='allblog'),
                  path('edit_blog/<int:bid>/', NewEdit_blog, name='edit_blog'),
                  path('delete_blog/<int:bid>/', Delete_blog, name="delete_blog")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
