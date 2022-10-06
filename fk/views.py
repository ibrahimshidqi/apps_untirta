from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def prodifk(request):
    judul = "S1 Kedokteran", "S1 Keperawatan", "D3 Keperawatan", "S1 Gizi", "S1 Ilmu Keolahragaan",

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'judul': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fk.html', konteks)

def sejarahfk(request):
    return render(request, 'sejarahfk.html')