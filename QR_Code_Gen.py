# QR Code Generator

import qrcode
import qrcode.image.svg

# Version Information

qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H, box_size=16, border=4)

# Take Data To Generate QR Code

qr_data = input("\nEnter Link or Text to open when scanned, 'E.g : https://example.com/' or 'E.g : This is a Qr Code Generator'\n\n=> ")

# Extension Format

extension = int(input("\nChoose Format :\n1. SVG\n2. PNG\n3. JPG\n\n=> "))

if extension == 1:
    svg_path_fill_image = qrcode.image.svg.SvgPathFillImage
    svg_image = qrcode.make(qr_data, image_factory=svg_path_fill_image)

    # Qr Name

    qr_svg_name = input("\nEnter QR Code Name ( Default Name : QR Code ) :\n\n=> ")

    if qr_svg_name == "":
        svg_image.save("QR Code.svg")
    else:
        svg_image.save(qr_svg_name+".svg")

    print("\nYour QR Code is Generated Successfully 😊\n")

elif extension == 2:
    qr.add_data(qr_data)

    qr.make(fit=True)

    # Color Filling

    foreground_color = input("\nSelect Foreground Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default Black ) :\n\n=> ")

    background_color = input("\nSelect Background Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default White ) :\n\n=> ")

    if foreground_color == "" and background_color == "":
        image = qr.make_image(fill_color="black", back_color="white")
    elif foreground_color == "" and background_color == background_color:
        image = qr.make_image(fill_color="black", back_color=background_color)
    elif foreground_color == foreground_color and background_color == "":
        image = qr.make_image(fill_color=foreground_color, back_color="white")
    else:
        image = qr.make_image(fill_color=foreground_color, back_color=background_color)

    # Qr Name

    qr_name = input("\nEnter QR Code Name ( Default Name : QR Code ) :\n\n=> ")

    if qr_name == "":
        image.save("QR Code.png")
    else:
        image.save(qr_name+".png")

    print("\nYour QR Code is Generated Successfully 😊\n")

else:
    qr.add_data(qr_data)

    qr.make(fit=True)

    # Color Filling

    foreground_color = input("\nSelect Foreground Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default Black ) :\n\n=> ")

    background_color = input("\nSelect Background Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default White ) :\n\n=> ")

    if foreground_color == "" and background_color == "":
        image = qr.make_image(fill_color ="black", back_color="white")
    elif foreground_color == "" and background_color == background_color:
        image = qr.make_image(fill_color="black", back_color=background_color)
    elif foreground_color == foreground_color and background_color == "":
        image = qr.make_image(fill_color=foreground_color, back_color="white")
    else:
        image = qr.make_image(fill_color=foreground_color, back_color=background_color)

    # Qr Name

    qr_name = input("\nEnter QR Code Name ( Default Name : QR Code ) :\n\n=> ")

    if qr_name == "":
        image.save("QR Code.jpg")
    else:
        image.save(qr_name+".jpg")

    print("\nYour QR Code is Generated Successfully 😊\n")

