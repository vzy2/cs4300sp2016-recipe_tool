from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader
from .form import QueryForm
from .test import find_recipes, find_recipes2
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def final(request):
    output_list = ''
    output=''
    ingredients = ''
    srName = ''
    similar_recipes = ''
    rush=False
    reqIng = ''

    if request.GET.get('ingredients'):        
        ingredients = request.GET.get('ingredients')
    if request.GET.get('rush'):
        rush = True
    if request.GET.get('srName'):
        srName = request.GET.get('srName')
    if request.GET.get('reqIng'):
        reqIng = request.GET.get('reqIng')
    if ingredients or srName:
        output_list = find_recipes2(ingredients, reqIng, rush, srName)
        if len(output_list) == 0:
            output = "None"
        else:
            paginator = Paginator(output_list, 10)
            page = request.GET.get('page')
            try:
                output = paginator.page(page)
            except PageNotAnInteger:
                output = paginator.page(1)
            except EmptyPage:
                output = paginator.page(paginator.num_pages)
    return render_to_response('project_template/final.html', 
                          {'output': output,
                           'magic_url': request.get_full_path(),
                           })

def index(request):
    output_list = ''
    output=''
    ingredients = ''
    similar_recipes = ''

    if request.GET.get('ingredients'):        
        ingredients = request.GET.get('ingredients')
        print ingredients
    if request.GET.get('similar_recipe'):
        similar_recipes = request.GET.get('similar_recipe')
    if ingredients or similar_recipes:
        #find_recipes should be implemented in test.py 
        # make use of inverted index 
        output_list = find_recipes(ingredients,similar_recipes)
        if len(output_list) == 0:
            output = "None"
        else:
            paginator = Paginator(output_list, 10)
            page = request.GET.get('page')
            try:
                output = paginator.page(page)
            except PageNotAnInteger:
                output = paginator.page(1)
            except EmptyPage:
                output = paginator.page(paginator.num_pages)
    return render_to_response('project_template/index.html', 
                          {'output': output,
                           'magic_url': request.get_full_path(),
                           })
