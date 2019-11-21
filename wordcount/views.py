from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.htm')


def aboutus(request):
    return render(request, 'about.htm')


def count(request):
    your_text = request.GET['fulltext']
    wordlist = your_text.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] = worddictionary[word] + 1
        else:
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(),
                         key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.htm', {'your_text': your_text, 'count': len(wordlist), 'sortedwords': sortedwords})
