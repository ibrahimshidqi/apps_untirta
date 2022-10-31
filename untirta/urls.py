"""untirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from faperta.views import prodifaperta
from faperta.views import *
from feb.views import prodifeb
from feb.views import sejarahfeb
from fh.views import prodifh
from fh.views import sejarahfh
from fisip.views import prodifisip
from fisip.views import sejarahfisip
from fk.views import prodifk
from fk.views import sejarahfk
from fkip.views import prodifkip
from fkip.views import *
from ft.views import prodift
from ft.views import sejarahft
from pascasarjana.views import prodipascasarjana
from pascasarjana.views import sejarahpascasarjana
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faperta/', prodifaperta),
    path('sejarahfaperta/', sejarahfaperta),
    path('feb/', prodifeb),
    path('sejarahfeb/', sejarahfeb),
    path('fh/', prodifh),
    path('sejarahfh/', sejarahfh),
    path('fisip/', prodifisip),
    path('sejarahfisip/', sejarahfisip),
    path('fk/', prodifk),
    path('sejarahfk/', sejarahfk),
    path('fkip/', prodifkip),
    path('sejarahfkip/', sejarahfkip),
    path('ft/', prodift),
    path('sejarahft/', sejarahft),
    path('pascasarjana/', prodipascasarjana),
    path('sejarahpascasarjana/', sejarahpascasarjana),
    path('', views.index),
    path('tambah-dosen/', tambah_dosen, name='tambah_dosen'),
    path('dosen/ubah/<int:id_dosen>', ubah_dosen, name='ubah_dosen'),
    path('dosen/hapus/<int:id_dosen>', hapus_dosen, name='hapus_dosen'),
    path('tambah-staff//', tambah_staff, name='tambah_staff'),
    path('staff/ubah/<int:id_staff>', ubah_staff, name='ubah_staff'),
    path('tambah-mahasiswa/', tambah_mahasiswa, name='tambah_mahasiswa'),
    path('mahasiswa/ubah/<int:id_mahasiswa>', ubah_mahasiswa, name='ubah_mahasiswa'),
    
]
