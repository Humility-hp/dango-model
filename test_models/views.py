from django.shortcuts import render
from .forms import NameForm
from django.core.mail import send_mail

# Create your views here.
def get_name(request):
 form = NameForm()
 subject = form["subject"]
 context = {"subject":subject.render("name.html")}
#  if request.method == "POST":
#   form = NameForm(request.POST)
#   if form.is_valid():
#    sender=form.cleaned_data['sender']
#    message = form.cleaned_data['message']
#    subject = form.cleaned_data['subject']
#    recipients=["hos97.ph@gmail.com"]
#    print(sender, message, subject,recipients)
#  else:
#   form = NameForm()
 return render(request, "name.html", context)

data ={
 "subject":"hello",
 "message":"Hi there",
 "sender":"foo@example.com",
 "cc_myself":True,
}

