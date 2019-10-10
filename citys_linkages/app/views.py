from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from app import models


def index(request):
    return render(request, 'index.html')


def province(request):
    all_province = models.BureauAreas.objects.filter(type='2')
    province_info_list = [(p.pid, p.name) for p in all_province]
    return JsonResponse(province_info_list, safe=False, json_dumps_params={'ensure_ascii': False})


def city(request):
    p_pid = request.GET.get('prpid')
    citys = models.BureauAreas.objects.filter(parent_id=p_pid, type='3')
    c_list = [(c.pid, c.name) for c in citys]
    return JsonResponse(c_list, safe=False, json_dumps_params={'ensure_ascii': False})


def county(request):
    ci_pid = request.GET.get('cipid')
    countys = models.BureauAreas.objects.filter(parent_id=ci_pid, type='4')
    co_list = [(c.pid, c.name) for c in countys]
    return JsonResponse(co_list, safe=False, json_dumps_params={'ensure_ascii': False})


def town(request):
    co_pid = request.GET.get('copid')
    towns = models.BureauAreas.objects.filter(parent_id=co_pid, type='5')
    t_list = [(t.pid, t.name) for t in towns]
    return JsonResponse(t_list, safe=False, json_dumps_params={'ensure_ascii': False})


def village(request):
    t_pid = request.GET.get('tpid')
    villages = models.Village.objects.filter(parent_id=t_pid)
    v_list = [(v.pid, v.name) for v in villages]
    return JsonResponse(v_list, safe=False, json_dumps_params={'ensure_ascii': False})


