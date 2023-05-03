import requests
import urllib.request
from PIL import Image, ImageDraw, ImageFont
import json
import os


def get_quote():
    # make the API request
    response = requests.get('https://api.quotable.io/quotes/random?maxLength=50')

    # check if the request was successful
    if response.status_code == 200:

        data = json.loads(response.content)
        if isinstance(data, list) and len(data) > 0:
            quote = data[0]['content']
            author = data[0]['author']

            # print the quote on the screen
            print(f'"{quote}" - {author}')
            return quote, author
        else:
            print('Error: empty response')
            return None
    else:
        print('Error making request')
        # extract the quote from the response
    
def get_image():    
    url = "https://picsum.photos/800" # The URL of the image you want to download
    filename = "my_image.jpg" # The name you want to save the image as

    response = requests.get(url) # Send a GET request to the URL

    with open(filename, "wb") as f:
        f.write(response.content) # Write the content of the response to a file

    print("Image saved as", filename) # Print a confirmation message

def create_image_with_quote():
    quote, author = get_quote()
    img = Image.open("my_image.jpg") #Open the image
    drawing = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("ebrima.ttf",35)
    drawing.text((60,80),f'"{quote}" \n- {author}', font=fnt, fill=(255,255,255) ,  stroke_width=5, stroke_fill='black') #Write the quote and author
    img.save("quoteImage.png") #Save new image

def erase_duplicate_image():
    file_path = "./my_image.jpg"
    try:
        os.remove(file_path)
        print(f"{file_path} has been deleted successfully")
    except OSError as e:
        print(f"Error: {file_path} could not be deleted. {e}")

if __name__ == "__main__":
    get_image()
    create_image_with_quote()
    erase_duplicate_image()

print("File created successfully")


