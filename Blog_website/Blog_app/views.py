from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, "app/home.html")


def about(request):
    return render(request, "app/about.html")


def services(request):
    return render(request, "app/services.html")


def contact(request):
    return render(request, "app/contact.html")


def login(request):
    return render(request, "app/login.html")


def logout(request):
    del request.session["Name"]
    return render(request, "app/home.html")


def logindata(request):
    if request.method == "POST":
        login_email = request.POST['login-email']
        login_password = request.POST['login-password']

        Email = request.session['Email']
        Password = request.session['Password']

        # print(login_email,Email,Password,login_password)

        if "Email" in request.session:
            if (login_email == Email and login_password == Password):
                Name = request.session['Name']
                Phone = request.session['Phone']
                request.session.modified = True
                data = {
                    "Name": Name,
                    "Email": Email,
                    "Phone": Phone,
                    "Password": Password,
                }
                return render(request, "app/home.html", {"dt": data})
            else:
                return render(request, "app/login.html")
        else:
            return render(request,"app/login.html")
    else:
        return render(request,"app/home.html")

def signup(request):
    return render(request, "app/signup.html")


def signupdata(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']

    request.session['Name'] = name
    request.session['Email'] = email
    request.session['Phone'] = phone
    request.session['Password'] = password

    return render(request, "app/login.html")
