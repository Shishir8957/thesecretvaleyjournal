from django.shortcuts import render
from .forms import TextForm

def index(request):
    form = TextForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # Additional logic when the text is saved
    return render(request, 'fileshare.html', {'form': form})
