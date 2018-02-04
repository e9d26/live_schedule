from django.shortcuts import render, get_object_or_404, redirect
from .models import Schedule

# Create your views here.
def schedule_list(request):
    schedules = Schedule.objects.order_by('date')
    return render(request, 'live_schedule/schedule_list.html', {'schedules': schedules})

#def schedule_detail(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    return render(request, 'live_schedule/schedule_detail.html', {'schedule': schedule})
