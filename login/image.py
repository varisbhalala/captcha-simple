import random
from PIL import Image , ImageDraw , ImageFont
import hashlib
from django.http import HttpResponse
import string

class Captcha_Simple():
    def img_captcha(request):
        random_string = ''.join(random.choices(string.ascii_uppercase , k=4))
        final = random_string.encode('utf-8')
        hash_object = hashlib.sha256(final)

        print("string---",hash_object.hexdigest())
        size = (50,50)
        request.session['captcha_key'] = hash_object.hexdigest()
        im = Image.new('RGB' , size)
        draw = ImageDraw.Draw(im)
        color = (255,255,255)
        text_pos = (8 , 20)
        font = ImageFont.truetype('/Users/varis.bhalala/Desktop/captcha_test/arial.ttf',13)
        draw.text(text_pos,random_string,font=font)

        response = HttpResponse(content_type="image/png")
        im.save(response, 'PNG')
        print(type(im))
        return response
