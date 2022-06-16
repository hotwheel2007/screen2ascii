def convert(image, image_load):
    ascii_img = []
    for h in range(0, image.height):
        row = ""
        for w in range(0, image.width):
            px = image_load[w, h]
            if px >= 225:
                row += "@@"
            elif px >= 200:
                row += "%%"
            elif px >= 175:
                row += "##"
            elif px >= 150:
                row += "**"
            elif px >= 125:
                row += "++"
            elif px >= 100:
                row += "=="
            elif px >= 75:
                row += "--"
            elif px >= 50:
                row += "::"
            elif px >= 25:
                row += ".."
            elif px >= 0:
                row += "  "

        ascii_img.append(row)

    return(ascii_img)