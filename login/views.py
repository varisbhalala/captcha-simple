from django.shortcuts import render , HttpResponseRedirect
from .forms import LoginForm
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
import json
import random
import string
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import hashlib


def login(request):
    form = LoginForm()
    return render(request,'login.html' , {'form' : form})

def login_check(request):
       if request.POST:
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        captcha = request.POST['captcha_text']
        captcha_input = captcha.encode('utf-8')
        hash_object = hashlib.sha256(captcha_input)
        # username = admin and password = admin is for demo
        # One can access parameters from dataabase dynamically 
        if username == 'admin' and password == 'admin' and hash_object.hexdigest() == request.session['captcha_key']:
            del request.session['captcha_key']
            human = True
            return render(request, 'welcome.html')
        else:
            form = LoginForm()
            return render(request,'login.html' , {'form' : form,'message' : 'Invalid Captcha'})
        
def refresh(request):
    to_json_response = dict()
    to_json_response['status'] = 0
    to_json_response['key'] = CaptchaStore.generate_key()
    to_json_response['image_url'] = captcha_image_url(to_json_response['key'])
    return HttpResponse(json.dumps(to_json_response), content_type='application/json')

def img_captcha(request):
    random_string = ''.join(random.choices(string.ascii_uppercase , k=4)).encode('utf-8')
    hash_object = hashlib.sha256(random_string)
    size = (50,50)
    request.session['captcha_key'] = hash_object.hexdigest()
    im = Image.new('RGB' , size)
    draw = ImageDraw.Draw(im)
    color = (255,255,255)
    text_pos = (8,20)
    font = ImageFont.truetype('/Users/varis.bhalala/Desktop/captcha_test/arial.ttf',13)
    draw.text(text_pos,random_string,font=font)
    response = HttpResponse(content_type="image/png")
    im.save(response, 'PNG')
    return response

    
