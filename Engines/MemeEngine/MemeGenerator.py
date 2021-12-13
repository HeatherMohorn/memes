from PIL import Image, ImageDraw, ImageFont

class MemeGenerator():
    def __init__(self, img_path, text, author, width):
        self.img_path = img_path
        self.text = text
        self.author = author
        self.width = width

    def make_meme(img_path, text, author, width = 500):
        image = Image.open(img_path)
        names = text.split(' ')
        out_path = 'static/' + names[-1] + '_meme.jpg'

        if width is not None:
            ratio = float(width)/float(image.size[0])
            height = int(ratio * float(image.size[1]))
            image = image.resize((width, height), Image.NEAREST)

        message = text + " -" + author
        if message is not None:
            draw = ImageDraw.Draw(image)
            #font = ImageFont.truetype('./fonts/OpenSans-Regular.ttf', size = 20)
            #draw.text((10, 30), message, font=font, fill='white')
            draw.text((10, 30), message)
            image.save(out_path)
        return out_path
