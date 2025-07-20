from django.shortcuts import render, get_object_or_404
from .models import Product,Category
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Order
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def product_detail(request, pk):
    ob_product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': ob_product})

def product_list(request):
    category_id = request.GET.get('category')
    query = request.GET.get('q')
    products = Product.objects.all()
    if category_id:
        products = products.filter(category_id=category_id)
    if query:
        products = products.filter(name__icontains=query)
    categories = Category.objects.all()
    return render(request, 'product_list.html', {'products': products, 'categories': categories})
    

def add_to_cart(request, pk):
    cart = request.session.get('cart', [])
    if pk not in cart:
        cart.append(pk)
    request.session['cart'] = cart
    return redirect('product_list')

def view_cart(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(pk__in=cart)
    return render(request, 'cart.html', {'products': products})

@login_required
def place_order(request):
    cart = request.session.get('cart', [])
    if cart:
        order = Order.objects.create(user=request.user)
        order.products.set(cart)
        order.save()
        request.session['cart'] = []  # clear cart
        return redirect('order_history')
    return redirect('product_list')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html', {'orders': orders})
