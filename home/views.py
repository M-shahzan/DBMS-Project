from django.shortcuts import render,HttpResponse
from .models import restables
from menu.models import Menu
from reservation.models import Feedback
from datetime import timedelta
from django.utils import timezone
from django.db import models
# Create your views here.

def index(request):
    count = restables.objects.count()
    available = restables.objects.filter(status = 'available').count()
    reserved = restables.objects.filter(status = 'reserved').count()
    item_count = Menu.objects.count()
    feedbacks = Feedback.objects.all()
    total_reviews = feedbacks.count()
    avg_rating = feedbacks.aggregate(models.Avg('rating'))['rating__avg'] or 0

    # Count new reviews from the last 7 days (example)
    one_week_ago = timezone.now() - timedelta(days=7)
    new_reviews = feedbacks.filter(submission_date__gte=one_week_ago).count()

    details = {
        'menu_count': item_count,
        'count': count,
        'available': available,
        'reserved': reserved,
        'total_reviews': total_reviews,
        'avg_rating': round(avg_rating, 1),
        'new_reviews': new_reviews,
    }

    if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
        return render(request, 'home_manage.html', {'details': details})
    
    return render(request, 'home.html', {'details': details})