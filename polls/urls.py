from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    AuthorBookListView,
    CreateNewBookView,
    BookCategoryListView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path("", BookListView.as_view(), name="index"),
    path("seznam_knih/", BookListView.as_view(template_name="polls/fast_book.html"), name="fast-book"),
    path("detail/<int:pk>", BookDetailView.as_view(), name="book-detail"),
    path("autor/<str:author>", AuthorBookListView.as_view(), name="author-books"),
    path("nova_kniha/", CreateNewBookView.as_view(), name="new-book"),
    path("<str:genre>/", BookCategoryListView.as_view(), name="book-category"),
    path("<int:pk>/uprava/", BookUpdateView.as_view(), name="book-update"),
    path("<int:pk>/odstraneni", BookDeleteView.as_view(), name="book-delete"),
    path("seznam_knih/<str:genre>/", BookCategoryListView.as_view(template_name="polls/fast_book_category.html"), name="fast-book-category"),
]