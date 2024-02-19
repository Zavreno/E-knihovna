from django import forms
from .models import Book


class CreateNewBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "genre",
            "publisher",
            "price",
            "web_price",
            "pub_date",
            "image",
        ]

        labels = {
            "title": "Titulek",
            "author": "Autor",
            "genre": "Kategorie",
            "publisher": "Vydavatel",
            "price": "Cena",
            "web_price": "Cena na internetu",
            "pub_date": "Datum vydání",
            "image": "Obrázek",
        }


class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "genre",
            "publisher",
            "price",
            "web_price",
            "pub_date",
            "image",
        ]

        labels = {
            "title": "Titulek",
            "author": "Autor",
            "genre": "Kategorie",
            "publisher": "Vydavatel",
            "price": "Cena",
            "web_price": "Cena na internetu",
            "pub_date": "Datum vydání",
            "image": "Obrázek",
        }