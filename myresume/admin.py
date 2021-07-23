from django.contrib import admin
from .models import ResumeUpload


@admin.register(ResumeUpload)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'contact', 'gender', 'father', 'mother', 'sivling',
                    'address', 'pin', 'home_town', 'education', 'experience', 'skill', 'language',
                    'hobbies', 'profile_img', 'document', 'date']
