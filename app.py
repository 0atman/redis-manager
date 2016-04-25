import os, redis_helper, json
from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template(
        'index.html',
        lists=redis_helper.get_all_lists_with_items()
    )

@app.route('/get_lists')
def get_lists():
    return jsonify(
        keys=redis_helper.get_lists()
    )

@app.route('/get_list_items/<list>')
def get_list_items(list):
    return jsonify(
        messages=redis_helper.get_list_items(list)
    )

@app.route('/get_all_lists_with_items')
def get_all_lists_with_items():
    return jsonify(
        lists=redis_helper.get_all_lists_with_items()
    )

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
