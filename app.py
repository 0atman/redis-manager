import os, redis_helper, json
from flask import Flask, jsonify, request
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

@app.route('/action_messages', methods = ['POST'])
def action_messages():
    response_data = request.json
    action = response_data['action']
    move_messages_to = response_data['move_messages_to']
    messages_to_move = response_data['messages_to_move']
    for queue in messages_to_move:
        for message in queue['messages']:
            queue_name = queue['name']
            if action == 'delete':
                redis_helper.delete_message_from_list(queue_name, message)
            elif 'lpush':
                redis_helper.delete_message_from_list(queue_name, message)
                redis_helper.lpush_message(move_messages_to, message)
            elif 'rpush':
                redis_helper.delete_message_from_list(queue_name, message)
                redis_helper.rpush_message(move_messages_to, message)
    return 'Action complete'


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
