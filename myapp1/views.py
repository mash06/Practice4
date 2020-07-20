from django.shortcuts import render
from myapp1 import main

# Create your views here.
def index(request):
    return render(request,'myapp1/FIRST.html')

def podschet(request):
    num3 = 0
    vkid = request.POST['num1']
    print(vkid)
    dictionary=main.readfromfile(vkid)
    #dictionary= main.readfromfile(vkid)
    if (vkid==dictionary[0]):
      print(dictionary[0])
      friends=dictionary[vkid][0]
      print(friends)
      followers=dictionary[vkid][1]
      photos=dictionary[vkid][2]
      grade = ""

      num3=(int(friends)+int(followers)+int(photos))/3

    if (num3<=242):
        grade="ОТЛИЧНИК"

    if(num3>242 and num3<=410):
        grade = "ХОРОШИСТ"

    if (num3 > 410 and num3 <=789):
        grade = "ТРОЕЧНИК"

    if (num3 > 789):
        grade = "ДВОЕЧНИК"

    params = {'dictionary1': dictionary[0],'dictionary2': dictionary[1], 'dictionary3': dictionary[2],'grade': grade}
    return render(request, 'myapp1/SECOND.html', params)



