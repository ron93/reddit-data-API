from flask import Blueprint, jsonify
from . import db
from .models import Thread
main = Blueprint('main', __name__)

@main.route('/threads', methods=['GET'])
def threads():
    thread_list = Thread.query.filter(Thread.thread != "")
    reddits = []

    for th in thread_list:
        reddits.append({'thread':th.thread, 'sentiment':th.sentiment,'time':th.time })
    return jsonify({'reddits':reddits})

@main.route('/reddit/<id>/' ,methods=['GET'])
def reddit(id):
    th = Thread.query.filter(Thread.id == id)
    reddit = []
    reddit.append({'thread':th.thread, 'sentiment':th.sentiment,'time':th.time })
    return jsonify({'reddit':reddit})