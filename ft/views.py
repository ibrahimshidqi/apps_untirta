from django.shortcuts import render

# Create your views here.
def prodift(request):
    judul = "S1 Teknik Elekro", "S1 Teknik Industri", "S1 Teknik Kimia", "S1 Teknik Mesin", "S1 Teknik Metalurgi", "S1 Teknik Sipil"
    
    konteks = {
        'judul': judul
    }
    return render(request, 'ft.html', konteks)

def sejarahft(request):
    return render(request, 'sejarahft.html')