#!/usr/bin/env python

import rospy
import json
from speedkiwi_msgs.msg import robot_status
from flask import Flask, jsonify
app = Flask(__name__)

rospy.init_node('webservice')

statuses = {}

def status_handler(data):
    """Deal with the other robot statuses, stores in an list for use later"""
    robot_id = data.robot_id
    statuses[robot_id] = {
        'type': data.robot_type,
        'x': data.x,
        'y': data.y,
        'theta': data.theta,
        'action': data.current_action,
        'isBlocked': data.is_blocked,
    }

rospy.Subscriber("statuses", robot_status, status_handler)

@app.route("/dashboard")
def dashboard():
    if statuses:
        return jsonify(statuses)
    else:
        return "Nope"

if __name__ == "__main__":
    app.run()
