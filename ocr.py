# -*- coding: utf-8 -*- 

import sys
import os
import time
import re
import datetime
from pytesseract import image_to_boxes, image_to_data, image_to_osd, Output
import pandas as pd
import cv2
from PIL import Image as img
from distutils.dir_util import copy_tree

matched_words = []
blacklist = 'Obama|Carter|Schwarzenegger|Sanders|Biden|Clinton|Harris|Albright|Gore|W.Bush|Warren|Clinton|OcasioCortez|Lewis|Pelosi|Booker|Booker|Trump|Giffords|Carson|AMTRAK|Administrative Conference of the United States|Advisory Council on Historic Preservation|American Battle Monuments Commission|Appalachian Regional Commission|Appraisal Subcommittee|Armed Forces Retirement Home|Barry Goldwater Scholarship and Excellence in Education Foundation|Central Intelligence Agency|Chemical Safety Board|Civil Air Patrol|Commodity Futures Trading Commission|Consumer Financial Protection Bureau|Consumer Product Safety Commission|Corporation for National & Community Service|Corporation for National and Community Service, Office Of Inspector General|Council of Inspectors General on Integrity and Efficiency|Court Services and Offender Supervision|Defense Nuclear Facilities Safety Board|Delta Regional Authority|Denali Commission|Department of Commerce|Department of Defense|Department of Education|Department of Energy|Department of Health and Human Services|Department of Homeland Security|Department of Housing and Urban Development|Department of Justice|Department of Labor|Department of State|Department of State, Office of Inspector General|Department of Transportation|Department of Veterans Affairs|Department of the Interior|Department of the Treasury|Director of National Intelligence|Election Assistance Commission|Environmental Protection Agency|Equal Employment Opportunity Commission|Executive Office of the President|Export|Import Bank of the U.S.|Farm Credit Administration|Federal Communications Commission|Federal Deposit Insurance Corporation|Federal Election Commission|Federal Energy Regulatory Commission|Federal Housing Finance Agency|Federal Housing Finance Agency, Office of Inspector General|Federal Labor Relations Authority|Federal Maritime Commission|Federal Mediation and Conciliation Service|Federal Mine Safety and Health Review Commission|Federal Permitting Improvement Steering Council|Federal Reserve Board of Governors|Federal Retirement Thrift Investment Board|Federal Trade Commission|General Services Administration|Gulf Coast Ecosystem Restoration Council|Harry S. Truman Scholarship Foundation|Institute of Museum and Library Services|Inter-American Foundation|James Madison Memorial Fellowship Foundation|Japan-US Friendship Commission|John F. Kennedy Center for Performing Arts|Legal Services Corporation|Marine Mammal Commission|Merit Systems Protection Board|Millennium Challenge Corporation|Morris K. Udall and Stewart L. Udall Foundation|National Aeronautics and Space Administration|National Archives and Records Administration|National Capital Planning Commission|National Council on Disability|National Credit Union Administration|National Endowment for the Arts|National Endowment for the Humanities|National Gallery of Art|National Indian Gaming Commission|National Labor Relations Board|National Mediation Board|National Nanotechnology Coordination Office|National Nuclear Security Administration|Obama|Carter|Schwarzenegger|Sanders|Biden|Clinton|Harris|Albright|Gore|Bush|Warren|Clinton|Cortez|Lewis|Pelosi|Booker|Booker|Trump|Giffords|Carson|Barack Obama|Jimmy Carter|Arnold Schwarzenegger|Bernie Sanders|Joe Biden|Bill Clinton|Kamala Harris|Madeleine Albright|Al Gore|George W. Bush|Elizabeth Warren|Hillary Clinton|Alexandria Ocasio Cortez|aoc|John Lewis|Nancy Pelosi|Cory Booker|Cory Booker|Donald Trump|Gabrielle Giffords|Ben Carson|republicans|fapping|Hitler|AF|pegging|asf|vote|tally|election|fascism|senate|house|dems|media|fbi|chuck schumer|conancy pel|covid|biden|trump|george soros|genocide|china|radical|ukraine|government|tax|govenor|socialism|blackface|left|climate change|troops|kill|afghanistan|iraq|candidate|soviet|swastika|russia|conflict|war|capitalli|conservative|slavery|electoral college|invation|military|taliban|amendment|hunter biden|party|libertarian|job|work|agency|mortgage|loan|home|address|applicant|hire|hiring|recruiting|payroll|position|part time|full time|tenant|rent|sale sign|zelensky|act of settlement|act of union|ad valorem|agrarian revolution|aggression|alliance|appeal|appropriation bill|armed neutrality|autonomy|balance of trade|balance of power|ballot|benevolent despotism|bill of rights|blockade|buffer-state|bull|bullion|bureaucracy|by law|bye laws|casting vote|census|centralised monarchy|chamber of commerce|chancellor of the exchequer|charter of liberties|chronology|circumnavigation|citizen|citizenship|city fathers|civics|civil disobedience|civil war|coalition ministry|code|commonwealth, the|consensus|constituency|constitution|constitutional monarchy|constitutional theory|constitution, federal|consumer|contraband articles|convention|crown colony|crusade|culture|currency|curfew|customs duties|deadlock, administrative|debt relief act|declaration of rights|delegate|demagogue|democracy|dependency|depreciation of money|despotic government|diarchy|direct taxation|divine right|doctrine of lapse|domicile|doomsday book|economic structure|electorate|embassy|emigrants|emigration|empire|envoy|excommunication|executive council|exploitation|exploration|famine relief|fanaticism|federal constitution|feudal system|fiduciary|fief|floating debt|flying shuttle|forced loan|foreign office|foreign policy|franchise|freeholders|free state|free trade|guild|gold standard|government, responsible|grand alliance|grants-in-aid|great charter of liberties|habeas corpus act|high treason|home government|home office|hostage|immigrants|immigration|impeachment|imperialism|incidence of taxation|independents|individual liberty|indulgence|industrial revolution|initiative, private|initiative, public|inscription|interdict|interpellations|joint stock company|journey man|judicial service|jurisdiction|labour, division of|labour legislation|laissez-faire|land tenure|legal tender|legislative council|letters patent|liberty of the press|limited liability|limited monarchy|magna carta|mandatory state|manorial system|martial law|military occupation|minority minute|mobocracy|negotiation|neolithic age|no-confidence motion|nomination|non-aggression|non-co-operation|non-intervention policy|non-official element|no tax campaign|opposition, the|orders in council|ordinance|palaeolithic age|passive resistance|petition of right|policy|poor rate|preferential tariff|protective duties|protective tariff|rate payers|reforms act|regulating act|reign of terror|renaissance, the|representative government|responsible government|round table conference|service, secret|sinking fund|squire|standard of life|standing army|standing committee|standing orders|stock and land lease system|subject, reserved|subject, transferred|subsidiary system|suffrage|tariffs|temperance|tolls|trade union|unitary constitution|vested interests|veto|white-paper|working committee|world court|write of habeas corpus|bullshit|gay|porn|fucking up|arse|arouse|blowing|dick|fuck|vagina|shit|lesbian|moan|prostitute|sex|hookup|missionary|omfg|wtf|rape|ass|bitch|cum|presidential|trump|democrats|Russia|Putin|US house candidate|congresswomen|congressman|vaccines|voting|abortions|whip|smoke|vibrator|alcohol|Fuck|balls|nude|sex|fuck|horny|ahole|anus|ashle|ashles|asholes|assmonkey|assface|asshle|asshlez|asshole|assholes|assholz|asswipe|azzhole|bassterds|bastard|bastards|bastardz|basterds|basterdz|biatch|bitch|bitches|blowjob|boffing|butthole|buttwipe|carpetmuncher|cawk|cawks|clit|cnts|cntz|cock|cockhead|cockhead|cocks|cocksucker|sucking|suck|cocksucker|crap|cunt|cunts|cuntz|dick|dild|dilds|dildo|dildos|dilld|dillds|dominatricks|dominatrics|dominatrix|dyke|enema|fagt|faget|faggt|faggit|faggot|fagit|fags|fagz|faig|faigs|fart|flippingthebird|fuck|fucker|fuckin|fucking|fucks|fudgepacker|fukah|fuken|fuker|fukin|fukk|fukkah|fukken|fukker|fukkin|gayboy|gaygirl|gays|gayz|goddamned|hells|hoar|hoor|hoore|jackoff|japs|jerkoff|jerk|jisim|jiss|jizm|jizz|knob|knobs|knobz|kunt|kunts|kuntz|lesbian|lezzian|lipshits|lipshitz|masochist|masokist|massterbait|masstrbait|masstrbate|masterbaiter|masterbate|masterbates|mothafucker|mothafuker|mothafukkah|mothafukker|motherfucker|motherfukah|motherfuker|motherfukkah|motherfukker|motherfucker|muthafucker|muthafukah|muthafuker|muthafukkah|muthafukker|nastt|nigger|nigur|niiger|niigr|orafis|orgasim|orgasm|orgasum|oriface|orifice|orifiss|packi|packie|packy|paki|pakie|paky|pecker|peeenus|peeenusss|peenus|peinus|pens|penas|penis|penisbreath|penus|penuus|phuc|phuck|phuk|phuker|phukker|polac|polack|polak|poonani|prck|pusse|pussee|pussy|puuke|puuker|queer|queers|queerz|qweers|qweerz|qweir|recktum|rectum|retard|sadist|scank|schlong|screwing|semen|sexy|sht|shter|shts|shtter|shtz|shit|shits|shitter|shitty|shity|shitz|shyt|shyte|shytty|shyty|skanck|skank|skankee|skankey|skanks|skanky|slut|sluts|slutty|slutz|sonofabitch|turd|vajina|vagna|vagiina|vagina|vajna|vajina|vullva|vulva|whre|whore|xrated|bch|bitch|blowjob|clit|arschloch|fuck|shit|asshole|btch|btch|bastard|bich|boiolas|buceta|cawk|chink|cipa|clits|cock|cunt|dildo|dirsa|ejakulate|fatass|fcuk|fuxr|hoer|hore|jism|kawk|litch|lich|lesbian|masturbate|masterbat|masterbat|motherfucker|mofo|nazi|nigga|nigger|nutsack|phuck|pimpis|pusse|pussy|scrotum|shemale|slut|smut|teets|tits|boob|teez|testical|testicle|titt|jackoff|wank|whoar|whore|damn|dyke|fuck|shit|amcik|andskota|arse|assrammer|ayir|bich|bitch|bollock|breasts|buttpirate|cabron|cazzo|chraa|chuj|cock|cunt|daygo|dego|dick|dike|dupa|dziwka|ejackulate|ekrem|ekto|enculer|faen|fanculo|fanny|feces|felcher|ficken|fitt|flikker|foreskin|fotze|futkretzn|gook|guiena|hell|helvete|hoer|honkey|huevon|injun|jizz|kanker|kike|klootzak|kraut|knulle|kuksuger|kurac|kurwa|kusi|kyrpa|lesbo|mamhoon|masturbat|merd|mibun|monkleigh|mouliewop|muie|mulkku|muschi|nazis|nepesaurio|nigger|orospu|paska|perse|picka|pierdol|pillu|pimmel|piss|pizda|poontsee|poop|porn|prn|preteen|pule|puta|puto|qahbeh|queef|rautenberg|schaffer|scheiss|schlampe|schmuck|screw|sharmuta|sharmute|shipal|shiz|skribz|skurwysyn|sphencter|spic|spierdalaj|splooge|suka|testicle|titt|twat|vittu|wank|wetback|wichser|yed|zabourah|wtf|cum|f\*\*\*|f\*\*c|f\*\*\*'
cnt = 0

print(str(sys.argv[1]))
folder = str(sys.argv[1])
# folder = r'C:\Users\uri\Downloads\scmmr extra3'
# files = os.listdir(folder)
# files = files.append(os.listdir(folder))
# print(files)
paths = []
lines = []

del_pics = 0
ok_pics = 0

for root, dirs, files in os.walk(os.path.abspath(folder)):
    for file in files:
        # print(os.path.join(root, file))
        paths.append(os.path.join(root, file))
#copy_tree(folder, folder + r'\uncensored')


def ocr(targetfile):
    os.chdir('C:\Program Files\Tesseract-OCR')
    # os.system(f'cd C:\Program Files\Tesseract-OCR') path = folder + r"\"" + f print(path) response = (os.popen(
    # f'tesseract "{targetfile}"  - -l eng -c tessedit_char_whitelist="
    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" ').read())
    response = image_to_data(targetfile, 'eng', output_type='data.frame',
                             config='tessedit_char_whitelist=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"')

    # response= str(response)
    # list1 = list(response.split(" "))
    # response = str(response.lower())

    # # print(targetfile)
    # final_response = response_cmd.replace("\n", "\t")

    return response

count_f = 0
total_pics = len(paths)

for i in range(2):
    for f in paths:
        count_f +=1
        print(f'proccesing pic {count_f} out of {total_pics}  ')
        print(matched_words)


        image = cv2.imread(f)
        # result = " ".join(line.strip() for line in ocr.splitlines())
        # response0 = ocr(f).replace(' ', '').replace('\s', '').replace('\t', '').replace('\r', '').replace('\n', '')
        xxx = ocr(f)

        # print(result)
        print(xxx)

        df = pd.DataFrame(xxx,
                          columns=['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top',
                                   'width', 'height', ' conf', 'text'])
        # print(df[df["text"].str.contains(blacklist, na=False, regex=True)])
        try:
            matched_rows = df[df["text"].str.contains(blacklist, na=False, regex=True, case=False)]

        except:
            pass

        if matched_rows.empty:
            pass
        else:
            del_pics += 1

        # print(len(matched_rows.index))
        # print('xxx', matched_rows["width"].iloc[1])
        for row in range(0, len(matched_rows.index)):
            width = matched_rows["width"].iloc[row]
            height = matched_rows["height"].iloc[row]
            left = matched_rows["left"].iloc[row]
            top = matched_rows["top"].iloc[row]
            text = matched_rows["text"].iloc[row]
            print('match!', text, width, height, left, top)
            matched_words.append(text)
            # image_pil = img.open(f)

            save = cv2.rectangle(image, (left, top), (left + width, top + height), (0, 0, 255), -1)
            cv2.imwrite(f, image)

ok_pics = len(paths) - del_pics
print(f'result: censored pics:{del_pics} , passed pics:{ok_pics}')
print('censored words: ' + str(matched_words))
print(r'thats one filthy mouth... :)')

