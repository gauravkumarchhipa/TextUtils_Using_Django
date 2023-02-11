# I have created this file - gaurav

from django.http import HttpResponse
# template
from django.shortcuts import render

# def index(request):
#     return HttpResponse("<h1>this is home page</h1>")
#
# #about page
#
# def about(request):
#     return HttpResponse("this is about page")
#
# # File Read
#
# def read_file(request):
#     f = open('path/1.txt', 'r')
#     file_content = f.read()
#     f.close()
#     return HttpResponse(file_content, context_type="text/plain")
#
# # Navigation
#
# def navigation(request):
#     return HttpResponse(''' <h1>open youtube </h1> <a href="https://www.youtube.com/">youtube</a>
#     <h1>open google </h1> <a href="https://www.google.com/">google</a>
#     <h1>open facebook </h1> <a href="https://www.facebook.com/">facebook</a>''')

# pipeline
# template


def index(request):
    # return HttpResponse("Home")
    # params = {'name': 'gaurav', 'place': 'India'}
    # return render(request, 'index.html', params)
    return render(request, 'index.html')
######################

# def removepunch(request):
#     #get the text
#     djtext = request.GET.get('text','default')
#     print(djtext)
#     # analyze the text
#     return HttpResponse("removepunch")

# def capitalizefirst(request):
#     return HttpResponse("capitalizefirst")
#
# def spaceremove(request):
#     return HttpResponse('''space remover <a href="/">back</a>''')
#
# def charcount(request):
#     return HttpResponse("charcount")


###########################

# def analyze(request):
#     #get the text
#     djtext = request.GET.get('text','default')
#     removepunch = request.GET.get('removepunch', 'off')
#     print(removepunch)
#     print(djtext)
#     # analyze the text
#     return HttpResponse("analyze")


############################################

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')

    # print(djtext)
    # check checkbox values
    removepunch = request.POST.get('removepunch', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # print(removepunch)
    # print(djtext)

    # check which checkbox is on
    if removepunch == "on":
        analyzed = djtext
        punctuations = ''' !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ '''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose' : 'Removed Punctuatuins', 'analyzed_text': analyzed}

        djtext = analyzed

        # analyze the text
        # return render(request,'analyze.html', params)
#################################################
    # elif(fullcaps=="on"):
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}

        djtext = analyzed

        # return render(request, 'analyze.html', params)
##################################
    # elif (newlineremover == "on"):
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'remove New Line', 'analyzed_text': analyzed}

        djtext = analyzed

        # return render(request, 'analyze.html', params)
###############################
    # elif (spaceremover == "on"):
    if (spaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'remove New Line', 'analyzed_text': analyzed}

        djtext = analyzed

        # return render(request, 'analyze.html', params)
##################################################

    # elif (charcount == "on"):
    if (charcount == "on"):
        analyzed = ""
        for char in djtext:
            djtext.count()
            analyzed = analyzed + char
        params = {'purpose': 'remove New Line', 'analyzed_text': analyzed}

        # djtext = analyzed
    if(removepunch != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on" and charcount != "on"):
        return HttpResponse("Error")
        # return render(request, 'analyze.html', params)
    # else :
    #     return HttpResponse("Error")
    return render(request, 'analyze.html', params)

    ##########################################
    ##exercise #####

