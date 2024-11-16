from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Topic, Case, Resolution

# Create your views here.
# @login_required
# def topics(request):
#     return render(request, 'assistant.html', {'topics': Topic.objects.all()})



# from django.http import JsonResponse
# from django.shortcuts import render
# from .models import Topic, Case, Resolution

# def wizard(request):
#     topics = Topic.objects.all()
#     return render(request, 'assistant.html', {'topics': topics})

# def get_cases(request, topic_id):
#     cases = Case.objects.filter(topic_id=topic_id).values('id', 'name')
#     return JsonResponse(list(cases), safe=False)

# def get_resolution(request, case_id):
#     resolution = Resolution.objects.filter(case_id=case_id).values('resolve').first()
#     return JsonResponse(resolution)


from django.shortcuts import render
from django.http import JsonResponse
from .models import Topic, Case, Resolution

# Initial view to render the template
def knowledge_wizard(request):
    topics = Topic.objects.all()  # Fetch all topics for step 1
    return render(request, 'knowledge_wizard.html', {'topics': topics})

# View to fetch cases related to the selected topic
def get_cases(request):
    topic_id = request.GET.get('topic_id')
    cases = Case.objects.filter(topic_id=topic_id)  # Filter cases by topic
    cases_list = list(cases.values('id', 'name'))  # Convert to list of dicts
    return JsonResponse(cases_list, safe=False)

# View to fetch resolution related to the selected case
def get_resolution(request):
    case_id = request.GET.get('case_id')
    resolution = Resolution.objects.filter(case_id=case_id).first()  # Get the resolution for the selected case
    if resolution:
        return JsonResponse({
            'name': resolution.name,
            'resolve': resolution.resolve,
        })
    else:
        return JsonResponse({'error': 'No resolution found'}, status=404)
