# Ex.05 Book Front Cover Page Design
# Date:10-12-25
# AIM:
To design a book front cover page using HTML and CSS.

# DESIGN STEPS:
## Step 1:
Create a Django Admin project.

## Step 2:
Create an app in the Django interface.

## Step 3:
Create a folder named 'static' in the app folder.

## Step 4:
Create a new HTML file in the static folder.

## Step 5:
Write the HTML code with relevant CSS properties.

## Step 6:
Choose the appropriate style and color scheme.

## Step 7:
Insert the images in their appropriate places.

## Step 8:
Publish the website in the LocalHost.

# PROGRAM:
bookcover.html
```

{% load static %}
<html>
    <head>
        <title>bookpreview</title>
        <link rel="stylesheet" href="{% static 'CSS.css' %}">
    </head>
    <body>
        <div id="book">
            <h1>
                <span class="letter1">F</span>
                <span class="letter2">R</span>
                <span class="letter3">I</span>
                <span class="letter4">E</span>
                <span class="letter5">N</span>
                <span class="letter6">D</span>
                <span class="letter7">S</span>
            </h1>

            <hr>
            <img src="{% static 'creators.png' %}">
            <h5>
                The Iconic sitcom, was created and written By,<br>
                <strong>
                    <span class="creators">David Crane & Marta Kauffman</span>
                </strong>
            </h5>
        </div>
    </body>
</html>
```
CSS.css
```
    @font-face {
    font-family: 'FriendsFont';
    src: url('friends.TTF');
    }

    body {
        margin: 0;
        background-color: rgb(93, 93, 93);
    }

    #book {
        height: 700px;
        width: 490px;
        border: 5px solid black;
        background-image: url('backgroundd.jpg');
        background-size: cover;
        background-position: center;
        margin: 40px auto;
        position: relative;
    }

    #book h1 {
        text-align: center;
        letter-spacing: 3px;
        font-family: 'FriendsFont';
        font-size: x-large;
        width: 100%;
        top: 118px;
        left: 0;
        margin: 0;
        position: absolute;
    }
    .letter1 { color: red; }
    .letter2 { color: blue; }
    .letter3 { color: yellow; }
    .letter4 { color: red; }
    .letter5 { color: yellow; }
    .letter6 { color: blue; }
    .letter7 { color: red; }

    hr {
    position: absolute;
    width: 150px;    
    right: 22px;      
    border: none;   
    bottom: 220px;  
    border-top: 2px solid white; 
    margin-bottom: 10px; 
    }

    #book img {
        height: 120px;
        width: 120px;
        border-radius: 20%;
        position: absolute;
        bottom: 100px;
        right: 30px;
        background-color:black;
        padding: 3px;
    }

    #book h5 {
        position: absolute;
        bottom: 0;
        right: 30px;
        width: 200px;
        margin: 0%;
        text-align: center;
        color: white;
        font-family: Magneto;
        font-size: 16px;
        line-height: 1.2;
        padding-bottom: 5px;
    }
    .creators{
    color: yellow;
    }
```

views.py
```
from django.shortcuts import render

def book_preview(request):
    return render(request, 'bookcover.html')
```

urls.py
```
from django.contrib import admin
from django.urls import path
from coverr import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.book_preview),
]
```


# OUTPUT:
![alt text](book/coverr/static/bookoutput.png)

# RESULT:
The program for designing book front cover page using HTML and CSS is completed successfully.
