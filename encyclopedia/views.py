from django.shortcuts import render
from markdown2 import Markdown

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
            "title": entry
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
            "search": True,
            "value": value
            })