from django.shortcuts import get_object_or_404
from ProfessionalServices.models import PServices


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    price = 5
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    ProfService_count = 0

    for id, quantity in cart.items():
        ProfService = get_object_or_404(PServices, pk=id)
        total += 5
        ProfService_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'ProfService': ProfService})

    return {
        'cart_items': cart_items,
        'total': total,
        'ProfService_count': ProfService_count}
