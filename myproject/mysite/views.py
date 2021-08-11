from django.shortcuts import render
import requests


def get_departments(request):
    if request.method == "GET":
        departments_json = requests.get("http://127.0.0.1:9000/department")
        departments_text = departments_json.json()
        context = {
            'data': departments_text,
        }
        return render(request, 'myproject/index.html', context)
