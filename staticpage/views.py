from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import PageForm
from .models import Page
from .tasks import generate_static_page


def page_create(request):
    print("Lll")
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save()
            print(page)
            generate_static_page.delay(page.id, page.title, page.body)
            print("kkk")
            return redirect(reverse('page_detail', args=[str(page.pk)]))
    else:
        form = PageForm()

    return render(request, 'staticpage/base.html', {'form': form})


def page_detail(request, pk):
    page = get_object_or_404(Page, id=pk)
    return render(request, 'staticpage/detail.html', {'page': page})
