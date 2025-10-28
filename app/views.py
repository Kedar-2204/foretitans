from django.shortcuts import render
from datetime import date
from admin_dashboard.models import *
from django.shortcuts import render
from django.utils.timezone import now

# Create your views here.
def index(request):
    today = now().date()

    current = list(Tournament.objects.filter(start_date__lte=today, end_date__gte=today)[:3])
    upcoming = list(Tournament.objects.filter(start_date__gt=today)[:2])
    past = list(Tournament.objects.filter(end_date__lt=today).order_by("-end_date")[:2])

    slider_images = SliderImage.objects.all()
    team = TeamMember.objects.all()
    sponsors = Sponsor.objects.all()
    news_list = CricketNews.objects.all().order_by('-id')
    contact_info = Contact.objects.last()

    total_needed = 7
    tournaments_selected = current + upcoming + past

    if len(tournaments_selected) < total_needed:
        # Get extra tournaments excluding already chosen
        extra = Tournament.objects.exclude(id__in=[t.id for t in tournaments_selected])[: (total_needed - len(tournaments_selected))]
        tournaments_selected += list(extra)

    context = {
        "current_tournaments": current,
        "upcoming_tournaments": upcoming,
        "past_tournaments": past,
        "slider_images": slider_images,
        "team": team,
        "sponsors": sponsors,
        'news_list': news_list,
        'contact_info': contact_info
    }
    return render(request, "index.html", context)

def about(request):
    team = TeamMember.objects.all()
    contact_info = Contact.objects.last()
    return render(request, "about.html",{"team": team,"contact_info":contact_info})

def our_work(request):
    # Fetch associations (organisers)
    associations = Organiser.objects.all()

    # Fetch partners (sponsors)
    partners = Sponsor.objects.all()

    contact_info = Contact.objects.last()

    # You can decide which one is "Principal Partner"
    principal_partner = partners.first() if partners.exists() else None

    return render(request, "our_work.html", {
        "associations": associations,
        "partners": partners,
        "principal_partner": principal_partner,
        'contact_info': contact_info
    })

def contact(request):
    contact_info = Contact.objects.last()
    return render(request, "contact.html", {"contact_info": contact_info})

def gallary(request):
    gallery_images = GalleryImage.objects.all().order_by("-uploaded_at")
    contact_info = Contact.objects.last()

    context = {
        "gallery_images": gallery_images,
        "contact_info":contact_info
    }
    return render(request, "gallary.html", context)

def news(request):
    news_list = CricketNews.objects.all().order_by('-id')
    ads = Advertisement.objects.all().order_by('-uploaded_at')
    contact_info = Contact.objects.last()
    context = {

        'news_list': news_list,
        'ads': ads,
        'contact_info': contact_info,
    }
    return render(request, "news.html",context)

def blog(request):
    contact_info = Contact.objects.last()
    return render(request, "blog.html", {"contact_info": contact_info})

def tournaments(request):
    today = now().date()
    current_tournaments = Tournament.objects.filter(start_date__lte=today, end_date__gte=today)
    upcoming_tournaments = Tournament.objects.filter(start_date__gt=today)
    past_tournaments = Tournament.objects.filter(end_date__lt=today)
    contact_info = Contact.objects.last()

    return render(request, "tournaments.html", {
        "current_tournaments": current_tournaments,
        "upcoming_tournaments": upcoming_tournaments,
        "past_tournaments": past_tournaments,
        "contact_info": contact_info
    })

def current_tournaments(request):
    today = date.today()
    tournaments = Tournament.objects.filter(start_date__lte=today, end_date__gte=today)
    contact_info = Contact.objects.last()
    return render(request, "current_tournaments.html", {"tournaments": tournaments,"contact_info": contact_info})


def upcoming_tournaments(request):
    today = date.today()
    tournaments = Tournament.objects.filter(start_date__gt=today)
    contact_info = Contact.objects.last()
    return render(request, "upcoming_tournaments.html", {"tournaments": tournaments,"contact_info": contact_info})


def past_tournaments(request):
    today = date.today()
    tournaments = Tournament.objects.filter(end_date__lt=today)
    contact_info = Contact.objects.last()
    return render(request, "past_tournaments.html", {"tournaments": tournaments,"contact_info": contact_info})


