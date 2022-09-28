from django.shortcuts import render

# Create your views here.
def prodifkip(request):
    judul = "S1 Pendidikan Nonformal", "S1 Pendidikan Bahasa Indonesia", "S1 Pendidikan Bahasan Inggris", "S1 Pendidikan Biologi", "S1 Pendidikan Matematika", "S1 Pendidikan Guru Sekolah Dasar", "S1 Pendidikan Guru PAUD", "S1 Bimbingan dan Konseling", "S1 Pendidikan Fisika", "S1 Pendidikan Ilmu Pengetahuan Alam", "S1 Pendidikan Kimia", "S1 Pendidikan Khusus", "S1 Pendidikan Pancasila dan Kewarganegaraan", "S1 Pendidikan Sejarah", "S1 Pendidikan Sosiologi", "S1 Pendidikan Vokasi Teknik Elektro", "S1 Pendidikan Vokasi Teknik Mesin",
    konteks = {
        'judul' : judul
    }
    return render(request, 'fkip.html', konteks)

def sejarahfkip(request):
    return render(request, 'sejarahfkip.html')