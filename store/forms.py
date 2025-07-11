from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your review...'}),
        }

class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=100, label="Full Name")
    address = forms.CharField(widget=forms.Textarea, label="Shipping Address")
    phone = forms.CharField(max_length=15, label="Phone Number")
