from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import (
    Person,
    PersonalInfo,
    MyExpertise,
    WhoAmI,
    Expertise,
    Education,
    Skill,
    Languages,
    DarkText,
    SocialInfo,
    ServiceText,
    Services,
    PortfolioText,
    Testimonials,
    TestPerson,
    ContactText,
    PortfolioProject,
)
from .forms import MessageForm

# Create your views here.


def home(request):
    status = 200
    """Function home."""

    if request.method == "POST":
        print("POSTED DATA")
        form = MessageForm(request.POST)
        if form.is_valid():
            print("NEED TO SAVE")
            form.save()
            return redirect("/")
    person = Person.objects.all()
    personal_info = PersonalInfo.objects.all()
    my_expertise = MyExpertise.objects.all()
    who_am_i = WhoAmI.objects.all()
    expertise = Expertise.objects.all()
    education = Education.objects.all()
    skill = Skill.objects.all()
    language = Languages.objects.all()
    dark_text = DarkText.objects.all()
    social = SocialInfo.objects.all()
    servicetext = ServiceText.objects.all
    services = Services.objects.all()
    portfoliotext = PortfolioText.objects.all()
    testimonials = Testimonials.objects.all()
    testperson = TestPerson.objects.all()
    contacttext = ContactText.objects.all()
    messageForm = MessageForm()
    portfolioProject = PortfolioProject.objects.all()
    data = {
        "logo": "L|H",
        "personal_info": personal_info,
        "my_expertise": my_expertise,
        "Who_am_I": who_am_i,
        "Expertise": expertise,
        "Education": education,
        "Skills": skill,
        "Languages": language,
        "Dark_text": dark_text,
        "social": social,
        "servicetext": servicetext,
        "services": services,
        "person": person,
        "portfoliotext": portfoliotext,
        "testimonials": testimonials,
        "testperson": testperson,
        "contacttext": contacttext,
        "messageForm": messageForm,
        "portfolioProject": portfolioProject,

    }

    return render(request, "index.html", context=data, status=status)


def portfolio_project(request, pk):
    project = get_object_or_404(PortfolioProject, pk=pk)
    return render(request, "portfolio-details.html", context={"project": project})
