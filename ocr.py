# -*- coding: utf-8 -*- 

import sys
import os
import time
import re
import datetime


blacklist = 'nude|sex|fuck|horny|ahole|anus|ashle|ashles|asholes|assmonkey|assface|asshle|asshlez|asshole|assholes|assholz|asswipe|azzhole|bassterds|bastard|bastards|bastardz|basterds|basterdz|biatch|bitch|bitches|blowjob|boffing|butthole|buttwipe|carpetmuncher|cawk|cawks|clit|cnts|cntz|cock|cockhead|cockhead|cocks|cocksucker|sucking|suck|cocksucker|crap|cunt|cunts|cuntz|dick|dild|dilds|dildo|dildos|dilld|dillds|dominatricks|dominatrics|dominatrix|dyke|enema|fagt|faget|faggt|faggit|faggot|fagit|fags|fagz|faig|faigs|fart|flippingthebird|fuck|fucker|fuckin|fucking|fucks|fudgepacker|fukah|fuken|fuker|fukin|fukk|fukkah|fukken|fukker|fukkin|gayboy|gaygirl|gays|gayz|goddamned|hells|hoar|hoor|hoore|jackoff|japs|jerkoff|jisim|jiss|jizm|jizz|knob|knobs|knobz|kunt|kunts|kuntz|lesbian|lezzian|lipshits|lipshitz|masochist|masokist|massterbait|masstrbait|masstrbate|masterbaiter|masterbate|masterbates|mothafucker|mothafuker|mothafukkah|mothafukker|motherfucker|motherfukah|motherfuker|motherfukkah|motherfukker|motherfucker|muthafucker|muthafukah|muthafuker|muthafukkah|muthafukker|nastt|nigger|nigur|niiger|niigr|orafis|orgasim|orgasm|orgasum|oriface|orifice|orifiss|packi|packie|packy|paki|pakie|paky|pecker|peeenus|peeenusss|peenus|peinus|pens|penas|penis|penisbreath|penus|penuus|phuc|phuck|phuk|phuker|phukker|polac|polack|polak|poonani|prck|pusse|pussee|pussy|puuke|puuker|queer|queers|queerz|qweers|qweerz|qweir|recktum|rectum|retard|sadist|scank|schlong|screwing|semen|sexy|sht|shter|shts|shtter|shtz|shit|shits|shitter|shitty|shity|shitz|shyt|shyte|shytty|shyty|skanck|skank|skankee|skankey|skanks|skanky|slut|sluts|slutty|slutz|sonofabitch|turd|vajina|vagna|vagiina|vagina|vajna|vajina|vullva|vulva|whre|whore|xrated|bch|bitch|blowjob|clit|arschloch|fuck|shit|asshole|btch|btch|bastard|bich|boiolas|buceta|cawk|chink|cipa|clits|cock|cunt|dildo|dirsa|ejakulate|fatass|fcuk|fuxr|hoer|hore|jism|kawk|litch|lich|lesbian|masturbate|masterbat|masterbat|motherfucker|mofo|nazi|nigga|nigger|nutsack|phuck|pimpis|pusse|pussy|scrotum|shemale|slut|smut|teets|tits|boobs|teez|testical|testicle|titt|jackoff|wank|whoar|whore|damn|dyke|fuck|shit|amcik|andskota|arse|assrammer|ayir|bich|bitch|bollock|breasts|buttpirate|cabron|cazzo|chraa|chuj|cock|cunt|daygo|dego|dick|dike|dupa|dziwka|ejackulate|ekrem|ekto|enculer|faen|fanculo|fanny|feces|felcher|ficken|fitt|flikker|foreskin|fotze|futkretzn|gook|guiena|hell|helvete|hoer|honkey|huevon|injun|jizz|kanker|kike|klootzak|kraut|knulle|kuksuger|kurac|kurwa|kusi|kyrpa|lesbo|mamhoon|masturbat|merd|mibun|monkleigh|mouliewop|muie|mulkku|muschi|nazis|nepesaurio|nigger|orospu|paska|perse|picka|pierdol|pillu|pimmel|piss|pizda|poontsee|poop|porn|prn|preteen|pule|puta|puto|qahbeh|queef|rautenberg|schaffer|scheiss|schlampe|schmuck|screw|sharmuta|sharmute|shipal|shiz|skribz|skurwysyn|sphencter|spic|spierdalaj|splooge|suka|testicle|titt|twat|vittu|wank|wetback|wichser|yed|zabourah|wtf|cum|f\*\*\*|f\*\*c|f\*\*\*'


print(str(sys.argv[1]))
folder = (str(sys.argv[1]))
# folder = r'C:\Users\uri\Downloads\scmmr extra3'
# files = os.listdir(folder)
# files = files.append(os.listdir(folder))
# print(files)
paths = []
lines= []

del_pics = 0
ok_pics = 0

for root, dirs, files in os.walk(os.path.abspath(folder)):
    for file in files:
        # print(os.path.join(root, file))
        paths.append(os.path.join(root, file))


def ocr(targetfile):
    os.chdir('C:\Program Files\Tesseract-OCR')
    # os.system(f'cd C:\Program Files\Tesseract-OCR')
    # path = folder + r"\"" + f
    # print(path)
    response = (os.popen(f'tesseract "{targetfile}"  - -l eng -c tessedit_char_whitelist=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" ').read())
    response = str(response.lower())
    # # print(targetfile)
    # final_response = response_cmd.replace("\n", "\t")

    return response


for f in paths:


    # result = " ".join(line.strip() for line in ocr.splitlines())
    # response0 = ocr(f).replace(' ', '').replace('\s', '').replace('\t', '').replace('\r', '').replace('\n', '')
    xxx = ocr(f)


    # print(result)
    print(xxx)
    if bool(re.search(blacklist , xxx)):
        print('match')
        print(re.findall(blacklist , xxx))
        del_pics += 1
        os.remove(f)

        
        
        
    else:
        print('no match')
        ok_pics += 1


    #time.sleep(1)
    #print(re.search('fuck', response0))
    # print(response)
    # response = re.sub('/n',"", response)
    # response = response.replace('\n', '')
    # print(response2)
    # print(re.search(r'fuck', response, flags=re.MULTILINE))
    #
    # else:
    #     ok_pics += 1
    #     print('no match')


print(f'result: del pics:{del_pics} , passed pics:{ok_pics}')
with open(r'C:\Users\uri\ocr_log.txt', 'a') as f:
    f.write((str(datetime.datetime.now()) + str(f' result: del pics:{del_pics} , passed pics:{ok_pics}\n')))

