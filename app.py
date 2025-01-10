from flask import Flask, render_template, request, redirect, url_for, flash
from pytube import YouTube
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

def download_video(video_url, download_path):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(download_path)
        return yt.title  # Return the title of the downloaded video
    except Exception as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        download_path = os.getcwd()  # Set download path to current directory
        
        if not video_url:
            flash('Please enter a valid YouTube URL.')
            return redirect(url_for('index'))

        title = download_video(video_url, download_path)
        flash(f'Downloaded: {title}')
        return redirect(url_for('result', title=title))

    return render_template('index.html')

@app.route('/result')
def result():
    title = request.args.get('title')
    return render_template('result.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)
