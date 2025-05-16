from django.shortcuts import render,redirect
from django.db import connection
from .models import Feedback

# Create your views here.
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