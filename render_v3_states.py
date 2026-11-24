import os
from playwright.sync_api import sync_playwright

output_dir = "D:/Shashi/Card/Version_3_Door_Touch"
html_path = os.path.abspath(os.path.join(output_dir, "index.html"))

with sync_playwright() as p:
    browser = p.chromium.launch()
    # High-DPI viewport matching luxury gatefold aspect ratio
    page = browser.new_page(viewport={"width": 1280, "height": 920}, device_scale_factor=2)
    page.goto(f"file:///{html_path.replace(os.sep, '/')}", wait_until="networkidle")
    page.wait_for_timeout(1000)

    # 1. Closed state
    page.screenshot(path=os.path.join(output_dir, "preview_v3_closed.png"))
    print("Captured: preview_v3_closed.png")

    # 2. Open Groom Wing
    page.evaluate("openGroomWing()")
    page.wait_for_timeout(1200)
    page.screenshot(path=os.path.join(output_dir, "preview_v3_groom_wing.png"))
    print("Captured: preview_v3_groom_wing.png")

    # 3. Open Bride Wing
    page.evaluate("openBrideWing()")
    page.wait_for_timeout(1200)
    page.screenshot(path=os.path.join(output_dir, "preview_v3_bride_wing.png"))
    print("Captured: preview_v3_bride_wing.png")

    # 4. Open Both Doors (Full Union)
    page.evaluate("openBothDoors()")
    page.wait_for_timeout(1500)
    page.screenshot(path=os.path.join(output_dir, "preview_v3_both_open.png"))
    print("Captured: preview_v3_both_open.png")

    browser.close()

print("All Version 3 states captured successfully!")
