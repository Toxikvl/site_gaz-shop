from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from oscar.apps.checkout import views
from oscar.apps.payment import forms, models

class PaymentDetailsView(views.PaymentDetailsView):

    def get_context_data(self, **kwargs):
        # Override method so the billing address forms can be
        # added to the context.
        ctx = super(PaymentDetailsView, self).get_context_data(**kwargs)
        ctx['billing_address_form'] = kwargs.get(
            'billing_address_form', forms.BillingAddressForm())
        return ctx

    def post(self, request, *args, **kwargs):
        # Override so we can validate the bankcard/billingaddress submission.
        # If it is valid, we render the preview screen with the forms hidden
        # within it.  When the preview is submitted, we pick up the 'action'
        # parameters and actually place the order.
        if request.POST.get('action', '') == 'place_order':
            return self.do_place_order(request)
        billing_address_form = forms.BillingAddressForm(request.POST)
        if not all([billing_address_form.is_valid()]):
            # Form validation failed, render page again with errors
            self.preview = False
            ctx = self.get_context_data(billing_address_form=billing_address_form)
            return self.render_to_response(ctx)
        # Render preview with bankcard and billing address details hidden
        return self.render_preview(request, billing_address_form=billing_address_form)

    def do_place_order(self, request):
        billing_address_form = forms.BillingAddressForm(request.POST)
        if not all([billing_address_form.is_valid()]):
            messages.error(request, "Invalid submission")
            return HttpResponseRedirect(reverse('checkout:payment-details'))
        submission = self.build_submission()
        submission['payment_kwargs']['billing_address'] = billing_address_form.cleaned_data
        return self.submit(**submission)