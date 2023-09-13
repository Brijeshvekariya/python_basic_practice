import qrcode

img = qrcode.make("https://github.com/Brijeshvekariya")

img.save("github.png")