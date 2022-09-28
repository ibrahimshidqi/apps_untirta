from django.shortcuts import render

# Create your views here.
def prodifisip(request):
    judul = "S1 Administrasi Publik", "S1 Ilmu Komunikasi", "S1 Ilmu Pemerintahan",
    konteks = {
        'judul': judul
    }
    return render(request, 'fisip.html', konteks)

def sejarahfisip(request):
    return render(request, 'sejarahfisip.html')