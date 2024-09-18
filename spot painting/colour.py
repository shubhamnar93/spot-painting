import colorgram


class ColorExtractor:
    def __init__(self):
        self.image_path = 'spot-painting-ezgif.com-webp-to-jpg-converter.jpg'
        self.num_colors = 30
        self.rgb_colors = self.extract_colors()

    def extract_colors(self):
        colors = colorgram.extract(self.image_path, self.num_colors)
        rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
        rgb_colors = rgb_colors[4:]
        return rgb_colors
