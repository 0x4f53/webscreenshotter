from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time, os, traceback

from PIL import Image

def take_screenshot (url, height, width, directory=".", file_suffix="screenshot_", stitch=True):
    saved_file_names = []
    try:  
        if not os.path.exists(directory): 
            os.mkdir(directory)
            print (f"Created {os.path.abspath(directory)}")
        else: 
            print (f"{os.path.abspath(directory)} already exists. Overwriting it...")
        
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        print (f"Fetching screenshots from {url}")

        driver.get(url)
        time.sleep(2)

        total_height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")

        driver.set_window_size(width, height)

        current_scroll = 0
        chunk_number = 1

        while current_scroll < total_height:
            driver.execute_script(f"window.scrollTo(0, {current_scroll});")
            time.sleep(1)
            
            save_file = f"{directory}/{file_suffix}{chunk_number}.png"
            
            driver.save_screenshot(save_file)
            saved_file_names.append(save_file)
            
            current_scroll += height
            chunk_number += 1
        
        if stitch:
            opened_images = [Image.open(image) for image in saved_file_names]
            max_width = max(img.width for img in opened_images)
            total_height = sum(img.height for img in opened_images)
            stitched_image = Image.new('RGB', (max_width, total_height))
            current_height = 0
            for img in opened_images:
                stitched_image.paste(img, (0, current_height))
                current_height += img.height            
            stitched_image.save(f"{directory}/{file_suffix}stitched.png")

        print(f"The following files were saved at: {os.path.abspath(directory)}")
        for file_name in saved_file_names: print (f" - {file_name}")
        if stitch: print (f"A stitched version was saved at {directory}/{file_suffix}stitched.png")

    except:
        print ("An error occurred:")
        traceback.print_exc()

    finally: driver.quit()

