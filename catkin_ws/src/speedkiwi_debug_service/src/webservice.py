#!/usr/bin/env python

import rospy
from json import dumps
from rosgraph_msgs.msg import Log
from speedkiwi_msgs.msg import robot_status, bin_status
from flask import Flask, jsonify, make_response

app = Flask(__name__, static_folder='static', static_url_path='')

rospy.init_node('webservice')

robot_statuses = {}


def robot_status_handler(data):
    """Deal with the other robot statuses, stores in an list for use later"""
    robot_id = data.robot_id
    robot_statuses[robot_id] = {
        'type': data.robot_type,
        'x': data.x,
        'y': data.y,
        'theta': data.theta,
        'action': data.current_action,
        'isBlocked': data.is_blocked
    }

rospy.Subscriber("statuses", robot_status, robot_status_handler)

robot_statuses = {}


def bin_status_handler(data):
    """Deal with the other robot statuses, stores in an list for use later"""
    bin_id = data.bin_id
    bin_statuses[bin_id] = {
        'x': data.x,
        'y': data.y,
        'isCarried': data.is_carried,
        'isEmpty': data.is_empty
    }

rospy.Subscriber("bin_status_topic", bin_status, bin_status_handler)

bin_statuses = {}


def log_handler(data):
    level = ''

    if data.level == data.DEBUG:
        level = 'DEBUG'
    elif data.level == data.INFO:
        level = 'INFO'
    elif data.level == data.WARN:
        level = 'WARNING'
    elif data.level == data.ERROR:
        level = 'ERROR'
    elif data.level == data.FATAL:
        level = 'FATAL'
    else:
        level = 'WTF'

    messages.append({
        'level': level,
        'node': data.name,
        'message': data.msg,
        'source': {
            'file': data.file,
            'function': data.function,
            'line': data.line
        }
    })

    if len(messages) > 1000:
        messages.pop(0)

messages = []

rospy.Subscriber('rosout_agg', Log, log_handler)

ROS_ERROR = {
    'status': 'error',
    'message': 'Not recieving data from ROS'
}


@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route("/robots")
def robots():
    if robot_statuses:
        return jsonify(robot_statuses)
    else:
        return jsonify(ROS_ERROR)


@app.route("/robots/<robot_id>")
def robot(robot_id):
    if robot_statuses and robot_id in robot_statuses:
        return jsonify(robot_statuses[robot_id])
    else:
        return jsonify(ROS_ERROR)


@app.route("/bins")
def bins():
    if bin_statuses:
        return jsonify(bin_statuses)
    else:
        return jsonify(ROS_ERROR)


@app.route("/bins/<bin_id>")
def bin(bin_id):
    if bin_statuses and bin_id in bin_statuses:
        return jsonify(bin_statuses[bin_id])
    else:
        return jsonify(ROS_ERROR)


@app.route("/log")
def log():
    if messages:
        res = make_response(dumps(messages))
        res.headers['Content-Type'] = 'application/json'
        return res
    else:
        return jsonify(ROS_ERROR)

if __name__ == "__main__":
    app.run(port=1337)
