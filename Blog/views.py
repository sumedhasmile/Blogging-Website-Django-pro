from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def HomePage(request):
    name = "SUMEDHA"
    return HttpResponse("<h1>WELCOME " + name + "</h1>")


def SecondPage(request):
    return HttpResponse("<h1>WELCOME TO HOME PAGE</h1>")


def HtmlPage(request):
    slist = ["sumedha", "sohan", "sidd", "sharada"]
    d = {"data": slist}
    return render(request, 'index.html', d)


def AllStudent(request):
    data = Student.objects.all()
    d = {"studentdata": data}
    return render(request, 'students.html', d)


def getData(request):
    data = Student.objects.get(id=2)
    filterdata = Student.objects.filter(branch="CS")
    d = {"student": data, "filterdata": filterdata}
    return render(request, 'single.html', d)


def Add(request, num1, num2):
    output = num1 + num2
    return HttpResponse("<h1>OUTPUT: " + str(output) + "</h1>")


def StudentDetail(request, sid):
    data = Student.objects.get(id=sid)
    d = {"student": data}
    return render(request, 'details.html', d)


def HtmlForm(request):
    output = None
    if request.method == "POST":
        d = request.POST
        print(d['num1'])
        print(d['num2'])
        a = int(d['num1'])
        b = int(d['num2'])
        output = a + b
    dic = {"opt": output}
    return render(request, 'hform.html', dic)


def Allblogs(request):
    blogs = BlogModel.objects.all()
    d = {'blogs': blogs}
    return render(request, 'allblog.html', d)


from datetime import date

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def Login(request):
    if request.method == "POST":
        dic = request.POST
        u = dic['user']
        p = dic['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            if request.user.is_staff:
                return redirect('all_cat')
            return redirect('home')
        else:
            messages.error(request, 'User not found')
            return redirect('login')
    return render(request, 'login.html')


def home(request):
    allcat = Category.objects.all()
    d = {'allcat': allcat}
    return render(request, 'home.html', d)


def Adminpanel(request):
    cat = Category.objects.all()
    d = {'allcat': cat}
    return render(request, 'all_cat.html', d)


def AddCategory(request):
    if request.method == "POST":
        dic = request.POST
        c = dic['cname']
        Category.objects.create(name=c)
        return redirect('all_cat')

    return render(request, 'add_cat.html')


def Category_detail(request, cid):
    catdata = Category.objects.get(id=cid)
    blogs = BlogModel.objects.filter(cat=catdata)
    d = {'blogs': blogs}
    return render(request, 'cat_details.html', d)


def userpanel(request):
    if not request.user.is_authenticated:
        return redirect('login')
    userblog = BlogModel.objects.filter(usr=request.user)
    userdata = UserDetail.objects.filter(usr=request.user).first()
    d = {'userblog': userblog,
         'userdata': userdata}
    return render(request, 'userpanel.html', d)


def AddBlog(request):
    if not request.user.is_authenticated:
        return redirect('login')
    allcat = Category.objects.all()
    d = {'allcat': allcat}
    if request.method == "POST":
        dic = request.POST
        catid = dic['cat']
        catdata = Category.objects.get(id=catid)
        title = dic['title']
        short = dic['short']
        long = dic['long']
        img = request.FILES['img']
        today_date = date.today()
        userdata = request.user
        print(dic)
        BlogModel.objects.create(
            usr=userdata,
            cat=catdata,
            title=title,
            desc=short,
            long_desc=long,
            date=today_date,
            image=img)

    return render(request, 'addblog.html', d)


def Logout(request):
    logout(request)
    return redirect('home')


def Signup(request):
    error = False
    if request.method == "POST":
        d = request.POST
        fullname = d['user'].split()
        first = fullname[0]
        last = fullname[1]
        mobile = d['mobile']
        email = d['email']
        username = d['username']
        pwd = d['pwd']
        image = request.FILES['img']
        user = User.objects.filter(username=username)
        if user:
            error = True
        else:
            userdata = User.objects.create_user(username=username, password=pwd, email=email
                                                , first_name=first, last_name=last)
            UserDetail.objects.create(usr=userdata, image=image, mobile=mobile)
            return redirect('login')
    dic = {"error": error}
    return render(request, 'signup.html', dic)


def Edit_blog(request, bid):
    blogdata = BlogModel.objects.get(id=bid)
    allcat = Category.objects.all()
    if request.method == "POST" and not request.user.is_staff:
        dic = request.POST
        catid = dic['cat']
        t = dic['title']
        short = dic['short']
        long = dic['long']

        try:
            img = request.FILES['img']
            blogdata.image = img
            blogdata.save()
        except:
            pass
        catdata = Category.objects.get(id=catid)
        blogdata.title = t
        blogdata.desc = short
        blogdata.long_desc = long
        blogdata.cat = catdata
        blogdata.save()
    d = {'blogdata': blogdata, 'allcat': allcat}
    return render(request, 'EditBlog.html', d)


def deleteData(request, bid):
    blogdata = BlogModel.objects.get(id=bid)
    blogdata.delete()

    return redirect('userpanel')


######New Blog ######
def newhome(request):
    allblog = BlogModel.objects.all()

    categorys = Category.objects.all()
    blog = allblog[::-1]
    print(blog)
    last_five_blog = blog[:5]
    print(last_five_blog)
    d = {'allblog': allblog, 'last_five_blog': last_five_blog, 'category': categorys}
    return render(request, 'newtemp/index.html', d)


def newsingle_post(request, bid):
    allblog = BlogModel.objects.all()
    blog = allblog[::-1]

    last_five_blog = blog[:7]
    d = {'allblog': allblog, 'last_five_blog': last_five_blog}
    return render(request, 'newtemp/single-post.html', d)


def newabout_us(request):
    return render(request, 'newtemp/about-us.html')


def BlogDetails(request, bid):
    data = BlogModel.objects.get(id=bid)
    categorys = Category.objects.all()
    allblog = BlogModel.objects.all()
    blog = allblog[::-1]
    last_five_blog = blog[:5]
    d = {'details': data, 'category': categorys, 'last_five_blog': last_five_blog, 'allblog': allblog}
    return render(request, 'newtemp/single-post.html', d)


def addcomment(request, bid):
    if not request.user.is_authenticated:
        return redirect('login')
    blogdata = BlogModel.objects.get(id=bid)
    usr = request.user
    td = date.today()
    msg = request.POST['message']
    UserComments.objects.create(usr=usr, blog=blogdata, date=td, msg=msg)
    return redirect('blog', bid)


def NewLogin(request):
    if request.method == "POST":
        dic = request.POST
        u = dic['user']
        p = dic['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            if request.user.is_staff:
                return redirect('home')
            return redirect('home')
        else:
            messages.error(request, 'User not found')
            return redirect('newlogin')
    return render(request, 'newtemp/login.html')


def NewSignup(request):
    error = False
    if request.method == "POST":
        d = request.POST
        fullname = d['user'].split()
        first = fullname[0]
        last = fullname[1]
        mobile = d['mobile']
        email = d['email']
        username = d['username']
        pwd = d['pwd']
        image = request.FILES['img']
        user = User.objects.filter(username=username)
        if user:
            error = True
        else:
            userdata = User.objects.create_user(username=username, password=pwd, email=email
                                                , first_name=first, last_name=last)
            UserDetail.objects.create(usr=userdata, image=image, mobile=mobile)
            return redirect('newlogin')
    dic = {"error": error}
    return render(request, 'newtemp/signup.html', dic)


def LikeBlog(request, bid):
    blogdata = BlogModel.objects.get(id=bid)
    user = request.user
    data = Like.objects.filter(blog=blogdata, usr=user)
    if not data:
        Like.objects.create(blog=blogdata, usr=user)
    else:
        data.delete()
    return redirect('blog', bid)


def NewAddBlog(request):
    if not request.user.is_authenticated:
        return redirect('newlogin')
    allcat = Category.objects.all()
    d = {'allcat': allcat}
    if request.method == "POST":
        dic = request.POST
        catid = dic['cat']
        catdata = Category.objects.get(id=catid)
        title = dic['title']
        short = dic['short']
        long = dic['long']
        img = request.FILES['img']
        today_date = date.today()
        userdata = request.user
        BlogModel.objects.create(usr=userdata, cat=catdata, title=title, desc=short, long_desc=long, date=today_date,
                                 image=img)
        return redirect('home')

    return render(request, 'newtemp/addblog.html', d)


def NewCategory_detail(request, cid):
    catdata = Category.objects.get(id=cid)
    blogs = BlogModel.objects.filter(cat=catdata)
    d = {'blogs': blogs}
    return render(request, 'newtemp/categoryDetails.html', d)


def NewAllblogs(request):
    allblogs = BlogModel.objects.all()
    # latest_blog = allblogs[::-1]
    latest_blog = BlogModel.objects.last()
    d = {'allblogs': allblogs, 'latest_blog': latest_blog}
    return render(request, 'newtemp/allblogs.html', d)


def NewEdit_blog(request, bid):
    blogdata = BlogModel.objects.get(id=bid)
    allcat = Category.objects.all()
    if request.method == "POST" and not request.user.is_staff:
        dic = request.POST
        catid = dic['cat']
        t = dic['title']
        short = dic['short']
        long = dic['long']

        try:
            img = request.FILES['img']
            blogdata.image = img
            blogdata.save()
        except:
            pass
        catdata = Category.objects.get(id=catid)
        blogdata.title = t
        blogdata.desc = short
        blogdata.long_desc = long
        blogdata.cat = catdata
        blogdata.save()

    d = {'blogdata': blogdata, 'allcat': allcat}
    return render(request, 'newtemp/edit_blog.html', d)


def Delete_blog(request, bid):
    details = BlogModel.objects.get(id=bid)
    details.delete()
    return redirect('home')
