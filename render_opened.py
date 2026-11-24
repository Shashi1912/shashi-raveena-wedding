import os
import subprocess

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_path = r'D:\Shashi\Card\Unique_Wedding_Invitations\concept3_mandapam_gatefold.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

opened_content = content.replace('class="mandapam-stage" id="mandapamStage"', 'class="mandapam-stage opened" id="mandapamStage"')
temp_path = r'D:\Shashi\Card\Unique_Wedding_Invitations\temp_opened.html'
with open(temp_path, 'w', encoding='utf-8') as f:
    f.write(opened_content)

out_png = r'D:\Shashi\Card\Unique_Wedding_Invitations\preview_concept3_opened.png'
cmd = [
    chrome_path,
    '--headless',
    '--disable-gpu',
    '--hide-scrollbars',
    '--window-size=1050,850',
    f'--screenshot={out_png}',
    temp_path
]
subprocess.run(cmd, check=True)

if os.path.exists(temp_path):
    os.remove(temp_path)

print('Rendered opened preview for Concept 3!')
