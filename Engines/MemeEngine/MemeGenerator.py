from PIL import Image, ImageDraw, ImageFont

class MemeGenerator():
    def __init__(self, img_path, text, author, width):
        self.img_path = img_path
        self.text = text
        self.author = author
        self.width = width

    def make_meme(self, img_path, text, author, width = 500):
        image = Image.open(img_path)
        names = img_path.split('.')
        out_path = names[0] + '_meme.' + names[1]

        if crop is not None:
            image = image.crop(crop)

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio * float(img.size[1]))
            image = image.resize((width, height), Image.NEAREST)

        message = text + " -" + author
        if message is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size = 20)
            draw.text((10, 30), message, font=font, fill='white')
            image.save(out_path)
        return out_path
