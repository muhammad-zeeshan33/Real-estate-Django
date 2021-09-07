from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, UserContact
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        get=request.POST
        listing=get['listing']
        listing_id=get['listing_id']
        agent_email=get['agent_email']
        name=get['name']
        email=get['email']
        phone=get['phone']
        message=get['message']

        contact =Contact(listing_id=listing_id, listing=listing, name=name, email=email, phone=phone, message=message)
        contact.save()  

        #send mail
        send_mail(
            'Property Listing Inquiry',
            'You have got a message from '+ name + ', for ' + listing + '. Sign in to your admin panel to get further details about the client! or contact  +'+ phone + '\n Clients Message: ' + message + '\n Checkout in Admin Panel.',
            'estateagency48@gmail.com',
            [agent_email, 'muhammadzeeshan33300@gmail.com', 'Usmanchughtai2018@gmail.com'],
            fail_silently=False
        )
        messages.success(request, ' Your message is delivered to the Agent, he will get back to you soon!')
        return redirect('/listings/'+listing_id)
    
def contactus(request):
    if request.method == 'POST':
        get=request.POST                        
        name=get['name']
        email=get['email']
        subject=get['subject']
        message=get['message']
        contact =UserContact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, ' Thank you for contacting us!')
        return redirect('contact')
    return render(request , 'pages/contact.html')