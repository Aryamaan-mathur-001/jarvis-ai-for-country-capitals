import pyttsx3
import speech_recognition as sr
import cv2
import threading
import time
import urllib.request
import numpy as np

# Country-capital database
country_capitals ={
    "afghanistan": "kabul",
    "albania": "tirana",
    "algeria": "alger",
    "american samoa": "fagatogo",
    "andorra": "andorra la vella",
    "angola": "luanda",
    "anguilla": "the valley",
    "antarctica": "no city",
    "antigua and barbuda": "saint john's",
    "argentina": "buenos aires",
    "armenia": "yerevan",
    "aruba": "oranjestad",
    "australia": "canberra",
    "austria": "wien",
    "azerbaijan": "baku",
    "bahamas": "nassau",
    "bahrain": "al-manama",
    "bangladesh": "dhaka",
    "barbados": "bridgetown",
    "belarus": "minsk",
    "belgium": "bruxelles [brussel]",
    "belize": "belmopan",
    "benin": "porto-novo",
    "bermuda": "hamilton",
    "bhutan": "thimphu",
    "bolivia": "la paz",
    "bosnia and herzegovina": "sarajevo",
    "botswana": "gaborone",
    "bouvet island": "no city",
    "brazil": "brasília",
    "british indian ocean territory": "no city",
    "brunei": "bandar seri begawan",
    "bulgaria": "sofia",
    "burkina faso": "ouagadougou",
    "burundi": "bujumbura",
    "cambodia": "phnom penh",
    "cameroon": "yaounde",
    "canada": "ottawa",
    "cape verde": "praia",
    "cayman islands": "george town",
    "central african republic": "bangui",
    "chad": "n'djamena",
    "chile": "santiago de chile",
    "china": "peking",
    "christmas island": "flying fish cove",
    "cocos (keeling) islands": "west island",
    "colombia": "bogota",
    "comoros": "moroni",
    "congo": "brazzaville",
    "cook islands": "avarua",
    "costa rica": "san josé",
    "croatia": "zagreb",
    "cuba": "la habana",
    "cyprus": "nicosia",
    "czech republic": "praha",
    "denmark": "copenhagen",
    "djibouti": "djibouti",
    "dominica": "roseau",
    "dominican republic": "santo domingo de guzm",
    "east timor": "dili",
    "ecuador": "quito",
    "egypt": "cairo",
    "el salvador": "san salvador",
    "england": "london",
    "equatorial guinea": "malabo",
    "eritrea": "asmara",
    "estonia": "tallinn",
    "eswatini": "mbabane",
    "ethiopia": "addis abeba",
    "falkland islands": "stanley",
    "faroe islands": "tórshavn",
    "fiji islands": "suva",
    "finland": "helsinki [helsingfors]",
    "france": "paris",
    "french guiana": "cayenne",
    "french polynesia": "papeete",
    "french southern territories": "no city",
    "gabon": "libreville",
    "gambia": "banjul",
    "georgia": "tbilisi",
    "germany": "berlin",
    "ghana": "accra",
    "gibraltar": "gibraltar",
    "greece": "athenai",
    "greenland": "nuuk",
    "grenada": "saint george's",
    "guadeloupe": "basse-terre",
    "guam": "aga",
    "guatemala": "ciudad de guatemala",
    "guinea": "conakry",
    "guinea-bissau": "bissau",
    "guyana": "georgetown",
    "haiti": "port-au-prince",
    "heard island and mcdonald islands": "no city",
    "holy see (vatican city state)": "citt",
    "honduras": "tegucigalpa",
    "hong kong": "victoria",
    "hungary": "budapest",
    "iceland": "reykjavík",
    "india": "new delhi",
    "indonesia": "jakarta",
    "iran": "tehran",
    "iraq": "baghdad",
    "ireland": "dublin",
    "israel": "jerusalem",
    "italy": "roma",
    "ivory coast": "yamoussoukro",
    "jamaica": "kingston",
    "japan": "tokyo",
    "jordan": "amman",
    "kazakhstan": "astana",
    "kenya": "nairobi",
    "kiribati": "bairiki",
    "kuwait": "kuwait",
    "kyrgyzstan": "bishkek",
    "laos": "vientiane",
    "latvia": "riga",
    "lebanon": "beirut",
    "lesotho": "maseru",
    "liberia": "monrovia",
    "libya": "tripoli",
    "liechtenstein": "vaduz",
    "lithuania": "vilnius",
    "luxembourg": "luxembourg [luxemburg/l",
    "macao": "macao",
    "north macedonia": "skopje",
    "madagascar": "antananarivo",
    "malawi": "lilongwe",
    "malaysia": "kuala lumpur",
    "maldives": "male",
    "mali": "bamako",
    "malta": "valletta",
    "marshall islands": "dalap-uliga-darrit",
    "martinique": "fort-de-france",
    "mauritania": "nouakchott",
    "mauritius": "port-louis",
    "mayotte": "mamoutzou",
    "mexico": "ciudad de m",
    "micronesia, federated states of": "palikir",
    "moldova": "chisinau",
    "monaco": "monaco-ville",
    "mongolia": "ulan bator",
    "montenegro": "podgorica",
    "montserrat": "plymouth",
    "morocco": "rabat",
    "mozambique": "maputo",
    "myanmar": "rangoon (yangon)",
    "namibia": "windhoek",
    "nauru": "yaren",
    "nepal": "kathmandu",
    "netherlands": "amsterdam",
    "netherlands antilles": "willemstad",
    "new caledonia": "noum",
    "new zealand": "wellington",
    "nicaragua": "managua",
    "niger": "niamey",
    "nigeria": "abuja",
    "niue": "alofi",
    "norfolk island": "kingston",
    "north korea": "pyongyang",
    "northern ireland": "belfast",
    "northern mariana islands": "garapan",
    "norway": "oslo",
    "oman": "masqat",
    "pakistan": "islamabad",
    "palau": "koror",
    "palestine": "gaza",
    "panama": "ciudad de panamá",
    "papua new guinea": "port moresby",
    "paraguay": "asunción",
    "peru": "lima",
    "philippines": "manila",
    "pitcairn": "adamstown",
    "poland": "warszawa",
    "portugal": "lisboa",
    "puerto rico": "san juan",
    "qatar": "doha",
    "reunion": "saint-denis",
    "romania": "bucuresti",
    "russia": "moscow",
    "rwanda": "kigali",
    "saint helena": "jamestown",
    "saint kitts and nevis": "basseterre",
    "saint lucia": "castries",
    "saint pierre and miquelon": "saint-pierre",
    "saint vincent and the grenadines": "kingstown",
    "samoa": "apia",
    "san marino": "san marino",
    "sao tome and principe": "são tomé",
    "saudi arabia": "riyadh",
    "scotland": "edinburgh",
    "senegal": "dakar",
    "serbia": "belgrade",
    "seychelles": "victoria",
    "sierra leone": "freetown",
    "singapore": "singapore",
    "slovakia": "bratislava",
    "slovenia": "ljubljana",
    "solomon islands": "honiara",
    "somalia": "mogadishu",
    "south africa": "pretoria",
    "south georgia and the south sandwich islands": "no city",
    "south korea": "seoul",
    "south sudan": "juba",
    "spain": "madrid",
    "sri lanka": "colombo, sri jayawardenepura kotte",
    "sudan": "khartum",
    "suriname": "paramaribo",
    "svalbard and jan mayen": "longyearbyen",
    "sweden": "stockholm",
    "switzerland": "bern",
    "syria": "damascus",
    "tajikistan": "dushanbe",
    "tanzania": "dodoma",
    "thailand": "bangkok",
    "the democratic republic of congo": "kinshasa",
    "togo": "lomé",
    "tokelau": "fakaofo",
    "tonga": "nuku'alofa",
    "trinidad and tobago": "port-of-spain",
    "tunisia": "tunis",
    "turkey": "ankara",
    "turkmenistan": "ashgabat",
    "turks and caicos islands": "cockburn town",
    "tuvalu": "funafuti",
    "uganda": "kampala",
    "ukraine": "kyiv",
    "united arab emirates": "abu dhabi",
    "united kingdom": "london",
    "united states": "washington",
    "uruguay": "montevideo",
    "uzbekistan": "toskent",
    "vanuatu": "port-vila",
    "venezuela": "caracas",
    "vetican city": "vetican city",
    "vietnam": "hanoi",
    "virgin islands, british": "road town",
    "virgin islands, u.s.": "charlotte amalie",
    "wales": "cardiff",
    "wallis and futuna": "mata-utu",
    "western sahara": "el-aai",
    "yemen": "sanaa",
    "zambia": "lusaka",
    "zimbabwe": "harare"
        
    


}


# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("How can I assist you?")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech recognition service is down.")
        return ""

# Process command
def process_command(command):
    if "capital of" in command:
        country = command.split("capital of")[-1].strip()
        capital = country_capitals.get(country.lower(), None)
        if capital:
            speak(f"The capital of {country.title()} is {capital}.")
        else:
            speak(f"Sorry, I don't know the capital of {country}.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye, Sir.")
        exit()
    else:
        speak("I can only tell you capitals of countries right now.")

# Display image-based UI instead of webcam
def face_ui():
    url = "https://imgcdn.stablediffusionweb.com/2024/11/19/28a9ed03-01c8-428f-a2d1-10031b79ffc9.jpg"
    try:
        resp = urllib.request.urlopen(url)
        image_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (600, 600))

        while True:
            cv2.imshow("JARVIS Interface", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
    except Exception as e:
        print("Error loading image:", e)
        speak("Error loading interface image.")

# Run everything
def run_jarvis():
    threading.Thread(target=face_ui, daemon=True).start()
    time.sleep(2)
    speak("JARVIS online.")
    while True:
        command = listen_command()
        process_command(command)

if __name__ == "__main__":
    run_jarvis()
