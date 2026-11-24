import urllib.request
import re

uas = {
    'googlebot': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'bingbot': 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'twitterbot': 'Twitterbot/1.0',
    'facebookexternalhit': 'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)',
    'whatsapp': 'WhatsApp/2.21.12.21 A',
    'mobile_chrome': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}

for name, ua in uas.items():
    req = urllib.request.Request('https://www.instagram.com/alanaatii/', headers={'User-Agent': ua})
    try:
        with urllib.request.urlopen(req) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
            meta_desc = re.findall(r'<meta [^>]*name=[\"\']description[\"\'][^>]*content=[\"\'](.*?)[\"\']', text, re.I)
            og_title = re.findall(r'<meta [^>]*property=[\"\']og:title[\"\'][^>]*content=[\"\'](.*?)[\"\']', text, re.I)
            og_desc = re.findall(r'<meta [^>]*property=[\"\']og:description[\"\'][^>]*content=[\"\'](.*?)[\"\']', text, re.I)
            print(f"[{name}] status={resp.status} meta_desc={meta_desc} og_title={og_title} og_desc={og_desc}")
    except Exception as e:
        print(f"[{name}] error: {e}")
