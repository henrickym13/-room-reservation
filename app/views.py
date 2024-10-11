from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from reserve.models import Reserve
from django.db.models import Count
from django.db.models.functions import ExtractMonth


def is_admin(user):
    return user.groups.filter(name='Administradores').exists()


@login_required
def index(request):
    if request.user.is_superuser:
        return redirect('usage_report')
    else:
        return redirect('user_booking_history')


@login_required
@user_passes_test(is_admin)
def usage_report(request):
    total_reserves = Reserve.objects.filter(status='confirmada').count()
    reservations_by_room = Reserve.objects.filter(status='confirmada').values(
        'room__name').annotate(total=Count('id')).order_by('-total')
    most_used_room = reservations_by_room.first() if reservations_by_room else None
    reservations_by_month = Reserve.objects.filter(status='confirmada').annotate(
       month=ExtractMonth('date')).values('month').annotate(total=Count('id')).order_by('month')
    
    return render(request, 'usage_report.html', {
        'total_reserves': total_reserves,
        'reservations_by_room': reservations_by_room,
        'most_used_room': most_used_room,
        'reservations_by_month': reservations_by_month,
    })