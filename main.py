from flask import Flask, request, send_from_directory, redirect, Response
import random
import os

response = Response

domain = "https://api.andyishereboi.com"
port = 25006
methods = ['GET']# ,'POST'
app = Flask(__name__)

# get header from client: auth = request.headers.get('authorization')


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}



VAPOR_DICT = { 'a':'ａ', 'b':'ｂ',
                    'c':'ｃ', 'd':'ｄ', 'e':'ｅ',
                    'f':'ｆ', 'g':'ｇ', 'h':'ｈ',
                    'i':'ｉ', 'j':'ｊ', 'k':'ｋ',
                    'l':'ｌ', 'm':'ｍ', 'n':'ｎ',
                    'o':'ｏ', 'p':'ｐ', 'q':'ｑ',
                    'r':'ｒ', 's':'ｓ', 't':'ｔ',
                    'u':'ｕ', 'v':'ｖ', 'w':'ｗ',
                    'x':'ｘ', 'y':'ｙ', 'z':'ｚ',
                    'A':'Ａ', 'B':'Ｂ',
                    'C':'Ｃ', 'D':'Ｄ', 'E':'Ｅ',
                    'F':'Ｆ', 'G':'Ｇ', 'H':'Ｈ',
                    'I':'Ｉ', 'J':'Ｊ', 'K':'Ｋ',
                    'L':'Ｌ', 'M':'Ｍ', 'N':'Ｎ',
                    'O':'Ｏ', 'P':'Ｐ', 'Q':'Ｑ',
                    'R':'Ｒ', 'S':'Ｓ', 'T':'Ｔ',
                    'U':'Ｕ', 'V':'Ｖ', 'W':'Ｗ',
                    'X':'Ｘ', 'Y':'Ｙ', 'Z':'Ｚ',
                    '1':'１', '2':'２', '3':'３',
                    '4':'４', '5':'５', '6':'６',
                    '7':'７', '8':'８', '9':'９',
                    '0':'０', ',':'  ', '.':'．',
                    '?':'？', '/':'／', '-':'－',
                    '(':'（', ')':'）', '_':'＿',
                    '{':'｛', '}':'｝', '[':'［',
                    ']':'］'}
 
# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
 
            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
 
    return cipher

def vapor_encode(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
 
            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += VAPOR_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
 
    return cipher
	

@app.route('/favicon.ico')
def slash_favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico',mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=methods)
def slash():
    return f"""
Methods: <br>
GET<br>
<br>
Availible Endpoints: <br>
<br>
Fun: <br>
Quote: Returns a quote from someone. URL Example: <a href=\"{domain}/api/fun/quote\">{domain}/api/fun/quote</a> <br>
Pickupline: Returns a pickup line. URL Example: <a href=\"{domain}/api/fun/pickupline\">{domain}/api/fun/pickupline</a> <br>
Kaomoji: Returns a kaomoji. URL Example: <a href=\"{domain}/api/fun/kaomoji\">{domain}/api/fun/kaomoji</a> <br>
Binary: Returns your text input in binary code. URL Example: <a href=\"{domain}/api/fun/binary?text=hi\">{domain}/api/fun/binary?text=hi</a> <br>
Morse: Returns your text input in morse code. URL Example: <a href=\"{domain}/api/fun/morse?text=hi there lol\">{domain}/api/fun/morse?text=hi there lol</a> <br>
Vapor: Returns your text input in vapor format. URL Example: <a href=\"{domain}/api/fun/vapor?text=hi\">{domain}/api/fun/vapor?text=hi</a> <br>
Reverse: Returns your text input reversed. URL Example: <a href=\"{domain}/api/fun/reverse?text=hi there lol\">{domain}/api/fun/reverse?text=hi there lol</a> <br>
Truth: Returns a truth (truth or dare). URL Example: <a href=\"{domain}/api/fun/truth\">{domain}/api/fun/truth</a> <br>
Dare:  Returns a dare (truth or dare). URL Example: <a href=\"{domain}/api/fun/dare\">{domain}/api/fun/dare</a> <br>
<br>
Facts: <br>
Whalefact: Returns a whale fact. URL Example: <a href=\"{domain}/api/fun/whalefact\">{domain}/api/fun/whalefact</a> <br>
Randomfact: Returns a random fact from the facts list. URL Example: <a href=\"{domain}/api/fun/randomfact\">{domain}/api/fun/randomfact</a> <br>
Racoonfact: Returns a racoon fact. URL Example: <a href=\"{domain}/api/fun/racoonfact\">{domain}/api/fun/racoonfact</a> <br>
Rabbitfact: Returns a rabbit fact. URL Example: <a href=\"{domain}/api/fun/rabbitfact\">{domain}/api/fun/rabbitfact</a> <br>
Pandafact: Returns a panda fact. URL Example: <a href=\"{domain}/api/fun/pandafact\">{domain}/api/fun/pandafact</a> <br>
Koalafact: Returns a koala fact. URL Example: <a href=\"{domain}/api/fun/koalafact\">{domain}/api/fun/koalafact</a> <br>
Kangaroofact: Returns a kangaroo fact. URL Example: <a href=\"{domain}/api/fun/kangaroofact\">{domain}/api/fun/kangaroofact</a> <br>
Giraffefact: Returns a giraffe fact. URL Example: <a href=\"{domain}/api/fun/giraffefact\">{domain}/api/fun/giraffefact</a> <br>
Foxfact: Returns a fox fact. URL Example: <a href=\"{domain}/api/fun/foxfact\">{domain}/api/fun/foxfact</a> <br>
Dogfact: Returns a dog fact. URL Example: <a href=\"{domain}/api/fun/rabbitfact\">{domain}/api/fun/rabbitfact</a> <br>
Catfact: Returns a cat fact. URL Example: <a href=\"{domain}/api/fun/catfact\">{domain}/api/fun/catfact</a> <br>
Birdfact: Returns a bird fact. URL Example: <a href=\"{domain}/api/fun/birdfact\">{domain}/api/fun/birdfact</a> <br>
<br>
Other trash:<br>
none yet
"""


@app.route('/api/', methods=methods)
def slash_api():
    return redirect("http://api.andyishereboi.com/", code=302)


@app.route('/api/fun/birdfact', methods=['GET'])
def slash_api_fun_birdfact():
    birdfact = open("lists/birdfact.txt", 'r').readlines()
    birdfact = random.choice(birdfact)
    birdfact = birdfact.replace("\n","")
    return {
        "fact": f"{birdfact}"
    }

@app.route('/api/fun/catfact', methods=methods)
def slash_api_fun_catfact():
    catfact = open("lists/catfact.txt", 'r').readlines()
    catfact = random.choice(catfact)
    catfact = catfact.replace("\n","")
    return {
        "fact": f"{catfact}"
    }

@app.route('/api/fun/dare', methods=methods)
def slash_api_fun_dare():
    dare = open("lists/dare.txt", 'r').readlines()
    dare = random.choice(dare)
    dare = dare.replace("\n","")
    return {
        "dare": f"{dare}"
    }

@app.route('/api/fun/dogfact', methods=methods)
def slash_api_fun_dogfact():
    dogfact = open("lists/dogfact.txt", 'r').readlines()
    dogfact = random.choice(dogfact)
    dogfact = dogfact.replace("\n","")
    return {
        "fact": f"{dogfact}"
    }

@app.route('/api/fun/foxfact', methods=methods)
def slash_api_fun_foxfact():
    foxfact = open("lists/foxfact.txt", 'r').readlines()
    foxfact = random.choice(foxfact)
    foxfact = foxfact.replace("\n","")
    return {
        "fact": f"{foxfact}"
    }

@app.route('/api/fun/giraffefact', methods=methods)
def slash_api_fun_giraffefact():
    giraffefact = open("lists/giraffefact.txt", 'r').readlines()
    giraffefact = random.choice(giraffefact)
    giraffefact = giraffefact.replace("\n","")
    return {
        "fact": f"{giraffefact}"
    }

@app.route('/api/fun/kaomoji', methods=methods)
def slash_api_fun_kaomoji():
    kaomoji = open("lists/kaomoji.txt", 'r').readlines()
    kaomoji = random.choice(kaomoji)
    kaomoji = kaomoji.replace("\n","")
    return {
        "kaomoji": f"{kaomoji}"
    }

@app.route('/api/fun/kangaroofact', methods=methods)
def slash_api_fun_kangaroofact():
    kangaroofact = open("lists/kangaroofact.txt", 'r').readlines()
    kangaroofact = random.choice(kangaroofact)
    kangaroofact = kangaroofact.replace("\n","")
    return {
        "fact": f"{kangaroofact}"
    }

@app.route('/api/fun/koalafact', methods=methods)
def slash_api_fun_koalafact():
    koalafact = open("lists/koalafact.txt", 'r').readlines()
    koalafact = random.choice(koalafact)
    koalafact = koalafact.replace("\n","")
    return {
        "fact": f"{koalafact}"
    }

@app.route('/api/fun/pandafact', methods=methods)
def slash_api_fun_pandafact():
    pandafact = open("lists/pandafact.txt", 'r').readlines()
    pandafact = random.choice(pandafact)
    pandafact = pandafact.replace("\n","")
    return {
        "fact": f"{pandafact}"
    }

@app.route('/api/fun/pickupline', methods=methods)
def slash_api_fun_pickupline():
    pickupline = open("lists/pickupline.txt", 'r').readlines()
    pickupline = random.choice(pickupline)
    pickupline = pickupline.replace("\n","")
    return {
        "pickupLine": f"{pickupline}"
    }

@app.route('/api/fun/quote', methods=methods)
def slash_api_fun_quote():
    quote = open("lists/quote.txt", 'r').readlines()
    quote = random.choice(quote)
    quote = quote.replace("\n","")
    return {
        "quote": f"{quote}",
        "author": "No author (i dont know how)"
    }

@app.route('/api/fun/rabbitfact', methods=methods)
def slash_api_fun_rabbitfact():
    rabbitfact = open("lists/rabbitfact.txt", 'r').readlines()
    rabbitfact = random.choice(rabbitfact)
    rabbitfact = rabbitfact.replace("\n","")
    return {
        "fact": f"{rabbitfact}"
    }

@app.route('/api/fun/racoonfact', methods=methods)
def slash_api_fun_racoonfact():
    racoonfact = open("lists/racoonfact.txt", 'r').readlines()
    racoonfact = random.choice(racoonfact)
    racoonfact = racoonfact.replace("\n","")
    return {
        "fact": f"{racoonfact}"
    }

@app.route('/api/fun/randomfact', methods=methods)
def slash_api_fun_randomfact():
    randomfact = open("lists/randomfact.txt", 'r').readlines()
    randomfact = random.choice(randomfact)
    randomfact = randomfact.replace("\n","")
    return {
        "fact": f"{randomfact}"
    }

@app.route('/api/fun/truth', methods=methods)
def slash_api_fun_truth():
    truth = open("lists/truth.txt", 'r').readlines()
    truth = random.choice(truth)
    truth = truth.replace("\n","")
    return {
        "truth": f"{truth}"
    }

@app.route('/api/fun/whalefact', methods=methods)
def slash_api_fun_whalefact():
    whalefact = open("lists/whalefact.txt", 'r').readlines()
    whalefact = random.choice(whalefact)
    whalefact = whalefact.replace("\n","")
    return {
        "fact": f"{whalefact}"
    }

@app.route('/api/fun/binary', methods=methods)
def slash_api_binary():
    text = request.args.get('text')
    if text != None:
        res = ' '.join(format(x, 'b') for x in bytearray(text, 'utf-8'))
        return {
            "text": res
        }
    else:
        return Response("{\"text\": \"SPECIFY TEXT TO CONVERT\" }", status=400, mimetype='application/json')

@app.route('/api/fun/reverse', methods=methods)
def slash_api_fun_reverse():
    text = request.args.get('text')
    if text != None:
        res = text[::-1]
        return {
            "text": res
        }
    else:
        return Response("{\"text\": \"SPECIFY TEXT TO CONVERT\" }", status=400, mimetype='application/json')

    
@app.route('/api/fun/morse', methods=methods)
def slash_api_fun_morse():
    text = request.args.get('text')
    if text != None:
        result = encrypt(text.upper())
        return {
            "text": result
        }
    else:
        return Response("{\"text\": \"SPECIFY TEXT TO CONVERT\" }", status=400, mimetype='application/json')

    
@app.route('/api/fun/vapor', methods=methods)
def slash_api_fun_vapor():
    text = request.args.get('text')
    if text != None:
        result = vapor_encode(text)
        return {
            "text": result
        }
    else:
        return Response("{\"text\": \"SPECIFY TEXT TO CONVERT\" }", status=400, mimetype='application/json')
    
@app.route('/karen-test/notifications', methods=methods)
def karen_test_notifications():
    import flask
    response = flask.jsonify([
  {
    "date": "october 2222 (just display this raw text as date)", 
    "description": "DESCRIPTION OF THIS CARD", 
    "title": "EXAMPLE TITLE", 
    "type": "info"
  }, 
  {
    "date": "june 1", 
    "description": "pay for premium or else", 
    "title": "second card", 
    "type": "money"
  }, 
  {
    "date": "may 22", 
    "description": "your premium is running out", 
    "title": "third", 
    "type": "warn"
  }, 
  {
    "date": "negitive 5", 
    "description": "hmmm running up the walls again????", 
    "title": "pee", 
    "type": "money"
  }, 
  {
    "date": "june 1", 
    "description": "pay for premium or else", 
    "title": "second card", 
    "type": "money"
  }, 
  {
    "date": "may 22", 
    "description": "your premium is running out", 
    "title": "third", 
    "type": "warn"
  }, 
  {
    "date": "negitive 5", 
    "description": "hmmm running up the walls again????", 
    "title": "pee", 
    "type": "money"
  }, 
  {
    "date": "june 1", 
    "description": "pay for premium or else", 
    "title": "second card", 
    "type": "money"
  }, 
  {
    "date": "may 22", 
    "description": "your premium is running out", 
    "title": "third", 
    "type": "warn"
  }, 
  {
    "date": "negitive 5", 
    "description": "hmmm running up the walls again????", 
    "title": "pee", 
    "type": "money"
  }, 
  {
    "date": "june 1", 
    "description": "pay for premium or else", 
    "title": "second card", 
    "type": "money"
  }, 
  {
    "date": "may 22", 
    "description": "your premium is running out", 
    "title": "third", 
    "type": "warn"
  }, 
  {
    "date": "negitive 5", 
    "description": "hmmm running up the walls again????", 
    "title": "pee", 
    "type": "money"
  }
]
)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)