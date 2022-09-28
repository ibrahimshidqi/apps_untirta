from django.shortcuts import render

# Create your views here.
def prodipascasarjana(request):
    judul = "Pascasarjana", "Doktor Pendidikan", "Magister Ilmu Hukum", "Magister Ilmu Pertanian", "Magister Administrasi Publik", "Magister Akuntansi", "Magister Ilmu Komunikasi", "Magister Manajemen", "Magister Teknik Kimia", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Pendidikan Matematika", "Teknologi Pendidikan"

    konteks = {
        'judul': judul
    }
    return render(request, 'pascasarjana.html', konteks)

def sejarahpascasarjana(request):
    return render(request, 'sejarahpascasarjana.html')