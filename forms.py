from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional

class AddCupcakeForm(FlaskForm):
    """Form for adding new cupcake"""

    flavor = StringField("Flavor*", validators=[InputRequired(message="Flavor is required")])
    size = SelectField("Size*", choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')], validators=[InputRequired(message="Size is required")])
    rating = SelectField("Rating*", choices=[('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')], validators=[InputRequired(message="Rating is required")])
    image = StringField("Image URL", validators=[Optional()])
    