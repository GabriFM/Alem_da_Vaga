from vagasdeestacionamento import app
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import cv2
import numpy as np
import os
import threading
from vagasdeestacionamento.routes import estacionamento, socketio



def camera_thread():
    estacionamento.run()

if __name__ == "__main__":
    # Inicie a thread da câmera
    thread = threading.Thread(target=camera_thread)
    thread.daemon = True
    thread.start()

    # Inicie o servidor Flask e o SocketIO
    socketio.run(app, debug=True, use_reloader=False)





