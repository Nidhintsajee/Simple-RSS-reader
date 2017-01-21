from django.shortcuts import render
import feedparser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@csrf_exempt
def reader_page(request):
	entered_url = request.POST.get('url')
	data_feed = feedparser.parse(entered_url)
        entries = data_feed.entries
        data_list = []
        for data in entries:
                data_dict = {
                'title':data.title,
                'description' : data.description,
                'link' : data.link
                }
                data_list.append(data_dict)
        return HttpResponse(json.dumps(data_list))

def entry_page(request):
	return render(request, 'entry_page.html')
