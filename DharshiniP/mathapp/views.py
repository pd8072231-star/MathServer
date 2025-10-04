from django.shortcuts import render
def calculate_BMI(request):
  context = {}
  context['BMI'] = float("0")
  context['height'] =float("0")
  context['weight'] = float("0")
  if (request.method=="POST"):
    print("POST method is used")
    h = request.POST.get("height","0")
    w = request.POST.get("weight","0")
    print("Request=", request)
    print("Height=", h)
    print("Weight=", w)
    BMI = float(w)/((float(h)*float(h))/100)
    context['BMI'] = BMI
    context['height'] = h
    context['weight'] = w
    print("BMI=", BMI)
  return render (request,'mathapp/bmi.html',context)