from django.shortcuts import render
def Display(request):
    return render(request,'home.html')
def dis(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print("USERNAME:", username)
        print("PASSWORD:", password)

        message = "Data received!"

    return render(request, "page2.html", {"message": message})
