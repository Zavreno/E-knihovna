from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView
from .models import Book
from .forms import CreateNewBookForm, BookUpdateForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q


class BookListView(ListView):
    model = Book
    template_name = "polls/index.html"
    context_object_name = "book_list"
    ordering = ["-up_date"]
    paginate_by = 28

    def get(self, request, *args, **kwargs):
        if kwargs.get("template_type") == "fast-book":
            self.template_name = "polls/fast_book.html"
        return super().get(request, *args, **kwargs)

    def get_paginate_by(self, queryset):
        if self.request.path == "/seznam_knih/":
            return 40
        return self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Knihy"
        context["genre_choices"] = Book.GENRE_CHOICES
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        sort_by = self.request.GET.get("sort_by")
        if query:
             queryset = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(genre__icontains=query))

        else:
             queryset = Book.objects.all().order_by("-up_date")

        if sort_by == "up_date":
            queryset = queryset.order_by("-up_date")
        elif sort_by == "title":
            queryset = queryset.order_by("title")
        elif sort_by == "author":
            queryset = queryset.order_by("author")
        elif sort_by == "price":
            queryset = queryset.order_by("price")
        elif sort_by == "pub_date":
            queryset = queryset.order_by("pub_date")

        return queryset


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.title
        context["genre_choices"] = Book.GENRE_CHOICES
        context["similar_book_list"] = Book.objects.filter(title=self.object.title).exclude(pk=self.object.pk)
        return context


class AuthorBookListView(ListView):
    model = Book
    template_name = "polls/author_books.html"
    context_object_name = "book_list"
    paginate_by = 15

    def get_queryset(self):
        book_author = self.kwargs.get("author")
        sort_by = self.request.GET.get("sort_by")
        queryset = Book.objects.filter(author=book_author)

        if sort_by == "up_date":
            queryset = queryset.order_by("-up_date")
        elif sort_by == "title":
            queryset = queryset.order_by("title")
        elif sort_by == "author":
            queryset = queryset.order_by("author")
        elif sort_by == "price":
            queryset = queryset.order_by("price")
        elif sort_by == "pub_date":
            queryset = queryset.order_by("pub_date")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.kwargs.get("author")
        context["genre_choices"] = Book.GENRE_CHOICES
        return context


class CreateNewBookView(FormView):
    template_name = "polls/new_book.html"
    form_class = CreateNewBookForm
    success_url = reverse_lazy("index")
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Kniha byla přidána!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Přidat knihu"
        context["genre_choices"] = Book.GENRE_CHOICES
        return context


class BookCategoryListView(ListView):
    model = Book
    template_name = "polls/book_category.html"
    context_object_name = "book_list"
    ordering = ["-up_date"]
    paginate_by = 40

    def get(self, request, *args, **kwargs):
        if kwargs.get("template_type") == "fast-book-category":
            self.template_name = "polls/fast_book_category.html"
        return super().get(request, *args, **kwargs)

    def get_paginate_by(self, queryset):
        if self.request.path == "/seznam_knih/<str:genre>/":
            return 40
        return self.paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.kwargs.get("genre")
        context["genre_choices"] = Book.GENRE_CHOICES
        return context

    def get_queryset(self):
        genre_filter = self.kwargs.get("genre")
        sort_by = self.request.GET.get("sort_by")
        queryset = Book.objects.filter(genre=genre_filter).order_by("-up_date")

        if sort_by == "up_date":
            queryset = queryset.order_by("-up_date")
        elif sort_by == "title":
            queryset = queryset.order_by("title")
        elif sort_by == "author":
            queryset = queryset.order_by("author")
        elif sort_by == "price":
            queryset = queryset.order_by("price")
        elif sort_by == "pub_date":
            queryset = queryset.order_by("pub_date")

        return queryset


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookUpdateForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        messages.success(self.request, "Změny byly uloženy!")
        return reverse_lazy("book-detail", kwargs={"pk":self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Upravit knihu"
        context["genre_choices"] = Book.GENRE_CHOICES
        return context


class BookDeleteView(DeleteView):
    model = Book

    def get_success_url(self):
        deleted_book = self.get_object()
        deleted_book_title = deleted_book.title
        messages.success(self.request, f"Kniha { deleted_book_title } byla odstraněna!")
        return reverse_lazy("fast-book")
