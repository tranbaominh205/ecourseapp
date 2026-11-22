from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.utils.html import format_html

from courses.models import Category, Course, Lesson, Tag



class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseAppAdminSite(admin.AdminSite):
    site_header = 'Hệ thống khoá học trực tuyến'


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'course', 'image_view']
    list_filter = ['id', 'subject', 'created_date']
    search_fields = ['subject', 'course__subject']
    readonly_fields = ['image_view']
    form = LessonForm

    def image_view(self, lesson):
        if lesson.image:
            return format_html(
                '<img src="{}" width="120" alt="{}" />',
                lesson.image.url,
                lesson.subject,
            )
        return '-'

    image_view.short_description = 'Hình ảnh'

    class Media:
        css = {
            'all': ('css/style.css',)
        }


admin_site = CourseAppAdminSite(name='myadmin')
admin_site.register(Category)
admin_site.register(Course)
admin_site.register(Lesson, LessonAdmin)
admin_site.register(Tag)