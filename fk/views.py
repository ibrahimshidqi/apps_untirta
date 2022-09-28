from django.shortcuts import render

# Create your views here.
def prodifk(request):
    judul = "S1 Kedokteran", "S1 Keperawatan", "D3 Keperawatan", "S1 Gizi", "S1 Ilmu Keolahragaan",
    konteks = {
        'judul': judul
    }
    return render(request, 'fk.html', konteks)

def sejarahfk(request):
    return render(request, 'sejarahfk.html')