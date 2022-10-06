from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def prodift(request):
    judul = "S1 Teknik Elekro", "S1 Teknik Industri", "S1 Teknik Kimia", "S1 Teknik Mesin", "S1 Teknik Metalurgi", "S1 Teknik Sipil"
    
    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'judul': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'ft.html', konteks)

def sejarahft(request):
    return render(request, 'sejarahft.html')