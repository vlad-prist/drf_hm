import requests
import stripe
from rest_framework import status

from config import settings
from forex_python.converter import CurrencyRates


stripe.api_key = settings.STRIPE_API_KEY


# def convert_rub_to_usd(amount):
#     ''' Конвертирует рубли в доллары '''
#     c = CurrencyRates()
#     rate = c.get_rate('RUB', 'USD')
#     return int(amount * rate)


def create_stripe_product(obj):
    """Создаем stripe продукт"""
    title_product = f'{obj.course_paid}' if obj.course_paid else f'{obj.lesson_paid}'
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get('id')


def create_stripe_price(amount):
    ''' Создает цену в Stripe '''
    return stripe.Price.create(
        currency="rub",
        unit_amount=int(amount)*100,
        product_data={"name": "Payment"},
    )


def create_stripe_session(price):
    ''' Создает сессию и оплатув Stripe '''
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    # response = requests.get(
    #     f'{settings.STRIPE_API}/v1/checkout/sessions/:{session.get('id')}'
    # )
    # print(response.json())
    return session.get('id'), session.get('url')
