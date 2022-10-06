from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def prodifaperta(request):
    judul = "S1 Agribisnis", "S1 Agrokoteknologi", "S1 Ilmu Perikanan", "S1 Teknologi Pangan"

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'judul': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'faperta.html', konteks)

def sejarahfaperta(request):
    return render (request, 'sejarahfaperta.html')
