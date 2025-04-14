from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import restables, Reservation
from .forms import reserveForm

@login_required
def reserveView(request):
    available = restables.objects.all()  # Fetch all tables
    form = reserveForm()  # Empty form for GET requests

    if request.method == "POST":
        form = reserveForm(request.POST)
        table_id = request.POST.get("table_id")  # Get table_id from form input

        if form.is_valid():
            try:
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

            except restables.DoesNotExist:
                print(f"Error: Table with ID {table_id} does not exist")
        else:
            print("Form errors:", form.errors)

    return render(request, 'reservations.html', {'available': available, 'form': form})
