from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from mvpapp.queries import get_avg_funding_by_person, get_companies_by_person, get_investors_by_company

from typing import Sequence 

def index(request):
  return HttpResponse("Test") 

def average_funding(request, person_id: str): 
  result: int = get_avg_funding_by_person(person_id)
  print('result', result)
  template = loader.get_template('mvpapp/paragraph.html')
  context = {
      'result': result,
  }
  return HttpResponse(template.render(context, request))

def companies(request, person_id: str):
  past_companies: Sequence[str] = get_companies_by_person(person_id) 
  template = loader.get_template('mvpapp/results_list.html')

  return HttpResponse(template.render({"results" : past_companies}, request))

def investors(request, company_name: str):
  company_investors: Sequence[str] = get_investors_by_company(company_name) 
  template = loader.get_template('mvpapp/results_list.html')

  return HttpResponse(template.render({"results" : company_investors}, request))


     
