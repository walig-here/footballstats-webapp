from django.http import HttpRequest, HttpResponse, FileResponse
from django.views import View
from django import forms


class _UploadFileForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    file = forms.ImageField(required=True)
    type = forms.ChoiceField(choices=[
        ("PLAYER", "PLAYER"),
        ("COUNTRY", "COUNTRY"),
        ("LEAGUE", "LEAGUE"),
        ("TEAM", "TEAM"),
    ])

class ServeImageView(View):
    def get(self, request: HttpRequest, file_path: str) -> FileResponse:
        raise NotImplementedError


# Create your views here.
class UploadImageView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        raise NotImplementedError