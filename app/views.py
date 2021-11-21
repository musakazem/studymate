from django.shortcuts import render, redirect
from .models import Items, Goals
from math import ceil

# Create your views here.

def dashboard(request):

	objs = Items.objects.all()
	progress = []

	for obj in objs:

		item = obj.id
		print(item)
		goals = Goals.objects.filter(item_id = item)
		completed = goals.filter(status = True)

		percentage = (len(completed)/len(goals))*100
		print(ceil(percentage))
		progress.append(ceil(percentage))

	contents = zip(objs,progress)

	context = {"contents":contents}
	return render(request, 'dashboard-page.html', context)


def addForm(request):

	if request.method == "POST":

		post_title = request.POST['title']
		names = request.POST.getlist('name')

		print(post_title)
		print(names)

		title_obj = Items(title = post_title)
		title_obj.save()

		title_id = Items.objects.get(title = post_title).id
		for name in names:
			name_obj = Goals(name = name, item_id = title_id)
			name_obj.save()

		return render(request, 'add-form.html')
		
	return render(request, 'add-form.html')


def editForm(request, pk):

	objs = Goals.objects.filter(item_id = pk)
	context = {"objs":objs, "primary_id":pk}

	if request.method == "POST":
		boxes = request.POST.getlist('box')
		print(boxes)
		print(objs)
		
		for obj in objs:
			if str(obj.id) in boxes:
				obj.status = True
				obj.save()
			else:
				obj.status = False
				obj.save()
					
				
		return redirect('dashboard')



	return render(request, 'edit-form.html',context)


