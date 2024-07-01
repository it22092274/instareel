from flask import Flask, render_template, request, send_file
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import requests
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
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)
        wait = WebDriverWait(driver, 20)
        form = wait.until(EC.presence_of_element_located((By.NAME, "formurl")))

        input_field = driver.find_element(By.NAME, "url")
        input_field.send_keys(reel_url)

        submit_button = driver.find_element(By.ID, "btn-submit")
        submit_button.click()

        download_section = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "download-content")))

        download_link = download_section.find_element(By.CLASS_NAME, "download-media").get_attribute("href")
        return download_link
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        driver.quit()

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
