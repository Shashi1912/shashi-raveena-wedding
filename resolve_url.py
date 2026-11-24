import urllib.request

url = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFifu8Qr63ZX2JS0Mi0IyB7KetQAtytA8yRqTt22UNPfPZsdlztsJYPqjy2coKE5o_eUuMNW6DODEbB6YmEF5sd7R_GkVuYHC34X_2iT0vFV3PSiRJLUGdfE6QLmgRLKg=="
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        print("Final URL:", resp.geturl())
except Exception as e:
    print("Error:", e)
