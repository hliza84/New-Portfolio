"""Module providingFunction printing python version."""
from django.contrib import admin
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
    Message,
)

# Register your models here.
admin.site.register(Person)
admin.site.register(PersonalInfo)
admin.site.register(MyExpertise)
admin.site.register(WhoAmI)
admin.site.register(Expertise)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Languages)
admin.site.register(DarkText)
admin.site.register(SocialInfo)
admin.site.register(ServiceText)
admin.site.register(Services)
admin.site.register(PortfolioText)
admin.site.register(Testimonials)
admin.site.register(TestPerson)
admin.site.register(ContactText)
admin.site.register(Message)
