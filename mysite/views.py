# I have created this file
from django.http import HttpResponse
import os
from django.shortcuts import render


def index(req):
    # return HttpResponse("Home")
    # params = {'name': 'Rahul', 'place': 'Mars'}
    # return render(req, 'index.html', params)
    return render(req, 'index.html')


def analyze(req):
    # get the text
    djtext = req.POST.get('text', 'default')

    # check the checkbox values
    removePunctuation = req.POST.get('removePunctuation', 'off')
    fullCaps = req.POST.get('fullCaps', 'off')
    newLineRemover = req.POST.get('newLineRemover', 'off')
    extraSpaceRemover = req.POST.get('extraSpaceRemover', 'off')
    charCounter = req.POST.get('charCounter', 'off')

    print(removePunctuation)
    analyzed = ""
    punctuations = '''!()-[]{}:;'"\,<>/?@#$%^&*_~'''
    if removePunctuation == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(req, 'analyze.html', params)
    if fullCaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to upperCase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(req, 'analyze.html', params)
    if newLineRemover == 'on':
        analyzed = ""
        for char in djtext:
            if (char != "\n" and char != '\r'):
                analyzed = analyzed+char
        params = {'purpose': 'Removed new Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(req, 'analyze.html', params)
    if extraSpaceRemover == "on":
        analyzed = ""
        prev = 'a'
        for char in djtext:
            if (char == ' ' and prev == ' '):
                continue
            else:
                analyzed = analyzed+char
            prev = char
        params = {'purpose': "Removed extra spaces", 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(req, 'analyze.html', params)
    if (charCounter == 'on'):
        cnt = 0
        for char in djtext:
            cnt = cnt+1
        params = {'purpose': "Count the number of characters",
                  'analyzed_text': cnt}
        return render(req, 'analyze.html', params)

    params = {'purpose': 'No filter selected', 'analyzed_text': djtext}
    return render(req, 'analyze.html', params)


# def capatalize(req):
#     return HttpResponse("capatalize the data")


# def newLineRemove(req):
#     return HttpResponse("remove the new line from the data")


# def capFirst(req):
#     return HttpResponse("capatalize the first letter")


# def spaceRemove(req):
#     return HttpResponse("Remove space from the data")


# def charCount(req):
#     return HttpResponse("count the number of characters in the data")
