from PIL import Image, ImageDraw, ImageFont

class MemeGenerator():
    def __init__(self, img_path, text, author, width):
        self.img_path = img_path
        self.text = text
        self.author = author
        self.width = width

    def make_meme(img_path, text, author, width = 500):
        print(img_path)
        image = Image.open(img_path)
        names = img_path.split('.')
        for name in names:
            print(name)
        out_path = '.' + names[1] + '_meme.'+ names[2] + '.jpg'
        print(out_path)

        #if crop is not None:
        #    image = image.crop(crop)

        if width is not None:
            ratio = float(width)/float(image.size[0])
            height = int(ratio * float(image.size[1]))
            image = image.resize((width, height), Image.NEAREST)

        message = text + " -" + author
        if message is not None:
            draw = ImageDraw.Draw(image)
            #font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size = 20)
            #draw.text((10, 30), message, font=font, fill='white')
            draw.text((10, 30), message, fill='white')
            image.save(out_path)
        return out_path
