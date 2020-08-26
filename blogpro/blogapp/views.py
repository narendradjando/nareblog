from django.shortcuts import render,get_object_or_404
from blogapp.models import Post,Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag

# Create your views here.
def postview(request,tagslug=None):
    t=False
    postlist=Post.objects.all()
    if tagslug:
        t=True
        tag=get_object_or_404(Tag,slug=tagslug)
        postlist=postlist.filter(tags__in= [tag])
    paginator = Paginator(postlist, 2)
    pagenumber= request.GET.get('page')
    try:
        postlist= paginator.page(pagenumber)
    except PageNotAnInteger:
        postlist= paginator.page(1)
    except EmptyPage:
        postlist= paginator.page(paginator.num_pages)
    return render(request,'test/postlist.html',{'postlist':postlist,'t':t})
from blogapp.forms import commentform
def postdetails(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    comments=post.comments.filter(active=True)
    csubtmit=False
    if request.method=='POST':
        form=commentform(request.POST)
        if form.is_valid():
            newcomment=form.save(commit=False)
            newcomment.post=post
            newcomment.save()
            csubtmit=True
    else :
        form=commentform()
    return render(request,'test/postdetails.html',{'post':post,'form':form,'csubtmit':csubtmit,'comments':comments})

from blogapp.forms import Emailshare
from django.core.mail import send_mail

def Emailshareview(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=Emailshare(request.POST)
        print('form object created')
        if form.is_valid():
            cd=form.cleaned_data
            print('cd obj created')
            send_mail('subjet','message','nare@blog.com',[cd['to']],fail_silently=False,)
            print('mail sent SUCCESSFULLY')
            sent=True
    else:
        form=Emailshare()
    return render(request,'test/emailshare.html',{'form':form,'post':post,'sent':sent})
