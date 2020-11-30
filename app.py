"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template, redirect
from forms import AddCupcakeForm
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


@app.route('/', methods=["GET", "Post"])
def home_page():
    form = AddCupcakeForm()
    cupcakes = Cupcake.query.all()

    if form.validate_on_submit():
        flavor = form.flavor.data.capitalize()

        size = form.size.data
        rating = form.rating.data

        try:
            image = form.image.data
        except:
            image = 'https://tinyurl.com/demo-cupcake'

        new_cupcake = Cupcake(flavor=flavor, size=size,
                              rating=rating, image=image)
        db.session.add(new_cupcake)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('index.html', form=form, cupcakes=cupcakes)


@app.route('/api/cupcakes')
def get_all_cupcakes():
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route('/api/cupcakes/<id>')
def get_a_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']

    try:
        image = request.json['image']
    except:
        image = 'https://tinyurl.com/demo-cupcake'

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    response_json = jsonify(new_cupcake.serialize())

    return (response_json, 201)


@app.route('/api/cupcakes/<id>', methods=['PATCH'])
def patch_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<id>', methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")
