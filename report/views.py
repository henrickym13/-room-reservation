from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from reserve.models import Reserve
from django.db.models import Count
from django.db.models.functions import ExtractMonth, ExtractHour
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse
from room.models import Room
from django.contrib.auth.models import User


# Create your views here.
def is_admin(user):
    return user.groups.filter(name='Administradores').exists()


def filter_reservations(request):
    reservations = Reserve.objects.filter(status='confirmada')

    room_id = request.GET.get('room')
    if room_id:
        reservations = reservations.filter(room_id=room_id)

    user_id = request.GET.get('user')
    if user_id:
        reservations = reservations.filter(user_id=user_id)

    date_reserve = request.GET.get('date')
    if date_reserve:
        reservations = reservations.filter(date=date_reserve)

    return reservations


@login_required
@user_passes_test(is_admin)
def usage_report(request):
    total_reserves = Reserve.objects.filter(status='confirmada').count()
    reservations_by_room = Reserve.objects.filter(status='confirmada').values(
        'room__name').annotate(total=Count('id')).order_by('-total')
    most_used_room = reservations_by_room.first() if reservations_by_room else None
    reservations_by_month = Reserve.objects.filter(status='confirmada').annotate(
       month=ExtractMonth('date')).values('month').annotate(total=Count('id')).order_by('month')
    peak_times = Reserve.objects.filter(status='confirmada').annotate(
        hour=ExtractHour('start_time')).values('hour').annotate(total=Count('id')).order_by('-total')

    reservations = filter_reservations(request)

    rooms = Room.objects.all()
    users = User.objects.all()

    context = {
        'total_reserves': total_reserves,
        'reservations_by_room': reservations_by_room,
        'most_used_room': most_used_room,
        'reservations_by_month': reservations_by_month,
        'peak_times': peak_times,
        'rooms': rooms,
        'users': users,
        'reservations': reservations,
    }
    
    return render(request, 'usage_report.html', context)


def setup_pdf_metadata(canvas, doc):
    doc.title = "Relatório de Reservas"
    canvas.setTitle("Relatório de Reservas")


def render_pdf_view(request):
    reservations_by_room = Reserve.objects.filter(status='confirmada').values('room__name').annotate(
        total=Count('id')).order_by('-total')
    reservations_by_month = Reserve.objects.filter(status='confirmada').annotate(
        month=ExtractMonth('date')).values('month').annotate(total=Count('id')).order_by('month')
    peak_times = Reserve.objects.filter(status='confirmada').annotate(
        hour=ExtractHour('start_time')).values('hour').annotate(total=Count('id')).order_by('-total')

    rooms = [reservation['room__name'] for reservation in reservations_by_room]
    room_totals = [reservation['total'] for reservation in reservations_by_room]
    months = [reservation['month'] for reservation in reservations_by_month]
    month_totals = [reservation['total'] for reservation in reservations_by_month]
    hours = [reservation['hour'] for reservation in peak_times]
    hour_totals = [reservation['total'] for reservation in peak_times]

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_graficos.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Relatório de Reservas", styles['Title']))

    elements.append(Paragraph("Salas mais Utilizadas", styles['Heading2']))
    drawing_rooms = Drawing(400, 220)
    bc_rooms = VerticalBarChart()
    bc_rooms.x = 50
    bc_rooms.y = 50
    bc_rooms.height = 125
    bc_rooms.width = 300
    bc_rooms.data = [room_totals]  
    bc_rooms.categoryAxis.categoryNames = rooms
    bc_rooms.bars[0].fillColor = colors.blue
    bc_rooms.valueAxis.valueMin = 0
    drawing_rooms.add(bc_rooms)
    elements.append(drawing_rooms)
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Frequência de Reservas por Mês", styles['Heading2']))
    drawing_month = Drawing(400, 220)
    bc_month = VerticalBarChart()
    bc_month.x = 50
    bc_month.y = 50
    bc_month.height = 125
    bc_month.width = 300
    bc_month.data = [month_totals] 
    bc_month.categoryAxis.categoryNames = [f'Mês {month}' for month in months] 
    bc_month.bars[0].fillColor = colors.orange
    drawing_month.add(bc_month)
    elements.append(drawing_month)
    elements.append(Spacer(1, 72))
    
    elements.append(Paragraph("Horário de Pico das Reservas", styles['Heading2']))
    drawing_hourly = Drawing(400, 240)
    pie = Pie()
    pie.x = 150
    pie.y = 50
    pie.width = 150
    pie.height = 150
    pie.data = hour_totals 
    pie.labels = [f'{hour}:00' for hour in hours]
    pie.slices[0].fillColor = colors.red
    pie.slices[1].fillColor = colors.blue
    pie.slices[2].fillColor = colors.green
    pie.slices[3].fillColor = colors.purple
    drawing_hourly.add(pie)
    elements.append(drawing_hourly)

    doc.build(elements, onFirstPage=setup_pdf_metadata)

    return response