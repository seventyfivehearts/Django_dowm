from django.shortcuts import render, HttpResponse

# Create your views here.


def ab_ajax(request):
    if request.method == 'POST':
        print(request.POST)
        i1 = request.POST.get('id1')
        i2 = request.POST.get('id2')
        i3 = int(i1) + int(i2)
        print(i3)
        return HttpResponse(i3)
    return render(request, 'index.html')