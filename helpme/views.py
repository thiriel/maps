from django.utils import simplejson
from django.core import serializers
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect, HttpResponse
from helpme.forms import CreatePoint


def helpme(request):
    return direct_to_template(request, 'maps.html')

def alert(request):
    if request.method == 'POST':
        form = CreatePoint(request.POST)
        if form.is_valid():
            point = form.save(commit=False)
            point.save()
            data = serializers.serialize('json', [point,])
            return HttpResponse(simplejson.dumps(data), mimetype="application/json")
