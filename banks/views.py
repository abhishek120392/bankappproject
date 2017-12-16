# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Branch, Bank
import json

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def bankdetails(request):
	ifsc_code = request.GET.get('ifsc_code')
	branch = Branch.objects.get(ifsc=ifsc_code)
	try:
		bank = Bank.objects.get(pk=branch.bank_id)
		resp = {
			'branch' : {
				'name' : bank.name,
				'bank_id' : branch.bank_id,
				'branch' : branch.branch,
				'address' : branch.address,
				'city' : branch.city,
				'district' : branch.district,
				'state' : branch.state
			}
		}
	except Exception as e:
		resp = {"status":"error", "message":e.message}

	return HttpResponse(json.dumps(resp, indent=2))

def bankInCity(request):
	bank_name = request.GET.get('name')
	city = request.GET.get('city')
	branches = []
	try:
		bank_branches = Branch.objects.filter(city=city, bank__name=bank_name).all()
		for bank_branch in bank_branches:
			branches.append(bank_branch.serialize())
		resp = {
			'bank_branches' : branches
		}
	except Exception as e:
		resp = {"status":"error", "message":e.message}

	return HttpResponse(json.dumps(resp, indent=2))
