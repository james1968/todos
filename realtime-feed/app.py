# ./app.py
from flask import Flask, render_template, request, jsonify
from pusher import Pusher
import uuid

# create flask app
app = Flask(__name__)


# configure pusher object
pusher = Pusher(
    app_id='526937',
    key='00e43de0549d95ef2e5f',
    secret='9f555fe422de52f88f26',
    cluster='eu',
    ssl=True
)


# index route
@app.route('/')
def index():
    return render_template('index.html')


# feed route
@app.route('/feed')
def feed():
    return render_template('feed.html')


# store post
@app.route('/post', methods=['POST'])
def addPost():
    data = {
        'id': "post-{}".format(uuid.uuid4().hex),
        'title': request.form.get('title'),
        'content': request.form.get('content'),
        'status': 'active',
        'event_name': 'created'
    }
    pusher.trigger("blog", "post-added", data)
    return jsonify(data)


# deactivate or delete post
@app.route('/post/<id>', methods=['PUT', 'DELETE'])
def updatePost(id):
    data = {'id': id}
    if request.method == 'DELETE':
        data['event_name'] = 'deleted'
        pusher.trigger("blog", "post-deleted", data)
    else:
        data['event_name'] = 'deactivated'
        pusher.trigger("blog", "post-deactivated", data)
    return jsonify(data)

# run flask app in debug mode
app.run(debug=True)
