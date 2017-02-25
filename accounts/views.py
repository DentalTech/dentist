from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm, FamilyForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
import stripe
import arrow
from .models import Family


stripe.api_key = settings.STRIPE_SECRET


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                family_number = form.cleaned_data['number_family']

                customer = stripe.Customer.create(
                    email=form.cleaned_data['email'],
                    card=form.cleaned_data['stripe_id'],  # this is currently the card token/id
                    plan='DENTIST_MONTHLY_' + str(family_number),
                )

                if customer:
                    user = form.save()
                    user.stripe_id = customer.id
                    user.subscription_end = arrow.now().replace(weeks=+4).datetime
                    user.save()

                    for x in range(family_number):

                        family_member = Family()
                        get_full_name = 'family_' + str(x+1)
                        family_member.full_name = form.cleaned_data[get_full_name]
                        family_member.account_name_id = user.id
                        family_member.save()

                user = auth.authenticate(email=request.POST.get('email'),
                                         password=request.POST.get('password1'))

                if user:
                    auth.login(request, user)
                    messages.success(request, "You have successfully registered")
                    return redirect(reverse('success'))
                else:
                    messages.error(request, "unable to log you in at this time!")

            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")

        else:
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        today = datetime.date.today()
        form = UserRegistrationForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))

    return render(request, 'membership.html', args)


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='/login/')
def success(request):
    return render(request, 'success.html')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))

@login_required(login_url='/accounts/login/')
def cancel_subscription(request):
   try:
       customer = stripe.Customer.retrieve(request.user.stripe_id)
       customer.cancel_subscription(at_period_end=True)
   except Exception, e:
       messages.error(request, e)
   return redirect('profile')


def family_member_details(request):

    user = request.user

    if user.is_authenticated:
        if request.method == 'POST':
            form = FamilyForm(request.POST, instance=user)
            if form.is_valid():

                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']

                family_member = Family()
                family_member.first_name = first_name
                family_member.last_name = last_name
                family_member.account_name_id = user.id
                family_member.save()

                return redirect(reverse('families'))

        else:
            form = FamilyForm()

        args = {}
        args.update(csrf(request))

        args['form']=form

        return render(request, 'family_members.html', args)


def all_families(request):
    families = Family.objects.all()
    return render(request, "families.html", {"families": families})



