from django.shortcuts import render 
from main.models import Myproject
# Create your views here.
def home(request):
	return render(request, 'main/home.html')

def footer(request):
	return render(request, 'main/footer.html')


def project1(request):
	results = Myproject.objects.all()
	content = {'results':results}
	return render(request,'main/project1.html',content)


def searchMatch(query ,item):
	if query in item.Pname.lower() or query in item.Ptag.lower():
		return True
	else:
		return False

"""def search(request):
	query = request.GET.get('search')
	results = []
	#print(searchProject)

	data = Myproject.objects.all()
	ProjList  = [item for item in data if searchMatch(query ,item)]

	results.append(ProjList)
	content = {'results':results}
	print(content)
	return render(request, 'main/project1.html',content)

"""

def search(request):
	query = request.GET.get('search')
	results = Myproject.objects.filter(Pname__icontains=query)
	print(results)
	params = {'results':results}
	return render(request, 'main/search.html',params)