from flask import render_template
from app import app
from app.forms import Converter

def convert(form, factor, direction, default_dir, reversed_dir):

    if form.validate_on_submit():
        unit = form.unit.data

        if direction == default_dir:
            return unit * factor
        
        elif direction == reversed_dir:
            return unit / factor
    
    return None


@app.route("/", methods=['GET', 'POST'])
@app.route("/meters-centimeters/<direction>", methods=['GET', 'POST'])
@app.route("/centimeters-meters/<direction>", methods=['GET', 'POST'])

def meters_to_centimeters(direction="meters-to-centimeters"):
    form = Converter()
    result = convert(form, 100, direction, "meters-to-centimeters", "centimeters-to-meters")

    if result is not None:
        form = Converter(formdata=None)

    return render_template('meters.html', form=form, result=result, direction=direction)   



@app.route("/feet-inches/<direction>", methods=['GET', 'POST'])
@app.route("/inches-feet/<direction>", methods=['GET', 'POST'])

def feet_to_inches(direction="feet-to-inches"):
    form = Converter()
    result = convert(form, 12, direction, "feet-to-inches", "inches-to-feet")

    if result is not None:
        form = Converter(formdata=None)

    return render_template('feet.html', form=form, result=result, direction=direction) 



@app.route("/miles-kilometers/<direction>", methods=['GET', 'POST'])
@app.route("/kilometers-miles/<direction>", methods=['GET', 'POST'])

def miles_to_kilometers(direction="miles-to-kilometers"):
    form = Converter()
    result = convert(form, 1.60934, direction, "miles-to-kilometers", "kilometers-to-miles")

    if result is not None:
        form = Converter(formdata=None)
    
    return render_template('miles.html', form=form, result=result, direction=direction)


@app.route("/fahrenheit-celsius/<direction>", methods=['GET', 'POST'])
@app.route("/celsius-fahrenheit/<direction>", methods=['GET', 'POST'])

def fahrenheit_to_celsius(direction="fahrenheit-to-celsius"):
    form = Converter()
    result = None

    if form.validate_on_submit():
        unit = form.unit.data

        if direction == "fahrenheit-to-celsius":
            result = (unit - 32) * 5/9
        
        elif direction == "celsius-to-fahrenheit":
            result = (unit * 9/5) + 32
        
    return render_template('temperature.html', form=form, result=result, direction=direction)


@app.route("/centimeters-inches/<direction>", methods=['GET', 'POST'])
@app.route("/inches-centimeters/<direction>", methods=['GET', 'POST'])

def centimeters_to_inches(direction="centimeters-to-inches"):
    form = Converter()
    result = convert(form, 1/2.54, direction, "centimeters-to-inches", "inches-to-centimeters")

    if result is not None:
        form = Converter(formdata=None)
    
    return render_template('centimeters.html', form=form, result=result, direction=direction)