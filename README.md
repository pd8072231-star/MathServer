# Ex.05 Design a Website for Server Side Processing
## Date:

## AIM:
 To design a website to calculate the Body Mass Index (BMI) in the server side. 


## FORMULA:
BMI = W/H<sup>2</sup>
<br> BMI --> Body Mass Index
<br> W --> Weight
<br> H --> Height

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
bmi.html
<html>
  <head>
      <title>BMI CALCULATOR -P.Dharshini(25010127)</title>
  </head>
  <style>
    body {
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      background: linear-gradient(135deg, #a8edea, #fed6e3);
    }
    .formelt {
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      border: 3px dotted #007BFF; /* dotted border */
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      text-align: center;
      width: 280px;
    }
    h1 {
      margin-bottom: 15px;
      color: #007BFF;
    }
    
    input[type="text"] {
      width: 100%;
      padding: 8px;
      margin-top: 5px;
      border: 2px solid #007BFF;
      border-radius: 4px;
    }
    button {
      margin-top: 15px;
      padding: 10px;
      width: 100%;
      background: #007BFF;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-weight: bold;
    }
    button:hover {
      background: #0056b3;
    }
  </style>
<body>
  <div class="container">
    <h1>BMI Calculator-P.Dharshini(25010127)</h1>
    <form method="POST">
    {%csrf_token%}
    <div class="formelt">
    Height:<input type="text" name="height" value="{{h}}"></input>(in cm)<br/>
    </div>
    <div class="formelt">
    Weight:<input type="text" name="weight" value="{{w}}"></input>(in kg)<br/>
    </div>
    <div class="formelt">
    <input type="submit" value="Calculate"></input><br/>
    </div>
    <div class="formelt">
    BMI:<input type="text" name="bmi" value="{{BMI}}"></input>kg/cm<sup>2</sup><br/>
    </div>
    </form>
    </div>
  </div>
  </body>
  </html>

urls.py
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('calculate_BMI/', views.calculate_BMI, name = "BMI"),
    path('', views.calculate_BMI, name="BMIapp")
]

views.py
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

# SERVER SIDE PROCESSING:
![alt text](<DharshiniP/mathapp/Screenshot (162).png>)

## HOMEPAGE:
![alt text](<DharshiniP/mathapp/Screenshot (163).png>)

## RESULT:
The program for performing server side processing is completed successfully.
