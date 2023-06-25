from flask import Flask, render_template
import pygame
from queue import Queue

app = Flask(__name__)
request_queue = Queue()

pygame.mixer.init()

@app.route('/')
def index():
    return render_template('dashboard.html', requests=request_queue.queue)

@app.post('/incoming')
def handle_incoming_request():
    # Process the incoming request
    # ...
    # Add the request to the queue
    request_queue.put(request.json)
    play_beep_sound()
    return 'Request received'

def play_beep_sound():
    pygame.mixer.music.load('/home/kali/workshop/browser-notification/static/notification-sound.mp3')
    pygame.mixer.music.play()

if __name__ == '__main__':
    app.run()
