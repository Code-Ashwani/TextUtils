# I have created this file - Ashwani Kumar

from django.shortcuts import render


# homepage for website
def index(request):
    return render(request, 'index.html')


# analyze function to analyze the text
def analyze(request):

    # getting data from website
    djtext = request.POST.get('text', 'default')
    punctuation = request.POST.get('punchCheck', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    countchar = request.POST.get('countchar', 'off')

    analyzed = ""
    punctuations = '''[]{}()~!@#$%^&*-_+=/?<>,.;:'"'''

    # checking user selected functions for analyzing text
    if punctuation == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = djtext.upper()

    if countchar == 'on':
        count = 0
        for char in djtext:
            if char is not " ":
                count += 1
        analyzed = analyzed + "  : Charcter count : " + str(count)

    params = {'purpose': 'Processing Input Text', 'analyzed_text': analyzed}

    # for error purpose
    if countchar != 'on' and fullcaps != 'on' and punctuation != 'on':
        params = {'purpose': 'Processing Input Text', 'analyzed_text': analyzed,
                  'error': 'Please Do Click on "Home" button and try again by selecting Functions'}
        return render(request, 'error.html', params)

    # in-case everything passes
    return render(request, 'analyzer.html', params)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
