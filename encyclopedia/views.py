from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.text import slugify

from .models import Pages
import markdown
from random import choice


def home_page(request):
    context = {}
    query = request.GET.get('q')
    if query:
        pages = Pages.objects.filter(title__icontains=query)
        context["pages"] = pages
        return render(request, 'encyclopedia/all_pages.html', context=context)

    return render(request, 'encyclopedia/home.html', context=context)


@login_required(login_url="login")
def create_page(request):
    context = {}
    query = request.GET.get('q')
    if query:
        pages = Pages.objects.filter(title__icontains=query)
        context["pages"] = pages
        return render(request, 'encyclopedia/all_pages.html', context=context)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('desc')
        Pages.objects.create(slug=slugify(title), user=request.user, title=title, description=description)
        return redirect("all")
    return render(request, 'encyclopedia/create_page.html')


def all_pages(request):
    pages = Pages.objects.all()
    query = request.GET.get('q')
    if query:
        pages = Pages.objects.filter(title__icontains=query)

    context = {
        "pages": pages
    }

    return render(request, 'encyclopedia/all_pages.html', context=context)


def delete_page(request, page_id):
    Pages.objects.get(id=page_id).delete()
    return redirect("all")


def edit_page(request, page_id):
    context = {}
    page = Pages.objects.get(id=page_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        page.title = title
        page.description = desc
        page.save()
        return redirect("all")
    context['page'] = page
    return render(request, 'encyclopedia/edit_page.html', context=context)


def detail_page(request, slug):
    context = {}
    page = Pages.objects.get(slug=slug)
    description = page.description
    markdown_to_html = markdown.markdown(description)

    context['page'] = page
    context['markdown_to_html'] = markdown_to_html
    return render(request, 'encyclopedia/detail_page.html', context=context)


def random_page(request):
    pages = Pages.objects.all()
    if pages:
        page = choice(pages)
        return redirect('detail', slug=page.slug)
    else:
        return redirect("all")


