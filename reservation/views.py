from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import restables, Reservation
from .forms import reserveForm,tableForm

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

            return redirect('reserve')  # Redirect after successful reservation

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
                return redirect('table_view')

        elif action == 'edit':
            table = restables.objects.get(pk=table_id)
            form = tableForm(request.POST, instance=table)
            if form.is_valid():
                form.save()
                return redirect('table_view')

        elif action == 'delete':
            table = restables.objects.get(pk=table_id)
            table.delete()
            return redirect('table_view')

    return render(request, 'tables.html', {'tables': tables, 'form': form})
