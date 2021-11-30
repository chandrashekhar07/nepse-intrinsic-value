from django.shortcuts import get_object_or_404
from .models import StockModel
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import StockModelForm

# Create your views here.

class StockListView(ListView):
    model = StockModel
    template_name ="stock/stockmodel_list.html"

    def get_queryset(self):
        request = self.request
        query = request.GET.get("type", None)

        if query is not None:
            return StockModel.objects.filter(category=query)

        return StockModel.objects.all()

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