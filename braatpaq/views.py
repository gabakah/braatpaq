from django.shortcuts import render_to_response

def home_page(request):
    return render_to_response('default.html', )

def features_page(request):
    return render_to_response('features.html',)

def accessories_page(request):
    return render_to_response('accessories.html',)