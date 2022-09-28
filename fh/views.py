from django.shortcuts import render

# Create your views here.
def prodifh(request):
    judul = "S1 Ilmu Hukum",
    konteks = {
        'judul': judul
    }
    return render(request, 'fh.html', konteks)

def sejarahfh(request):
    return render(request, 'sejarahfh.html')