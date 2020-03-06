from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from ProfessionalServices.models import PServices
import stripe

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """View to handle customer payment and purchase Professional Service"""
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            cart = request.session.get('cart', {})
            for id, quantity in cart.items():
                ProfService = get_object_or_404(PServices, pk=id)
                total = 0
                total += quantity * ProfService.udPrice
                order = order_form.save(commit=False)
                for x in range(0,quantity):
                    print(x)
                    order.pk = None
                    order.date = timezone.now()
                    order.remainingHours = ProfService.totalHours
                    order.ProfService = ProfService
                    order.user = request.user
                    order.save()

            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(
                    request,
                    "Your card was declined.",
                    extra_tags="alert-danger")

            if customer.paid:
                messages.success(
                    request,
                    "You have successfully paid",
                    extra_tags="alert-success")
                purchase_list = []
                for id, quantity in cart.items():
                    purchase_list.append(id)
                for id in purchase_list:
                    ProfService = get_object_or_404(PServices, pk=id)
                    ProfService.purchases += 1
                    ProfService.save()
                request.session['cart'] = {}
                return redirect(reverse('profile'))
            else:
                messages.error(
                    request,
                    "Unable to take payment",
                    extra_tags="alert-danger")
        else:
            messages.error(
                request,
                "We were unable to take a payment.",
                extra_tags="alert-primary")
            print (messages.error)
    else:
        if request.user.is_authenticated:
            order_form = OrderForm(initial={'email': request.user.email, 'full_name': request.user.get_full_name})
            payment_form = MakePaymentForm()
        else:
            payment_form = MakePaymentForm()
            order_form = OrderForm()

    return render(request,
                  "checkout.html",
                  {"order_form": order_form,
                   "payment_form": payment_form,
                   "publishable": settings.STRIPE_PUBLISHABLE})