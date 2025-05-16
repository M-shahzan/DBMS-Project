from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import restables, Reservation
from .forms import reserveForm,tableForm
from django.db import connection,models
from django.utils import timezone

@login_required
def reserveView(request):
    available = restables.objects.filter(status = 'available')  # Fetch all tables
    form = reserveForm()  # Empty form for GET requests

    if request.method == "POST":
        form = reserveForm(request.POST)
        table_id = request.POST.get("table_id")  # Get table_id from form input

        if form.is_valid():
                # Fetch the selected table
            table = restables.objects.get(table_id=table_id)

            # Save reservation
            reservation = form.save(commit=False)
            reservation.user = request.user  # Assign logged-in user
            reservation.table = table  # Link to selected table
            reservation.save()

            # Update table status to "reserved"
            table.status = "reserved"
            table.save()

            return redirect('feedback')  # Redirect after successful reservation

    return render(request, 'reservations.html', {'available': available, 'form': form})

@login_required
def tablesView(request):
    tables = restables.objects.all().order_by('table_num')
    form = tableForm()

    if request.method == 'POST':
        action = request.POST.get('action')
        table_id = request.POST.get('table_id')

        if action == 'add':
            form = tableForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('tables')

        elif action == 'edit':
            table = restables.objects.get(pk=table_id)
            form = tableForm(request.POST, instance=table)
            if form.is_valid():
                form.save()
                return redirect('tables')

        elif action == 'delete':
            table = restables.objects.get(pk=table_id)
            table.delete()
            return redirect('tables')

    return render(request, 'tables.html', {'tables': tables, 'form': form})

@login_required
def reservationsView(request):
    # Get all reservations ordered by date (newest first)
    reservations = Reservation.objects.all().order_by('-date')
    
    # Get counts for statistics
    total_count = reservations.count()
    today_count = Reservation.objects.filter(date__date=timezone.now().date()).count()
    
    # Get status counts using aggregation
    tables_by_status = restables.objects.values('status').annotate(count=models.Count('status'))
    status_counts = {item['status']: item['count'] for item in tables_by_status}
    
    # Prepare context
    context = {
        'reservations': reservations,
        'total_count': total_count,
        'today_count': today_count,
        'available_count': status_counts.get('available', 0),
        'reserved_count': status_counts.get('reserved', 0),
        'out_of_service_count': status_counts.get('outofservice', 0),
    }
    
    return render(request, 'reservationsView.html', context)