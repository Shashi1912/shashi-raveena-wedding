import re
import json
import urllib.request
import xml.etree.ElementTree as ET

targets = ['qPS0yLEwG3U', 'DMmbbweYGKY', 'aosKebQY4uw', 'w49tXp-S2zk', 'm-Br8HPka0o', 'FG4edQ5P4UM']

for vid in targets:
    with open(f'yt_{vid}.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract description from initial player response
    desc_match = re.search(r'\"shortDescription\":\"(.*?)\"', html)
    desc = desc_match.group(1).encode('utf-8').decode('unicode_escape', 'ignore') if desc_match else ""
    
    # Extract captions
    captions_match = re.search(r'\"captionTracks\":(\[.*?\])', html)
    transcript_text = ""
    if captions_match:
        try:
            tracks = json.loads(captions_match.group(1))
            if tracks:
                baseUrl = tracks[0].get('baseUrl')
                # fetch caption xml
                req = urllib.request.Request(baseUrl, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as resp:
                    c_xml = resp.read().decode('utf-8', errors='ignore')
                    root = ET.fromstring(c_xml)
                    lines = [elem.text for elem in root.findall('.//text') if elem.text]
                    transcript_text = " ".join(lines)
        except Exception as e:
            transcript_text = f"Error fetching captions: {e}"
            
    print(f"\n================ Video: {vid} ================")
    print("Description:", desc)
    print("Transcript:", transcript_text[:500])
