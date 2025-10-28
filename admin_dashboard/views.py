from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


# Create your views here.
def dashboard(request):
    return render(request, "dashboard.html", {'navbar' : 'home'})


def add_advertise(request):
    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]
        Advertisement.objects.create(image=image)  # saves to DB + media folder
        messages.success(request,"Advertise has been successfully added.")
        return redirect("add_advertise")  # refresh page after upload
    return render(request, "add_advertise.html")


def organisors(request):
    if request.method == 'POST':
        name = request.POST['organiser_name']
        role = request.POST['organiser_role']
        info = request.POST['organiser_info']
        photo = request.FILES['organiser_photo']
        Organiser.objects.create(name=name, role=role, info=info, photo=photo)
        messages.success(request, f"{name} has been successfully added as an organiser.")
        return redirect('organisors')
    return render(request, 'organisors.html')

def add_mentors(request):
    if request.method == 'POST':
        name = request.POST['mentor_name']
        info = request.POST['mentor_info']
        photo = request.FILES['mentor_photo']
        Mentor.objects.create(name=name, info=info, photo=photo)
        messages.success(request, f"{name} has been successfully added as an mentor.")
        return redirect('add_mentors')
    return render(request, 'add_mentors.html')

def add_sponsors(request):
    if request.method == 'POST':
        if 'sponsor_submit' in request.POST:
            image = request.FILES['sponsor_image']
            url = request.POST.get('sponsor_url', '')
            info = request.POST.get('sponsor_info', '')
            Sponsor.objects.create(image=image, url=url, info=info)
            messages.success(request, "Sponsor has been successfully added.")

        elif 'team_submit' in request.POST:
            owner_name = request.POST.get('owner_name')
            team_name = request.POST.get('team_name')
            team_photo = request.FILES['team_photo']
            TeamEntry.objects.create(owner_name=owner_name, team_name=team_name, photo=team_photo)
            messages.success(request, "Team entry has been successfully added.")

        return redirect('add_sponsors')

    return render(request, 'add_sponsors.html')


from django.shortcuts import render, redirect
from .models import Tournament

def add_tournaments(request):
    if request.method == "POST":
        name = request.POST.get("name")
        logo = request.FILES.get("logo")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        venue = request.POST.get("venue")
        num_teams = request.POST.get("num_teams")
        num_matches = request.POST.get("num_matches")

        Tournament.objects.create(
            name=name,
            logo=logo,
            start_date=start_date,
            end_date=end_date,
            venue=venue,
            num_teams=num_teams,
            num_matches=num_matches
        )
        messages.success(request, "Tournament has been successfully added.")
        return redirect("add_tournaments")  # replace with your tournament list page
    
    return render(request, "add_tournaments.html")


def add_team(request):
    if request.method == "POST":
        team_name = request.POST.get("team_name")
        owner_name = request.POST.get("owner_name")
        tournaments_ids = request.POST.getlist("tournaments")  # multiple checkboxes

        team = TeamEntry.objects.create(
            team_name=team_name,
            owner_name=owner_name
        )

        if tournaments_ids:
            team.tournaments.set(tournaments_ids)  # link selected tournaments

        messages.success(request, "Team has been successfully added.")
        return redirect("add_tournaments")

    return redirect("add_tournaments")


# -------------------
# Add Player
# -------------------
def add_player(request):
    if request.method == "POST":
        player_name = request.POST.get("player_name")
        contact = request.POST.get("contact")
        dob = request.POST.get("dob")
        playing_role = request.POST.get("playing_role")
        city = request.POST.get("city")
        state = request.POST.get("state")
        team_id = request.POST.get("team")
        tournaments_ids = request.POST.getlist("tournaments")

        team = TeamEntry.objects.get(id=team_id)

        player = Player.objects.create(
            player_name=player_name,
            contact=contact,
            dob=dob,
            playing_role=playing_role,
            city=city,
            state=state,
            team=team
        )

        if tournaments_ids:
            player.tournaments.set(tournaments_ids)

        messages.success(request, "Player has been successfully added.")
        return redirect("add_tournaments")

    return redirect("add_tournaments")


def contacts(request):
    if request.method == "POST":
        email = request.POST.get("email")
        contact_number = request.POST.get("contact_number")
        address = request.POST.get("address")

        # Save to DB
        Contact.objects.create(
            email=email,
            contact_number=contact_number,
            address=address
        )
        return redirect("contacts")  # Redirect to same page or success page

    return render(request, "contacts.html")



def cricket_news(request):
    if request.method == 'POST':
        heading = request.POST['news_heading']
        subheading = request.POST.get('news_subheading', '')
        content = request.POST['news_content']
        link = request.POST.get('news_link', '')
        image = request.FILES.get('news_image')
        video = request.FILES.get('news_video')

        CricketNews.objects.create(
            heading=heading,
            subheading=subheading,
            content=content,
            link=link,
            image=image,
            video=video
        )
        return redirect('cricket_news')
    return render(request, 'cricket_news.html')


def announcements(request):
    if request.method == 'POST':
        heading = request.POST['announcement_heading']
        date = request.POST['announcement_date']
        info = request.POST['announcement_info']
        image = request.FILES.get('announcement_image')
        Announcement.objects.create(heading=heading, date=date, info=info, image=image)
        messages.success(request, " Announcement has been successfully added in Database.")
        return redirect('announcements')
    return render(request, 'announcements.html')

def results(request):
    if request.method == 'POST':
        heading = request.POST['result_heading']
        date = request.POST['result_date']
        image = request.FILES['result_image']
        Result.objects.create(heading=heading, date=date, image=image)
        return redirect('results')
    return render(request, 'results.html')



def upload_slider(request):
    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]
        obj = SliderImage(image=image)
        obj.save()
        return redirect("upload_slider")
    slider_images = SliderImage.objects.all()
    return render(request, "upload_slider.html", {"slider_images": slider_images})


# Upload Team Member
def upload_team(request):
    if request.method == "POST" and request.FILES.get("image") and request.POST.get("name"):
        name = request.POST["name"]
        role = request.POST["role"]
        image = request.FILES["image"]
        linkedin = request.POST.get("linkedin", "")
        instagram = request.POST.get("instagram", "")
        facebook = request.POST.get("facebook", "")
        obj = TeamMember(name=name,role=role,image=image,linkedin=linkedin, instagram=instagram, facebook=facebook)
        obj.save()
        return redirect("upload_team")
    team = TeamMember.objects.all()
    return render(request, "upload_team.html", {"team": team})


def gallery_upload(request):
    if request.method == "POST":
        image_file = request.FILES.get("image")
        title = request.POST.get("title")

        if image_file:
            GalleryImage.objects.create(image=image_file, title=title)
            return redirect("gallery_upload")  # name from urls.py

    gallery_images = GalleryImage.objects.all().order_by("-uploaded_at")
    return render(request, "gallery_upload.html", {"gallery_images": gallery_images})