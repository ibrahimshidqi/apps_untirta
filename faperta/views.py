from django.shortcuts import render

# Create your views here.
def prodifaperta(request):
    judul = "S1 Agribisnis", "S1 Agrokoteknologi", "S1 Ilmu Perikanan", "S1 Teknologi Pangan"

    konteks = {
        'judul': judul
    }
    return render(request, 'faperta.html', konteks)

def sejarahfaperta(request):
    return render (request, 'sejarahfaperta.html')