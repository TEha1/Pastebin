from django.urls import path
from .views import PublicPastebinCLView, PublicPastebinListView, CertainPastebinLCView, \
    PrivatePastebinLCView, PrivatePastebinRUDView, CertainPastebinListView, PasteByDate

urlpatterns = [
    path('pastebins/', CertainPastebinLCView.as_view(), name="view pastebins    (registered users"),
    path('pastebin/<int:pk>/', CertainPastebinListView .as_view(), name="get specific pastebin    (registered users)"),
    path('public/pastebins/', PublicPastebinCLView.as_view(), name="view pastebins   (guest users)"),
    path('public/pastebin/<int:pk>/', PublicPastebinListView .as_view(), name="get specific pastebin   (guest users)"),
    path('user/<int:pk>/pastebins/', PrivatePastebinLCView.as_view(), name="add and get specific pastebins of a specific  user  (registered users)"),
    path('user/<int:spk>/pastebin/<int:pk>/', PrivatePastebinRUDView.as_view(), name="get, delete and upadte specific pastebin of a specific user   (registered users)"),
    path('pastebin/date/', PasteByDate.as_view(), name="pastebin order by date   (registered users)"),
]
