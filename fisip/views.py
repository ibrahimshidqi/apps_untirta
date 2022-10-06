from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def prodifisip(request):
    judul = "S1 Administrasi Publik", "S1 Ilmu Komunikasi", "S1 Ilmu Pemerintahan",

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'judul': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fisip.html', konteks)

def sejarahfisip(request):
    return render(request, 'sejarahfisip.html')