from django.shortcuts import get_object_or_404
from .models import StockModel
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import StockModelForm

# Create your views here.


class StockListView(ListView):
    model = StockModel
    template_name = "stock/stockmodel_list.html"
    context_object_name = "object_list"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        query = self.request.GET.get("type", None)
        stocks = []
        if query is not None:
            stocks = StockModel.objects.filter(category=query)
        else:
            stocks = StockModel.objects.all()

        total_roe = sum(stock.roe for stock in stocks)
        total_eps = sum(stock.eps for stock in stocks)
        total_book_value = sum(stock.book_value for stock in stocks)
        total_price = sum(stock.price for stock in stocks)

        context["avg_roe"] = total_roe/len(stocks) if len(stocks) > 0 else 0
        context["avg_eps"] = total_eps/len(stocks) if len(stocks) > 0 else 0
        context["avg_book_value"] = total_book_value / \
            len(stocks) if len(stocks) > 0 else 0
        context["avg_price"] = total_price / \
            len(stocks) if len(stocks) > 0 else 0

        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get("type", None)

        if query is not None:
            return StockModel.objects.filter(category=query)

        return StockModel.objects.all()


class StockCreateView(CreateView):
    template_name = 'stock/stockmodel_form.html'
    form_class = StockModelForm
    success_url = '/'


class StockUpdateView(UpdateView):
    template_name = 'stock/stockmodel_form.html'
    form_class = StockModelForm
    success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(StockModel, id=id_)


class StockDeleteView(DeleteView):
    model = StockModel
    success_url = '/'
