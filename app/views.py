from django.shortcuts import render, redirect
from .models import Items, Goals
from math import ceil

# Create your views here.

def dashboard(request):

	objs = Items.objects.all()
	progress = []

	for obj in objs:

		item = obj.id
		# print(item)
		goals = Goals.objects.filter(item_id = item)
		completed = goals.filter(status = True)

		try:
			percentage = (len(completed)/len(goals))*100
			# print(ceil(percentage))
			progress.append(ceil(percentage))
		except:
			percentage = 0
			progress.append(percentage)

	contents = zip(objs,progress)

	print(len(objs))
	print(len(progress))
	context = {"contents":contents}
	return render(request, 'dashboard-page.html', context)


def addForm(request):

	if request.method == "POST":

		post_title = request.POST['title']
		names = request.POST.getlist('name')

		print(post_title)
		print(names)

		if not post_title or names == ['']:

			return render(request, 'add-form.html')

		else:
			title_obj = Items(title = post_title)
			title_obj.save()

			title_id = Items.objects.get(title = post_title).id
			for name in names:
				name_obj = Goals(name = name, item_id = title_id)
				name_obj.save()

			return redirect('dashboard')
		
	return render(request, 'add-form.html')


def editForm(request, pk):

	title = Items.objects.get(id = pk)
	objs = Goals.objects.filter(item_id = pk)
	context = {"objs":objs, "primary_id":pk, "title":title}


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

def updateForm(request, pk):

	item = Items.objects.get(id = pk)
	goals = Goals.objects.filter(item_id = pk)

	context = {

		"item": item,
		"goals": goals,
	}


	if request.method == "POST":

		goal_items = request.POST.getlist("goal_item")
		new_title = request.POST.get("title")
		print(goal_items)
		print(new_title)

		
		item.title = new_title
		item.save()

		
		goals.delete()

		if not goal_items:
			item.delete()
		else:
			for item_name in goal_items:
				
				update = Goals(name = item_name, item_id = pk)
				update.save()

		return redirect('dashboard')

		

	print("Skipped Post")

	return render(request, 'edit_item-form.html', context)
	


def deleteGoal(request, pk):

	item = Items.objects.get(id = pk)

	print(item)
	item.delete()

	return redirect('dashboard')


