from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.user.is_superuser:
        return redirect('usage_report')
    else:
        return redirect('user_booking_history')
