from flask import render_template, request
import os, sys, platform
from flask import current_app as app
from datetime import datetime



@app.route("/blog")
def blog():
    news_dict = {
        'first day': 'I feel good',
        'Second Day': 'I feel bad',
        'Third Day': 'I happy',
    }
    return render_template("blog.html", news_dict=news_dict, sys_info=request.headers.get('User-Agent'),
                           sys=sys.version, os_name=os.name, platform=platform.system(), release=platform.release(),
                           date=datetime.now())


@app.route("/news")
def sale():
    sale_dict = {
        'Iphone x': '256$',
        'I Mac': '1999$',
        'Samsung s12': '599$',

    }
    return render_template("sale.html", sale_dict=sale_dict, sys_info=request.headers.get('User-Agent'),
                           sys=sys.version, os_name=os.name, platform=platform.system(), release=platform.release(),
                           date=datetime.now())


@app.route("/")
def aboutme():
    return render_template("aboutme.html", boolean=False, name='Svyatoslav', error='Wrong data',
                           sys_info=request.headers.get('User-Agent'), sys=sys.version, os_name=os.name,
                           platform=platform.system(), release=platform.release(), date=datetime.now())




