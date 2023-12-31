from django.urls import path
from shop_main_app.views import PopularProductListView, ProductDetailView, CategoryListView, SearchListView, \
    UserLoginView, UserCreateView, UserLogoutView, ProfileInfoDetailsView, ProfileUpdateView, UserUpdatePasswordView, \
    GeneratePDFView

urlpatterns = [
    path('', PopularProductListView.as_view(), name='main'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_details'),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category_list'),
    path('search/', SearchListView.as_view(), name='search'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileInfoDetailsView.as_view(), name='profile_details'),
    path('profile-update/<int:pk>', ProfileUpdateView.as_view(), name='profile_update'),
    path('user-update-password/<int:pk>', UserUpdatePasswordView.as_view(), name='update_password'),
    path('render-invoice/<int:pk>', GeneratePDFView.as_view(), name='render_invoice')
]
