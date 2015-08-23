#!/usr/bin/env python

import rospy
import json
from speedkiwi_msgs.msg import robot_status, bin_status
from flask import Flask, jsonify
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
        'isBlocked': data.is_blocked,
    }

rospy.Subscriber("statuses", robot_status, robot_status_handler)

robot_statuses = {}

def bin_status_handler(data):
    """Deal with the other robot statuses, stores in an list for use later"""
    bin_id = data.bin_id
    bin_statuses[bin_id] = {
        'x': data.x,
        'y': data.y
    }

rospy.Subscriber("bin_status_topic", bin_status, bin_status_handler)

bin_statuses = {}

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

if __name__ == "__main__":
    app.run(port=1337)
