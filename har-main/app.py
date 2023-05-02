from flask import  Flask, request, jsonify, render_template, Response, current_app
import os
from collections import deque
import numpy as np
import cv2
import json
import time

import gdown

# Specify the Google Drive file ID and output file name
file_id = '1VHl2W04ZuSkCKwKywAlDWiZRw-RANEZ0'
output_file = 'model/resnet-34_kinetics.onnx'

# # Download the file from Google Drive
url = f'https://drive.google.com/uc?id={file_id}'
gdown.download(url, output_file, quiet=False)

# Load the file into your Streamlit Cloud application
# self.ACTION_RESNET = output_file

app = Flask(__name__)

# https://drive.google.com/file/d/1VHl2W04ZuSkCKwKywAlDWiZRw-RANEZ0/view?usp=share_link

class Parameters:
    def __init__(self):
        self.CLASSES = open("model/action_recognition_kinetics.txt").read().strip().split("\n")
        # self.ACTION_RESNET = 'model/resnet-34_kinetics.onnx'
        self.ACTION_RESNET = output_file
        self.SAMPLE_DURATION = 16
        self.SAMPLE_SIZE = 112

param = Parameters()

captures = deque(maxlen=param.SAMPLE_DURATION)

print("[INFO] loading human activity recognition model...")
net = cv2.dnn.readNet(model=param.ACTION_RESNET)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    form_data = request.form
    org_name = form_data['originalname']
    path = os.getcwd()
    if file:
        file.save(os.path.join(path, 'videos', org_name))
        vs = cv2.VideoCapture(os.path.join(path, 'videos', org_name))

        label = ''
        labels = []
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= 10:
                print("Time's up! Exiting loop.")
                break
            (grabbed, capture) = vs.read()
            if not grabbed:
                vs.release()
                break
            capture = cv2.resize(capture, dsize=(550, 400))
            captures.append(capture)
            if len(captures) < param.SAMPLE_DURATION:
                continue
            imageBlob = cv2.dnn.blobFromImages(captures, 1.0,(param.SAMPLE_SIZE,param.SAMPLE_SIZE),(114.7748, 107.7354, 99.4750),swapRB=True, crop=True)
            imageBlob = np.transpose(imageBlob, (1, 0, 2, 3))
            imageBlob = np.expand_dims(imageBlob, axis=0)
            net.setInput(imageBlob)
            outputs = net.forward()
            label = param.CLASSES[np.argmax(outputs)]
            labels.append(label)
            print(label)
                # with app.app_context():
                #     print("Hello")
                #     json_str = json.dumps({'label': label})
                #     yield json_str.encode('utf-8')  # Update to use json_str.encode('utf-8')
    
        # vs.release()
        return label
        # return app.response_class(generate(), mimetype='application/json', direct_passthrough=True)

        # return jsonify({'labels': labels})
    else:
        return 'Error uploading file'

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
