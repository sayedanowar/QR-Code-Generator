
import qrcode
from PIL import Image

# QR Code Type

qr_types = ["\nChoose QR Code Type :", "1. Facebook", "2. WhatsApp", "3. Instagram", "4. Twitter", "5. YouTube", "6. URL", "7. Text"]

for type in qr_types:
    print(type)

qr_data = int(input("\n>> "))

qr = qrcode.QRCode(version=1,
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=16,
        border=4)

if qr_data == 1:
    fb_img = './Icons/FB.png'
    fb_logo = Image.open(fb_img)

    basewidth = 100     # BaseWidth

    # Adjust Image Size

    wpercent = (basewidth/float(fb_logo.size[0]))
    hsize = int((float(fb_logo.size[1])*float(wpercent)))
    fb_logo = fb_logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)

    fb_url = input("\nFacebook Profile/Page Link :\n\n>> ")     # Taking Facebook Link

    if fb_url.startswith("https://www.facebook.com/") or fb_url.startswith("https://facebook.com/"):

        qr.add_data(fb_url)    # Adding Data to QR Code
        qr.make()   # Creating QR Code

        # Taking Color From User

        foreground_color = input("\nSelect Foreground Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default Black ) :\n\n>> ")
        background_color = input("\nSelect Background Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default White ) :\n\n>> ")

        if foreground_color == "" and background_color == "":
            qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        elif foreground_color == "" and background_color == background_color:
            qr_image = qr.make_image(fill_color="black", back_color=background_color).convert('RGB')
        elif foreground_color == foreground_color and background_color == "":
            qr_image = qr.make_image(fill_color=foreground_color, back_color="white").convert('RGB')
        else:
            qr_image = qr.make_image(fill_color=foreground_color, back_color=background_color).convert('RGB')

        # Size of QR code

        pos = ((qr_image.size[0] - fb_logo.size[0]) // 2,
            (qr_image.size[1] - fb_logo.size[1]) // 2)
        qr_image.paste(fb_logo, pos)

        # Taking QR Code Name From User

        qr_name = input("\nEnter QR Code Name ( By Default : Facebook ) :\n\n>> ")

        if qr_name == "":
            qr_image.save("Facebook.png")   # Save The Generated QR Code
        else:
            qr_image.save(qr_name+".png")

        print("\nYour QR Code is Generated Successfully 😊\n")
    else:
        print("\nInput Facebook Link Only\n")

elif qr_data == 2:
    wa_img = './Icons/WA.png'
    wa_logo = Image.open(wa_img)

    basewidth = 100     # BaseWidth

    # Adjust Image Size

    wpercent = (basewidth/float(wa_logo.size[0]))
    hsize = int((float(wa_logo.size[1])*float(wpercent)))
    wa_logo = wa_logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)

    # Taking Country, Whatsapp Number & Message

    print('''\nINSTRUCTION :\nEnter Your Number With Country Code. Omit any Zeroes, Brackets, Dashes or '+' Sign When Adding the PHONE NUMBER.''')
    print("Example :\nUse : 1XXXXXXXXXX\nDon't Use : +001-(XXX)XXXXXXX")
    print("\nIf India Don't Need Country Code Just Enter Your Number.\n")

    country = int(input("Choose Country :\n1. India\n2. Others\n\n>> "))

    if country == 1:
        wa_num = input("\nJust Enter Your Number :\n\n>> ")
        wa_msg = input("\nText Message ( Default : HI ):\n\n>> ")
        if wa_msg == "":
            wa_data = f"https://wa.me/91{wa_num}?text=Hi"
        else:
            wa_data = f"https://wa.me/91{wa_num}?text={wa_msg}"
            if wa_msg.find(" "):
                wa_msg.replace(" ", "%20")
        qr.add_data(wa_data)    # Adding Data to QR Code
        qr.make()   # Generating QR Code
    else:
        wa_num = input("\nEnter Your Number With Country Code and Omit '+' Sign :\n\n>> ")
        wa_msg = input("\nText Message ( Default : HI ):\n\n>> ")
        if wa_msg == "":
            wa_data = f"https://wa.me/{wa_num}?text=Hi"
        else:
            wa_data = f"https://wa.me/{wa_num}?text={wa_msg}"
            if wa_msg.find(" "):
                wa_msg.replace(" ", "%20")
        qr.add_data(wa_data)    # Adding Data to QR Code
        qr.make()   # Generating QR Code

    # Taking Color From User

    foreground_color = input("\nSelect Foreground Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default Black ) :\n\n>> ")
    background_color = input("\nSelect Background Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default White ) :\n\n>> ")

    if foreground_color == "" and background_color == "":
        qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    elif foreground_color == "" and background_color == background_color:
        qr_image = qr.make_image(fill_color="black", back_color=background_color).convert('RGB')
    elif foreground_color == foreground_color and background_color == "":
        qr_image = qr.make_image(fill_color=foreground_color, back_color="white").convert('RGB')
    else:
        qr_image = qr.make_image(fill_color=foreground_color, back_color=background_color).convert('RGB')
    
    # Size of QR code

    pos = ((qr_image.size[0] - wa_logo.size[0]) // 2,
        (qr_image.size[1] - wa_logo.size[1]) // 2)
    qr_image.paste(wa_logo, pos)

    # Taking QR Code Name from User

    qr_name = input("\nEnter QR Code Name ( By Default : WhatsApp ) :\n\n>> ")

    if qr_name == "":
        qr_image.save("WhatsApp.png")   # Save The Generated QR Code
    else:
        qr_image.save(qr_name+".png")

    print("\nYour QR Code is Generated Successfully 😊\n")

elif qr_data == 3:
    ig_img = './Icons/IG.png'
    ig_logo = Image.open(ig_img)

    basewidth = 100     # BaseWidth

    # Adjust Image Size

    wpercent = (basewidth/float(ig_logo.size[0]))
    hsize = int((float(ig_logo.size[1])*float(wpercent)))
    ig_logo = ig_logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)

    ig_usrname = input("\nInstagram Username :\n\n>> ")     # Taking Instagram Username

    qr.add_data("https://www.instagram.com/"+ig_usrname)    # Adding Data to QR Code

    qr.make()   # Generating QR Code

    # Taking Color From User

    foreground_color = input("\nSelect Foreground Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default Black ) :\n\n>> ")
    background_color = input("\nSelect Background Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default White ) :\n\n>> ")

    if foreground_color == "" and background_color == "":
        qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    elif foreground_color == "" and background_color == background_color:
        qr_image = qr.make_image(fill_color="black", back_color=background_color).convert('RGB')
    elif foreground_color == foreground_color and background_color == "":
        qr_image = qr.make_image(fill_color=foreground_color, back_color="white").convert('RGB')
    else:
        qr_image = qr.make_image(fill_color=foreground_color, back_color=background_color).convert('RGB')
    
    # Size of QR code

    pos = ((qr_image.size[0] - ig_logo.size[0]) // 2,
        (qr_image.size[1] - ig_logo.size[1]) // 2)
    qr_image.paste(ig_logo, pos)

    # Taking QR Code Name from User

    qr_name = input("\nEnter QR Code Name ( By Default : Instagram ) :\n\n>> ")

    if qr_name == "":
        qr_image.save("Instagram.png")  # Save The Generated QR Code
    else:
        qr_image.save(qr_name+".png")

    print("\nYour QR Code is Generated Successfully 😊\n")

elif qr_data == 4:
    tw_img = './Icons/TW.png'
    tw_logo = Image.open(tw_img)

    basewidth = 100     # BaseWidth

    # Adjust Image Size

    wpercent = (basewidth/float(tw_logo.size[0]))
    hsize = int((float(tw_logo.size[1])*float(wpercent)))
    tw_logo = tw_logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)

    tw_handle = input("\nTwitter Handle :\n\n>> ")  # Taking Twitter Username

    qr.add_data("https://twitter.com/"+tw_handle)   # Adding Data to QR Code

    qr.make()   # Generating QR Code

    # Taking Color From User

    foreground_color = input("\nSelect Foreground Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default Black ) :\n\n>> ")
    background_color = input("\nSelect Background Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default White ) :\n\n>> ")

    if foreground_color == "" and background_color == "":
        qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    elif foreground_color == "" and background_color == background_color:
        qr_image = qr.make_image(fill_color="black", back_color=background_color).convert('RGB')
    elif foreground_color == foreground_color and background_color == "":
        qr_image = qr.make_image(fill_color=foreground_color, back_color="white").convert('RGB')
    else:
        qr_image = qr.make_image(fill_color=foreground_color, back_color=background_color).convert('RGB')
    
    # Size of QR code

    pos = ((qr_image.size[0] - tw_logo.size[0]) // 2,
        (qr_image.size[1] - tw_logo.size[1]) // 2)
    qr_image.paste(tw_logo, pos)

    # Taking QR Code Name from User

    qr_name = input("\nEnter QR Code Name ( By Default : Twitter ) :\n\n>> ")

    if qr_name == "":
        qr_image.save("Twitter.png")    # Save The Generated QR Code
    else:
        qr_image.save(qr_name+".png")

    print("\nYour QR Code is Generated Successfully 😊\n")

elif qr_data == 5:
    yt_img = './Icons/YT.png'
    yt_logo = Image.open(yt_img)

    basewidth = 100     # BaseWidth

    # Adjust Image Size

    wpercent = (basewidth/float(yt_logo.size[0]))
    hsize = int((float(yt_logo.size[1])*float(wpercent)))
    yt_logo = yt_logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)

    yt_link = input("\nYoutube Video/Channel Link :\n\n>> ")    # Taking YouTube Link

    if yt_link.startswith("https://www.youtube.com/") or yt_link.startswith("https://youtu.be/"):

        qr.add_data(yt_link)    # Adding Data to QR Code
        qr.make()    # Creating QR Code

        # Taking Color From User

        foreground_color = input("\nSelect Foreground Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default Black ) :\n\n>> ")
        background_color = input("\nSelect Background Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default White ) :\n\n>> ")

        if foreground_color == "" and background_color == "":
            qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        elif foreground_color == "" and background_color == background_color:
            qr_image = qr.make_image(fill_color="black", back_color=background_color).convert('RGB')
        elif foreground_color == foreground_color and background_color == "":
            qr_image = qr.make_image(fill_color=foreground_color, back_color="white").convert('RGB')
        else:
            qr_image = qr.make_image(fill_color=foreground_color, back_color=background_color).convert('RGB')

        # Size of QR code

        pos = ((qr_image.size[0] - yt_logo.size[0]) // 2,
            (qr_image.size[1] - yt_logo.size[1]) // 2)
        qr_image.paste(yt_logo, pos)

        # Taking QR Code Name from User

        qr_name = input("\nEnter QR Code Name ( By Default : YouTube ) :\n\n>> ")

        if qr_name == "":
            qr_image.save("YouTube.png")    # Save The Generated QR Code
        else:
            qr_image.save(qr_name+".png")

        print("\nYour QR Code is Generated Successfully 😊\n")
    else:
        print("\nInput Youtube Link Only\n")

elif qr_data == 6:
    link_img = './Icons/LINK.png'
    link_logo = Image.open(link_img)

    basewidth = 100     # BaseWidth

    # Adjust Image Size

    wpercent = (basewidth/float(link_logo.size[0]))
    hsize = int((float(link_logo.size[1])*float(wpercent)))
    link_logo = link_logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)

    link = input("\nEnter URL :\n\n>> ")    # Taking Link Data

    if link.startswith("https://"):

        qr.add_data(link)    # Adding Data to QR Code
        qr.make()    # Creating QR Code

        # Taking Color From User

        foreground_color = input("\nSelect Foreground Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default Black ) :\n\n>> ")
        background_color = input("\nSelect Background Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default White ) :\n\n>> ")

        if foreground_color == "" and background_color == "":
            qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        elif foreground_color == "" and background_color == background_color:
            qr_image = qr.make_image(fill_color="black", back_color=background_color).convert('RGB')
        elif foreground_color == foreground_color and background_color == "":
            qr_image = qr.make_image(fill_color=foreground_color, back_color="white").convert('RGB')
        else:
            qr_image = qr.make_image(fill_color=foreground_color, back_color=background_color).convert('RGB')

        # Size of QR code

        pos = ((qr_image.size[0] - link_logo.size[0]) // 2,
            (qr_image.size[1] - link_logo.size[1]) // 2)
        qr_image.paste(link_logo, pos)

        # Taking QR Code Name from User

        qr_name = input("\nEnter QR Code Name ( By Default : URL ) :\n\n>> ")

        if qr_name == "":
            qr_image.save("URL.png")    # Save The Generated QR Code
        else:
            qr_image.save(qr_name+".png")

        print("\nYour QR Code is Generated Successfully 😊\n")
    else:
        print("\nInput Link Not Text\n")

elif qr_data == 7:
    txt_img = './Icons/TXT.png'
    txt_logo = Image.open(txt_img)

    basewidth = 100     # BaseWidth

    # Adjust Image Size

    wpercent = (basewidth/float(txt_logo.size[0]))
    hsize = int((float(txt_logo.size[1])*float(wpercent)))
    txt_logo = txt_logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)

    text = input("\nEnter Free Text :\n\n>> ")    # Taking Text Data

    qr.add_data(text)    # Adding Data to QR Code
    qr.make()    # Generating QR Code

    # Taking Color From User

    foreground_color = input("\nSelect Foreground Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default Black ) :\n\n>> ")
    background_color = input("\nSelect Background Colour for QR Code, E.g : Red, Green, Blue, Etc ( If Empty by Default White ) :\n\n>> ")

    if foreground_color == "" and background_color == "":
        qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    elif foreground_color == "" and background_color == background_color:
        qr_image = qr.make_image(fill_color="black", back_color=background_color).convert('RGB')
    elif foreground_color == foreground_color and background_color == "":
        qr_image = qr.make_image(fill_color=foreground_color, back_color="white").convert('RGB')
    else:
        qr_image = qr.make_image(fill_color=foreground_color, back_color=background_color).convert('RGB')
    
    # Size of QR code

    pos = ((qr_image.size[0] - txt_logo.size[0]) // 2,
        (qr_image.size[1] - txt_logo.size[1]) // 2)
    qr_image.paste(txt_logo, pos)

    # Taking QR Code Name from User

    qr_name = input("\nEnter QR Code Name ( By Default : TxT ) :\n\n>> ")

    if qr_name == "":
        qr_image.save("TxT.png")    # Save The Generated QR Code
    else:
        qr_image.save(qr_name+".png")

    print("\nYour QR Code is Generated Successfully 😊\n")

