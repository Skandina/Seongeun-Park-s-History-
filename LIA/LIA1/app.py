from flask import Flask
from flask import request
from flask import jsonify
import io
import base64
import json
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import textwrap
Image.MAX_IMAGE_PIXELS = None

app = Flask(__name__)

#Getting the data from json:
@app.post("/")
def home():
    data = request.get_json()
    txt = data.get('text', '')
    imstr = data.get('img', '')
    str_x1 = data.get('x1','')
    str_x2 = data.get('x2','')
    str_y1 = data.get('y1','')
    str_y2 = data.get('y2','') 
    x1 = int(str_x1) 
    y1 = int(str_y1)
    x2 = int(str_x2)
    y2 = int(str_y2) 
    tbox_w = (x2-x1) 
    tbox_h = (y2-y1)

# Opening the image using Pillow (import PIL)
    img = Image.open(io.BytesIO(base64.b64decode(imstr)))
    draw = ImageDraw.Draw(img)
    shape = (x1, y1, x2, y2)
    draw.rectangle(shape, outline="red")
    
#Getting Maxfontsize first
    Maxfontsize = 1
    fnt = ImageFont.truetype("impact.ttf", Maxfontsize)
    wordwraplenth = len(txt)
    i = 0
    bbox = draw.textbbox((x1,y1), txt, font=fnt)
    bbox_w = bbox[2]-bbox[0]
    bbox_h = bbox[3]-bbox[1]
    
    while bbox_w <= tbox_w or bbox_h <= tbox_h:
        Maxfontsize += 10
        fnt = ImageFont.truetype("impact.ttf", Maxfontsize)
        bbox = draw.textbbox((x1,y1), txt, font=fnt)
        bbox_w = bbox[2]-bbox[0]
        bbox_h = bbox[3]-bbox[1]
        if bbox_w > tbox_w and bbox_h > tbox_h:
            break    

# Wrapping the text and adjust fontsize 
    for i in range(500): 
            bbox = draw.textbbox((x1,y1), txt, font=fnt)
            bbox_w = bbox[2]-bbox[0]
            bbox_h = bbox[3]-bbox[1]
            if bbox_w >= tbox_w and bbox_h > tbox_h:
                Maxfontsize -= 10
                fnt = ImageFont.truetype("impact.ttf", Maxfontsize)
            if bbox_w > tbox_w and bbox_h < tbox_h: 
                 wordwraplenth = int(wordwraplenth - wordwraplenth/10)
                 wrapper = textwrap.TextWrapper(width=wordwraplenth)
                 txt = wrapper.fill(text=txt)
                 fnt = ImageFont.truetype("impact.ttf", Maxfontsize)
            if bbox_w < tbox_w and bbox_h >= tbox_h:
                newlenth = int(wordwraplenth + wordwraplenth/5)
                wrapper = textwrap.TextWrapper(width=wordwraplenth)
                txt = wrapper.fill(text=txt)
                fnt = ImageFont.truetype("impact.ttf", Maxfontsize)
                Maxfontsize -= 5
            if bbox_w <= tbox_w and bbox_h <= tbox_h:
                break

#Write the text at the center   
    positionx = int(x1 + (tbox_w/2))
    positiony = int(y1 + (tbox_h/2))
    draw.text((positionx, positiony), txt, anchor="mm", align="center", font=fnt)

#Getting the Base64 encoded result
    buffered  = io.BytesIO()
    img.save(buffered, format="JPEG")
    result = base64.b64encode(buffered.getvalue()).decode("utf-8")
    response = {'img':result}
    return jsonify(response)

if __name__=="__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5031)
