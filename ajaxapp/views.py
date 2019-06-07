from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def homepage(request):
	context = {}
	if request.method == 'POST':
		print('===============',request.POST)
		name = request.POST.get('name')
		sername = request.POST.get('sername')

		context['name'] = name
		context['sername'] = sername
		print('--------------------',context)

		context = json.dumps(context)

		return HttpResponse(context)


	return render (request, 'ajaxapp/index.html')