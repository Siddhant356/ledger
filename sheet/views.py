from django.shortcuts import render, redirect
from .models import Ledger
from .forms import LedgerForm
from django.contrib.auth.models import User

def ledger_view(request):
    if request.method =='POST':
        form = LedgerForm(request.POST)

        if form.is_valid():
            ledger = form.save(commit=False)
            ledger.save()

            form = LedgerForm()
            return redirect('sheet:ledger_sheet')

    else:
        form = LedgerForm()
    
    ledgers = Ledger.objects.all()
    users = User.objects.all()
    return render(request,'sheet/ledger.html',{'form': form, 'ledgers': ledgers, 'users':users})