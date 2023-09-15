from django.contrib import admin

from options_app.models import Footer, Carousel


# Register your models here.


@admin.register(Footer)
class AuthorAdmin(admin.ModelAdmin):

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionality
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Carousel)
class AuthorAdmin(admin.ModelAdmin):

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        if Carousel.objects.all().count() >= 5:
            return False
        return True

