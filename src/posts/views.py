from django.db.models import Count,Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post
#from .models import Post
def websiteofzensa(request):
    coksatanlar= Post.objects.filter(coksatanlar=True)
    enyeniler= Post.objects.filter(enyeniler=True)
    ahsap= Post.objects.filter(ahsap=True)
    boyalar= Post.objects.filter(boyalar=True)


    #coksatanlar= Post.objects.filter(thumbnail=True)
    #enyeniler= Post.objects.filter(thumbnaily=True) 
    #ahsap= Post.objects.filter(thumbnaila=True)  
    
    #latest= Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list':coksatanlar,
        'object_list2':enyeniler,
        'object_list3':ahsap,
        'object_list_boya':boyalar
     #   'object_list2':coksatanlar,
      #  'object_list3':enyeniler,
       # 'object_list4':ahsap
        #'latest':latest
    }
    return render(request, 'websiteofzensa.html', context)

def search(request):
    queryset= Post.objects.all()
    query= request.GET.get('q')
    if query:   
        queryset=queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct() 

    context ={
   
        'queryset': queryset
        
    }
    return render(request, 'search_results.html', context)    

def products(request):
    #post_list= Post.objects.all() #blog html inde de bunu kullanacağız o yüzden modelsdeki postun tüm objectlerini post list olarak tanımladık burada
    post_list= Post.objects.filter(akıl_oyunları=True)
    paginator = Paginator(post_list, 4)

    page_request_var= 'page'#buraya verilen numarayı alıp page e eşitliyoruz
    page= request.GET.get(page_request_var)


    try:#eğer herhangi bir sıkıntı yoksa girilen numarayı açacak
        paginated_queryset = paginator.page(page)

    except PageNotAnInteger: #eğer girilen numara integer değilse hata vermek yerine ilk sayfayı döndürecek
        paginated_queryset=paginator.page(1)

    except EmptyPage:
        paginated_queryset=Paginator.page(paginator.num_pages)#sayfa sayısı kadar num_pages in manası.yani en son sayfayı döndürecek    

    context ={
   
        'queryset': paginated_queryset,
        'page_request_var':page_request_var
    }
    return render(request, 'products.html', context)

def ahsap(request):
    #post_list= Post.objects.all() #blog html inde de bunu kullanacağız o yüzden modelsdeki postun tüm objectlerini post list olarak tanımladık burada

    ahsap_list= Post.objects.filter(ahsap_obje=True)
    paginator= Paginator(ahsap_list, 4)



    page_request_var= 'page'#buraya verilen numarayı alıp page e eşitliyoruz
    
    page= request.GET.get(page_request_var)
    

    try:#eğer herhangi bir sıkıntı yoksa girilen numarayı açacak
      
        paginated_queryset = paginator.page(page)
       
    except PageNotAnInteger: #eğer girilen numara integer değilse hata vermek yerine ilk sayfayı döndürecek
        
        paginated_queryset = paginator.page(1)
        
    except EmptyPage:
       
        paginated_queryset= Paginator.page(paginator.num_pages)
       

    context ={
        
        'ahsap_objeler': paginated_queryset,
        
        'page_request_var':page_request_var
    }
    return render(request, 'ahsap.html', context)

def boyalar(request):
    #post_list= Post.objects.all() #blog html inde de bunu kullanacağız o yüzden modelsdeki postun tüm objectlerini post list olarak tanımladık burada

    boya_list= Post.objects.filter(boya=True)
    paginator= Paginator(boya_list, 20)



    page_request_var= 'page'#buraya verilen numarayı alıp page e eşitliyoruz
    
    page= request.GET.get(page_request_var)
    

    try:#eğer herhangi bir sıkıntı yoksa girilen numarayı açacak
      
        paginated_queryset = paginator.page(page)
       
    except PageNotAnInteger: #eğer girilen numara integer değilse hata vermek yerine ilk sayfayı döndürecek
        
        paginated_queryset = paginator.page(1)
        
    except EmptyPage:
       
        paginated_queryset= Paginator.page(paginator.num_pages)
       

    context ={
        
        'boya_objeler': paginated_queryset,
        
        'page_request_var':page_request_var
    }
    return render(request, 'boyalar.html', context)

def post(request, id):
    post = get_object_or_404(Post, id=id) #bu bir object id si idye eşit olan objeyi alıp post a eşitliyor eğer bulamazsa 404 döndürüyor
    #deneme
    
    #denembitti
    context = {
        'post':post
        
        #deneme
        
    }
    return render(request, 'post.html', context)    

#şimdi yapacağım değişiklikler ahşap ürünler ve en yeni ürünler sliderları için farklı resimler koymak olacak
# şuanki durumda Post classında bulunan objeleri alıyor ama benim istediğim belli bir kısmı seçmesi
# aklıma bir fikir geldi featured gibi birşey aypmayı deneyeceğim bekle    