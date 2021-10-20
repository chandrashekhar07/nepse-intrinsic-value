from django.shortcuts import get_object_or_404
from .models import StockModel
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import StockModelForm

# Create your views here.

class StockListView(ListView):
    model = StockModel
    template_name ="stock/stockmodel_list.html"

class StockCreateView(CreateView):
    template_name='stock/stockmodel_form.html'
    form_class = StockModelForm
    success_url ='/'



class StockUpdateView(UpdateView):
    template_name='stock/stockmodel_form.html'
    form_class = StockModelForm
    success_url ='/'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(StockModel,id=id_)


class StockDeleteView(DeleteView):
    model = StockModel
    success_url = '/'