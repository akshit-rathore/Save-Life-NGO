from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import donation
import razorpay
from . import my_new_id


# Create your views here.
client = razorpay.Client(auth=('rzp_test_2fX9F9LavNHdYu','ZULfEfH7N2X1KdVM6bxiDxGR'))

@login_required(login_url='login')
def Donation(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        amount = request.POST['amount']
        donate = donation(name=name, email=email, username=username, amount=amount)
        donate.save()
        my_new_id.id = donate.id
        return redirect('bill')

    return render(request, 'webpages/pay.html')


@login_required(login_url='login')
def bill(request):
    # if request.method == 'POST':
    billdata = get_object_or_404(donation, pk=my_new_id.id)
    
    DATA = {
        "amount": billdata.amount*100,
        "currency": "INR",
        "payment_capture": 1,
    }
    payment_order = client.order.create(data=DATA)
    payment_order_id = payment_order['id']
    donation_data = {
            'billdata': billdata,
            'key':'rzp_test_2fX9F9LavNHdYu',
            'order_id': payment_order_id,
        }
    return render(request, 'webpages/bill.html', donation_data)


@login_required(login_url='login')
def success(request):
    billdata = get_object_or_404(donation, pk=my_new_id.id)
    billdata.order_status = 1
    billdata.save()
    messages.success(request, "Thanks for donation!")
    return render(request, 'webpages/success.html')

@login_required(login_url='login')
def fail(request):
    billdata = get_object_or_404(donation, pk=my_new_id.id)
    billdata.delete()
    messages.warning(request, "Some Error Occured!")
    return render(request, 'webpages/fail.html')