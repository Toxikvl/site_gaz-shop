from decimal import Decimal as D
from django.utils.translation import ugettext_lazy as _
from oscar.apps.shipping import methods


class SelfPickup(methods.Free):
    code = 'self-pickup'
    name = _('Самовывоз')


class Courier(methods.FixedPrice):
    code = 'courier'
    name = _('Доставка')

    charge_excl_tax = D('350.00')
    charge_incl_tax = D('350.00')