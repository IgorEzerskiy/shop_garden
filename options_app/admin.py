from django.contrib import admin

from options_app.models import Footer, Carousel, ShippingAndBilling, ReturnPolicy, AboutInfo, ContactForm, \
    TextAtMainPage, TelegramBotConfig


# Register your models here.

@admin.register(TelegramBotConfig)
class AuthorAdmin(admin.ModelAdmin):

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        if TelegramBotConfig.objects.all().count() >= 1:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Footer)
class AuthorAdmin(admin.ModelAdmin):

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        if Footer.objects.all().count() >= 1:
            return False
        return True

    # This will help you to disable delete functionality
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Carousel)
class AuthorAdmin(admin.ModelAdmin):

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        if Carousel.objects.all().count() >= 5:
            return False
        return True


@admin.register(ShippingAndBilling)
class AuthorAdmin(admin.ModelAdmin):

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        if ShippingAndBilling.objects.all().count() >= 1:
            return False
        return True


@admin.register(ReturnPolicy)
class AuthorAdmin(admin.ModelAdmin):

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        if ReturnPolicy.objects.all().count() >= 1:
            return False
        return True


@admin.register(TextAtMainPage)
class AuthorAdmin(admin.ModelAdmin):

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        if TextAtMainPage.objects.all().count() >= 1:
            return False
        return True


@admin.register(AboutInfo)
class AuthorAdmin(admin.ModelAdmin):

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        if AboutInfo.objects.all().count() >= 1:
            return False
        return True


@admin.register(ContactForm)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'message',)
    list_display = ('name', 'email', 'status',)

    # This will help you to disable add functionality
    def has_add_permission(self, request):
        return False
