#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageDraw

def make_image(screen, bgcolor, filename):
    """
     画像の作成
    """
    img = Image.new('RGB', screen,bgcolor)
    #
    #ここに、いろいろな処理を追加する
    draw = ImageDraw.Draw(img)
    draw.ellipse((20,20,204,204), outline=(225, 225, 225), fill=(255, 255, 255))
    del draw
    img.save("./result/mask_cir01.jpg")
    img.save("./result/mask_cir.png")
    #
    #img.save(filename)
    return

def main():
    # 画像のサイズ
    screen = (224,224)

    # 画像の背景色（RGB）
    bgcolor=(0,0,0)

    # 保存するファイル名（ファイル形式は、拡張子から自動的に判別する）
    filename = "mask-01.jpg"
    make_image(screen, bgcolor, filename)

if __name__ == '__main__':
    main()
