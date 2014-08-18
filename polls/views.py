# from django.shortcuts import render
from django.http import HttpResponse
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from polls.models import Poll

# In Django, web pages and other content are delivered by views. Each view is
# represented by a a Pythin function or method. Django will choose a view by
# examining the URL that's requested.
# Create your views here.

# Django's TEMPLATE_LOADERS setting contains
# django.template.loaders.app_directories.Loader which looks for a "templates"
# subdirectory in each of the INSTALLED_APS. This is how Django knows to look
# for poll templates even though we don't modify TEMPLATE_DIRS in settings.py

# here is the python version
# def index(request):
#     latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
#     output = ', '.join([p.question for p in latest_poll_list])
#     return HttpResponse(output)


def index(request):
    '''
    load the template called polls/index.html and passes it as a context
    The context is a dictionary mapping template variable names to python
    objects.
    'latest_poll_list' becomes the variable that you use in the template!
    e.g., {% if latest_poll_list %}
    - The render() function takes the request object as its first argument, a
    template name as its second argument, and a dictionary as its optional
    third argument. It returns an HttpResponse object of the given template
    with the given context.
    '''
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)
    # long form version
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_poll_list': latest_poll_list,
    # })
    # return HttpResponse(template.render(context))


def detail(request, poll_id):
    '''
    This view raises the Http404 exception if a poll with the requested ID
    doesn't exist.
    long form: from django.http import Http404
    Short form: get_object_or_404()
    get_object_or_404() is a shortcut for get and raise Http404
    '''
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})
    # try:
    #     poll = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404
    # return render(request, 'polls/detail.html', {'poll': poll})


def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
