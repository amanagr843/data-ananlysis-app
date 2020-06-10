from django.shortcuts import render
import pandas as pd
from .get_data import data
# Create your views here.

def main(request):
    # districts = data["District Name"].unique()
    sates = sorted(data["State Name"].unique())
    # sub_districts = data["Sub District Name"].unique()
    inputSubDistrict = str(request.POST.get('inputsubdis'))
    State_Name = data.loc[data["Sub District Name"].str.contains(pat = inputSubDistrict, regex=False),"State Name"]
    District_Name = data.loc[data["Sub District Name"].str.contains(pat = inputSubDistrict, regex=False),"District Name"]
    Sub_District_Name = data.loc[data["Sub District Name"].str.contains(pat = inputSubDistrict, regex=False),"Sub District Name"]
    Village_Name = data.loc[data["Sub District Name"].str.contains(pat = inputSubDistrict, regex=False),"Village Name"]
    Village_Population = data.loc[data["Sub District Name"].str.contains(pat = inputSubDistrict, regex=False),"Total Population of Village"]
    Male = data.loc[data["Sub District Name"].str.contains(pat = inputSubDistrict, regex=False),"Total Male Population of Village"]
    Female = data.loc[data["Sub District Name"].str.contains(pat = inputSubDistrict, regex=False),"Total Female Population of Village"]
    q = request.POST.get('quantity')
    r = District_Name.size
    # print(District_Name.size)
    if q == '10':
        r = 10
    elif q == '20':
        r = 20

    mylist = zip(State_Name,District_Name,Sub_District_Name,Village_Name,Village_Population,Male,Female)
    return render(request,"main.html",{"states":sates,"mylist":mylist,"r":r})


def district_choices_ajax(request):
    state = request.GET.get('dis')
    distr = sorted(data.loc[data["State Name"].str.contains(pat = state),"District Name"].astype("str").unique())
    return render(request,"_choice_ajax.html",{"distr":distr})

def sub_district_choices_ajax(request):
    dist = request.GET.get('sub')
    subdist = sorted(data.loc[data["District Name"].str.contains(pat = dist),"Sub District Name"].astype("str").unique())
    return render(request,"_sub_choices_ajax.html",{"subdist":subdist})
