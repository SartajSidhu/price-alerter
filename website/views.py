from flask import Blueprint, render_template, request, flash, redirect
from website.amazon import amazoncheck, alert
from website.walmart import wmcheck
#from website.alert import alert

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def az():
    data = request.form 
    if request.method == 'POST':
        url = request.form.get('url')
        desire = request.form.get('desire')
        email = request.form.get('email')
        desire = float(desire.replace('$', '').replace(',', '').strip())
        if (("@" in email)==False) or (("." in email)==False):
            flash("Please enter a valid email")
        else:
            if(amazoncheck(url,desire,email)==1):
                flash("Sorry can't find the products price", category="error")
            else:
                flash("You will receive an email once the product is lower than $%.2f" % desire, category="success")

    return render_template("az.html")

@views.route('/wm')
def wm():
    data = request.form 
    if request.method == 'POST':
        url = request.form.get('url')
        desire = request.form.get('desire')
        email = request.form.get('email')
        desire = float(desire.replace('$', '').replace(',', '').strip())
        if (("@" in email)==False) or (("." in email)==False):
            flash("Please enter a valid email")
        else:
            if(wmcheck(url,desire,email)==1):
                flash("Sorry can't find the products price", category="error")
            else:
                flash("You will receive an email once the product is lower than $%2f" % desire,category="success")

    return render_template("wm.html")