from django import forms

from .models import Artwork, Review


class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = [
            'title',
            'slug',
            'category',
            'description',
            'technique',
            'image',
            'year',
            'dimensions',
            'price',
            'is_available',
            'is_featured',
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
