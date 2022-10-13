from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(redirect_field_name='login')
def index(request):
    return render(request,'sobre/dash.html')