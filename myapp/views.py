# Views 

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Individu

class IndividuListView(ListView):
    model = Individu
    template_name = "myapp/individu_list.html"
    context_object_name = "daftar_individu"

class IndividuDetailView(DetailView):
    model = Individu
    template_name = "myapp/individu_detail.html"

class IndividuCreateView(CreateView):
    model = Individu
    fields = ['nama_depan', 'nama_belakang', 'gender', 'email', 'kota', 'tahun_engagement', 'consent_publish']
    template_name = "myapp/individu_form.html"
    success_url = reverse_lazy('individu_list')

class IndividuUpdateView(UpdateView):
    model = Individu
    fields = ['nama_depan', 'nama_belakang', 'gender', 'email', 'kota', 'tahun_engagement', 'consent_publish']
    template_name = "myapp/individu_form.html"
    success_url = reverse_lazy('individu_list')

class IndividuDeleteView(DeleteView):
    model = Individu
    template_name = "myapp/individu_confirm_delete.html"
    success_url = reverse_lazy('individu_list')
