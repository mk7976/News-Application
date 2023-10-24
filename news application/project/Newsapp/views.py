from django.shortcuts import render
import requests
import json
import random
from .models import Information

# Create your views here.


bussinesslist = []
technologylist = []
healthlist = []
politicslist = []
sportslist = []


def Home(request):
    Homelist = []
    navbarlist = []

    def ArticleCatchforBodyFunction():

        for i in range(0, 5):
            categorychoice = ["sports", "technology", "politics", "health", "business"]
            category = categorychoice[i]
            country = "in"
            url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=2a9287396d6746d28fbac9b5e7fd8398"

            responce = requests.get(url)

            data = json.loads(responce.text)
            if data["status"] == "ok":
                articles = data["articles"]
                for article in articles:
                    if type(article) == dict:
                        if ((article["title"] is None) or (article["title"] == '[Removed]')) or ((
                                                                                                         article[
                                                                                                             "description"] is None) or (
                                                                                                         article[
                                                                                                             "description"] == '[Removed]')) or (
                                (
                                        article["url"] is None) or (article["url"] == '[Removed]')) or (
                                (article["content"] is None) or (article["content"] == '[Removed]')) or (
                                (article["urlToImage"] is None) or (article["urlToImage"] == '[Removed]')):
                            a = 0


                        else:
                            if (i == 0):

                                if len(sportslist) == 0 or len(sportslist) != 0:
                                    sportslist.append(article)
                                    Homelist.append(article)
                                    if len(Homelist) == (len(sportslist) - 5):
                                        break

                            if (i == 1):
                                if len(technologylist) == 0 or len(technologylist) != 0:
                                    technologylist.append(article)
                                    Homelist.append(article)
                                    if len(Homelist) == (len(sportslist) - 5) + (len(technologylist) - 5):
                                        break

                            if (i == 2):
                                if len(politicslist) == 0 or len(politicslist) != 0:
                                    politicslist.append(article)
                                    Homelist.append(article)
                                    if len(Homelist) == (len(sportslist) - 5) + (len(technologylist) - 5) + (
                                            len(politicslist) - 5):
                                        break

                            if (i == 3):
                                if len(healthlist) == 0 or len(healthlist) != 0:
                                    healthlist.append(article)
                                    Homelist.append(article)
                                    if len(Homelist) == (len(sportslist) - 5) + (len(technologylist) - 5) + (
                                            len(politicslist) - 5) + (len(healthlist) - 5):
                                        break

                            if (i == 4):
                                if len(bussinesslist) == 0 or len(bussinesslist) != 0:
                                    bussinesslist.append(article)
                                    Homelist.append(article)
                                    if len(Homelist) == (len(sportslist) - 5) + (len(technologylist) - 5) + (
                                            len(politicslist) - 5) + (len(
                                        healthlist) - 5) + (len(bussinesslist) - 5):
                                        break

    ArticleCatchforBodyFunction()

    def Uspoliticsfunction():

        categorychoice = ["sports", "technology", "politics", "health", "business"]
        category = "politics"
        country = "us"
        url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=2a9287396d6746d28fbac9b5e7fd8398"

        responce = requests.get(url)

        data = json.loads(responce.text)
        if data["status"] == "ok":
            articles = data["articles"]
            for article in articles:
                if type(article) == dict:
                    if ((article["title"] is None) or (article["title"] == '[Removed]')) or ((
                                                                                                     article[
                                                                                                         "description"] is None) or (
                                                                                                     article[
                                                                                                         "description"] == '[Removed]')) or (
                            (
                                    article["url"] is None) or (article["url"] == '[Removed]')) or (
                            (article["content"] is None) or (article["content"] == '[Removed]')) or (
                            (article["urlToImage"] is None) or (article["urlToImage"] == '[Removed]')):
                        a = 0

                    # l1.append(article)
                    # print(len(l1))
                    else:
                        Homelist.append(article)
                        politicslist.append(article)

                        # print(article)
                        # print("The End")

        # print(len(l2))

    Uspoliticsfunction()

    print("sport:", len(sportslist))
    print("Home:", len(Homelist))
    print("politics:", len(politicslist))
    print("bussiness:", len(bussinesslist))
    print("health:", len(healthlist))
    print("technology:", len(technologylist))

    print("Homelist after fucntion", len(Homelist))

    homelist = []
    for i in range(0, len(Homelist) * 3000):
        c = random.randint(0, len(Homelist) - 1)
        d = Homelist[c]
        if d not in homelist:
            homelist.append(d)

    print("homelist after reararrging", len(homelist))

    for i in homelist:
        if len(navbarlist) < 10:
            navbarlist.append(i)

    navlist = []

    for i in range(0, len(navbarlist) * 100):
        c = random.randint(0, len(navbarlist) - 1)
        d = navbarlist[c]
        if d not in navlist:
            navlist.append(d)

    navactivelist = []

    navactivelist.append(navlist[0])
    navlist.pop(0)

    slidelist = [f"Slide {i + 1}" for i in range(1, len(navlist) + 1)]

    nlist = [i for i in range(1, len(navlist) + 1)]

    print("homelist:", len(homelist))
    print("navlist:", len(navlist))

    return render(request, "home.html", {"total": homelist, "navlist": navlist,
                                         "navactivelist": navactivelist, "slidelist": slidelist, "nlist": nlist})


def businessPage(request):
    return render(request, "bussiness.html", {"total": bussinesslist})


def HealthPage(request):
    return render(request, "Health.html", {"total": healthlist})


def PoliticalPage(request):
    politicslist2 = []
    for i in range(0, len(politicslist) * 10):
        c = random.randint(0, len(politicslist) - 1)
        d = politicslist[c]
        if d not in politicslist2:
            politicslist2.append(d)

    return render(request, "political.html", {"total": politicslist2})


def TechnologyPage(request):
    return render(request, "technology.html", {"total": technologylist})


def SportsPage(request):
    return render(request, "Sports.html", {"total": sportslist})


def Contact(request):
    return render(request, "contact.html")


def SendMassage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST["email"]
        message = request.POST["message"]
        subject = request.POST["subject"]
        a = Information(Name=name, Email=email, Message=message, Subject=subject)
        a.save()
        message1 = "Your Quarry message was submitted.thank you!"





    else:
        message1 = "message is not sent."
        print("message is not sent")
    return render(request, "contact.html", {"total": message1})


def About(request):
    return render(request, "about.html")


print("The End")
