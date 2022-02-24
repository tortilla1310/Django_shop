from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from mainapp.models import Product, ProductCategory
from django.urls import reverse, reverse_lazy
from adminapp.utils import superuser_required
from django.http.response import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product/edit.html'
    fields = '__all__'

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        return {
            'category': self.get.category()
        }

    def get_success_url(self) -> str:
        return reverse('admin:products', kwargs=self.kwargs)

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = ProductCategory.objects.get(pk=self.kwargs['pk'])
        return context


@ superuser_required
def products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category).order_by('id')

    return render(request, 'adminapp/product/products.html', context={
        'title': 'Продукты',
        'category': category,
        'objects': products
    })


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'

        return context


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
