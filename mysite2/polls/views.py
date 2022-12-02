from django.shortcuts import render, loader
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .forms import OwnerForm, PetForm
from .models import Owner, Pet


# Create your views here.

def home(request):
    return render(request, "polls/home.html")


def add_owner(request):
    if request.method == "POST":
        f = OwnerForm(request.POST)
        if f.is_valid():
            f.save()
    f = OwnerForm()
    return render(request, "polls/register_owner.html", {"owner_form": f})


def add_pet(request):
    if request.method == "POST":
        f = PetForm(request.POST)
        if f.is_valid():
            f.save()
    f = PetForm()
    return render(request, "polls/register_pet.html", {"pet_form": f})


def list_of_owners(request):
    owner_list = Owner.objects.all()
    template = loader.get_template("polls/list_of_owners.html")
    context = {"owner_list": owner_list}
    # print("AAAAAAAAAAA")
    # print(owner_list)
    # for o in owner_list:
    #     print(o.name)
    #     print(o.id)
    return HttpResponse(template.render(context, request))


def owner_profile(request, owner_id):
    # print("BBBBBBBBBBBBBB")
    # print("owner_id", owner_id)
    owner = Owner.objects.get(id=owner_id)
    # print("owner:", owner)
    # print("o_n", owner.name)
    # owners_pets = Pet.objects.filter(owner_name=owner.name)

    owners_pets = owner.pet_set.all()
    owners_pets2 = Pet.objects.filter(owner_name=owner)

    # print("AAAAAAAAAAA")
    # print(owners_pets)
    return render(request, "polls/owner_profile.html", {"owners_pets": owners_pets2, "owners_name": owner.name})


class OwnersList(ListView):
    model = Owner


class OwnerDetails(DetailView):
    model = Owner


def cookie(request):
    print(request.COOKIES)
    resp = HttpResponse("C is for cookie and thats all..")
    resp.set_cookie("zap", 36)  # no expiration date-> until browser is closed
    resp.set_cookie("sai", 42, max_age=1000)  # exp date: 1000 seconds
    return resp


def sessfun(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4: del (request.session["num_visits"])
    return HttpResponse("view count: " + str(num_visits))


def detail(request):
    pass