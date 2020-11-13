from django.shortcuts import render
from .models import Faxmachine

# Create your views here.
def faxmachine_list(request):
    machines = Faxmachine.objects.order_by('faxowner')
    return render(request, 'fpb/faxmachine_list.html', {'machines': machines})