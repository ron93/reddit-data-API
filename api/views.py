from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/reddits', methods=['GET'])
def reddits():
    reddits = []
    return jsonify({'reddits':reddits})
'''
@main.route('/reddit/<id>/' ,methods=['GET'])
def reddit(id):
    reddit = []
    return jsonify({'reddit':reddit})'''