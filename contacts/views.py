from django.shortcuts import render, redirect
from contacts.models import contact
from .forms import contactForm
from django.utils import timezone



#method to render the welcome page
def welcomeView(request):
	return render (request,'contacts/index.html')

#method to render the list page
def listView(request):
		
		#get all contacts available in the database
    allContacts = contact.objects.all()

    pageContent = {'allContacts': allContacts}
    return render(request, 'contacts/listView.html',pageContent)

#method to render the add page
def addView(request):
	#create an instance of the contact form
	form = contactForm()
	message = ''
	
	#if session contains message, get message  
	if 'message' in request.session:
		message = request.session['message']
		del  request.session['message']
	
	pageContent = {'form': form, 'message': message}
	
	return render(request, 'contacts/addView.html', pageContent)		

#method to recieve user input and store contact
def addANewContact(request):
	try:
			# if this is a POST request we need to process the form data
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = contactForm(request.POST)
			
			# check validity of the form:
			if form.is_valid():
				
				# process the data in form.cleaned_data and save to database
				newEntry = contact(name = form.cleaned_data.get('Name'), emailAddress = form.cleaned_data.get('Email'), date_logged=timezone.now())
				newEntry.save()
				
				#set success message
				request.session['message'] = 'contact saved'
			
			else:
				#set error message
				request.session['message'] = 'Please fill the form correctly'
		return redirect('add')
	
	except:
		#set error message and redirect to add page
		request.session['message'] = 'Encountered an error, please try again.'
		return redirect('add')
