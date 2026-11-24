import os
from playwright.sync_api import sync_playwright

output_dir = "D:/Shashi/Card/Version_5_Spatial_8D"
html_path = os.path.abspath(os.path.join(output_dir, "index.html"))

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 920}, device_scale_factor=2)
    page.goto(f"file:///{html_path.replace(os.sep, '/')}", wait_until="networkidle")
    page.wait_for_timeout(600)

    # 0. Welcome Overlay Screen
    page.screenshot(path=os.path.join(output_dir, "preview_v5_welcome.png"))
    print("Captured: preview_v5_welcome.png")

    # Dismiss overlay to reveal closed Mandapam card
    page.evaluate("dismissWelcomeAndPlay()")
    page.wait_for_timeout(800)

    # 1. Closed state
    page.screenshot(path=os.path.join(output_dir, "preview_v5_closed.png"))
    print("Captured: preview_v5_closed.png")

    # 2. Open Groom Wing
    page.evaluate("openGroomWing()")
    page.wait_for_timeout(1200)
    page.screenshot(path=os.path.join(output_dir, "preview_v5_groom_wing.png"))
    print("Captured: preview_v5_groom_wing.png")

    # 3. Open Bride Wing
    page.evaluate("openBrideWing()")
    page.wait_for_timeout(1200)
    page.screenshot(path=os.path.join(output_dir, "preview_v5_bride_wing.png"))
    print("Captured: preview_v5_bride_wing.png")

    # 4. Open Both Doors (Full Union)
    page.evaluate("openBothDoors()")
    page.wait_for_timeout(1500)
    page.screenshot(path=os.path.join(output_dir, "preview_v5_both_open.png"))
    print("Captured: preview_v5_both_open.png")

    browser.close()

print("All Version 5 states with Welcome Screen captured successfully!")
