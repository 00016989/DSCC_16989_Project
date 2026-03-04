from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from .forms import ProductForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .models import Product, Feedback, Category
from django.core.exceptions import PermissionDenied


def home(request):
    products = Product.objects.all().order_by('-id')[:3]

    return render(request, 'main/home.html', {
        'products': products,
    })


class ProductListView(ListView):
    model = Product
    template_name = 'main/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.GET.get('category')

        if category_id:
            queryset = queryset.filter(category__id=category_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'


class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('products')

    def test_func(self):
        return self.request.user.is_staff


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('products')

    def test_func(self):
        return self.request.user.is_staff


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'main/product_confirm_delete.html'
    success_url = reverse_lazy('products')

    def test_func(self):
        return self.request.user.is_staff


class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    fields = ['message']
    template_name = 'main/feedback_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.kwargs['pk']})


class FeedbackListView(ListView):
    model = Feedback
    template_name = 'main/feedback_list.html'
    context_object_name = 'feedbacks'
    ordering = ['-created_at']


class FeedbackUpdateView(LoginRequiredMixin, UpdateView):
    model = Feedback
    fields = ['message']
    template_name = 'main/feedback_form.html'
    success_url = reverse_lazy('feedback_list')

    def dispatch(self, request, *args, **kwargs):
        feedback = self.get_object()
        if feedback.user != request.user and not request.user.is_staff:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class FeedbackDeleteView(LoginRequiredMixin, DeleteView):
    model = Feedback
    template_name = 'main/feedback_confirm_delete.html'
    success_url = reverse_lazy('feedback_list')

    def dispatch(self, request, *args, **kwargs):
        feedback = self.get_object()
        if feedback.user != request.user and not request.user.is_staff:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'main/register.html', {'form': form})
