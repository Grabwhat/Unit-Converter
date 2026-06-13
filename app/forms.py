from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class Converter(FlaskForm):
    unit = FloatField("Enter Units Here", render_kw={"class": "unit-input"}, validators=[
        InputRequired(), 
        NumberRange(min=0, message="Only postive numbers are accepted")
    ])
    submit = SubmitField("Convert", render_kw={"class": "submit-btn"})