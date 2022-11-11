from django.urls import path

from . import views


appapp_name='auctions'
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("wishlist/add_to_wishlist/<int:id>", views.add_to_wishlist, name="add_to_wishlist"), 
    path("bid/<int:id>", views.bid, name="bid"),
    path('<slug:category_slug>', views.index, name='auctions_by_category'),
    # path("listing/<int:listing_id>",)
]
