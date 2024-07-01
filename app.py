from flask import Flask, render_template, request, send_file
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    reel_url = request.form['url']
    download_link = get_download_link(reel_url)
    if download_link:
        video_path = download_video(download_link)
        return send_file(video_path, as_attachment=True)
    else:
        return "Failed to download the video."

def get_download_link(reel_url):
    url = 'https://snapinsta.app/instagram-reels-video-download'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # You will need to inspect the page to find the correct form field names and other details.
    # This is an example and may not work as-is without proper inspection.
    form = soup.find('form', {'name': 'formurl'})
    input_field = form.find('input', {'name': 'url'})
    input_field['value'] = reel_url

    form_action = form['action']
    form_response = requests.post(form_action, data={input_field['name']: input_field['value']})
    form_soup = BeautifulSoup(form_response.content, 'html.parser')
    
    # Again, inspect the page to find the correct class names or IDs.
    download_section = form_soup.find('div', {'class': 'download-content'})
    download_link = download_section.find('a', {'class': 'download-media'})['href']

    return download_link

def download_video(download_link):
    folder_path = 'reels'
    os.makedirs(folder_path, exist_ok=True)

    video_response = requests.get(download_link)
    video_name = os.path.join(folder_path, 'downloaded_video.mp4')

    with open(video_name, 'wb') as video_file:
        video_file.write(video_response.content)

    return video_name

if __name__ == '__main__':
    app.run(debug=True)
