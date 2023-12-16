from django.shortcuts import render
from markdown2 import Markdown
import random

from . import util

def md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)


def index(request):
    return render(request, "encyclopedia\index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    html_content = md_to_html(entry)
    if html_content is not None:
        return render(request, "encyclopedia\entry.html", {
            "content": html_content,
            "title": entry
        })
    else: 
        return render(request, "encyclopedia\error.html", {
            "title": entry,
            "message": "This page doesn't exists"
        })
        
def search(request):
    if request.method == "POST":
        value = request.POST['q']
        html_content = md_to_html(value)
        if html_content is not None:
            return render(request, "encyclopedia\entry.html", {
            "content": html_content,
            "title": value
        })
        else:
            entries = []
            for entry in util.list_entries():
                if value.upper() in entry.upper():
                    entries.append(entry)
            return render(request, "encyclopedia\search.html", {
            "entries": entries,
            "value": value
            })
            
def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia\createPage.html")    
    else:
        title = request.POST['title']
        content = request.POST['content']
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia\error.html", {
                "message": "Page already exists"
            })
        else:
            util.save_entry(title, content)
            html_content = md_to_html(title)
            return render(request, "encyclopedia\entry.html", {
                "title": title,
                "content": html_content
            })
            
def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia\editPage.html", {
            "title": title,
            "content": content
        })
        
def saveEdit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = md_to_html(title)
        return render(request, "encyclopedia\entry.html", {
            "title": title,
            "content": html_content
            })


def rand(request):
    Entries = util.list_entries()
    choosen = random.choice(Entries)
    html_content = md_to_html(choosen)
    return render(request, "encyclopedia\entry.html", {
        "title": choosen,
        "content": html_content
        })