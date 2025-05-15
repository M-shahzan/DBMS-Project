from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import restables, Reservation,Feedback
from .forms import reserveForm,tableForm
from django.db import connection

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
def feedbackView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        visit_date = request.POST.get('visit_date')
        comments = request.POST.get('comments')

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO feedback (name, email, rating, visit_date, comments)
                VALUES (%s, %s, %s, %s, %s)
            """, [name, email, rating, visit_date, comments])

        return redirect('home')

    return render(request, 'feedback.html')


def feedbackListView(request):
    feedbacks = Feedback.objects.all().order_by('-submission_date')
    total_feedback = feedbacks.count()
    ratings = feedbacks.values_list('rating', flat=True)
    average_rating = sum(ratings) / len(ratings) if ratings else 0

    context = {
        'feedbacks': feedbacks,
        'total_feedback': total_feedback,
        'average_rating': average_rating,
    }
    return render(request, 'feedback_list.html', context)

