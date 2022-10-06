from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff

# Create your views here.
def prodipascasarjana(request):
    judul = "Pascasarjana", "Doktor Pendidikan", "Magister Ilmu Hukum", "Magister Ilmu Pertanian", "Magister Administrasi Publik", "Magister Akuntansi", "Magister Ilmu Komunikasi", "Magister Manajemen", "Magister Teknik Kimia", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Pendidikan Matematika", "Teknologi Pendidikan"

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'judul': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'pascasarjana.html', konteks)

def sejarahpascasarjana(request):
    return render(request, 'sejarahpascasarjana.html')