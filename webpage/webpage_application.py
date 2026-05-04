import network
import time
from microdot_libraries.microdot import Microdot , Response
from microdot_libraries.utemplate import Template
import os

SSID: str = "Matko-wifi"
PASSWORD: str = "876543210"

# Creating Wi-Fi network

nic: network.WLAN = network.WLAN(network.AP_IF)
nic.active(False)
time.sleep(1)
nic.active(True)

nic.config(
    essid=SSID,
    password=PASSWORD,
    authmode=network.AUTH_WPA2_PSK,
)

# wait until the AP initializes
time.sleep(1)

print("AP running:", nic.active())
print("Config:", nic.ifconfig())

# Connecting to Wi-Fi network

# nic: network.WLAN = network.WLAN(network.STA_IF)
# nic.active(False)
# time.sleep(1)
# nic.active(True)
#
# nic.connect(SSID, PASSWORD)
#
# while True:
#     status: list[int] = nic.status()
#     if status == network.STAT_GOT_IP:
#         print("Connected!")
#         print("Network config:", nic.ifconfig())
#         break
#
#     if status in (network.STAT_WRONG_PASSWORD,
#                   network.STAT_NO_AP_FOUND,
#                   network.STAT_CONNECT_FAIL):
#         print("Connection failed, status:", status)
#         sys.exit(0)
#
#     print("Connecting... status:", status)
#     time.sleep(1)

# MicroDot webpage server code

WEBPAGE_NAME: str = "testing_webpage"

app: Microdot = Microdot()

os.chdir('templates')

try:
    os.remove(WEBPAGE_NAME + "_html.py")
except OSError as e:
    print(e)

os.chdir('/')

webpage:Template = Template(WEBPAGE_NAME + ".html")

Response.default_content_type = "text/html"




# Declaring dictionaries containing the webpage variables.
webpage_variables_text: dict[str,str] = {
    "parameter_1": "CAT",
    "parameter_2": "MOUSE",
}

webpage_variables_radio_buttons: dict[str,str] = {
    "fplf_html": "checked",
    "fplf_css": "",
    "fplf_cpp": "",
}

webpage_variables_switch_buttons: dict[str,str] = {
    "led_checked": "",
}

webpage_variables_slider: dict[str,str] = {
    "pwm_value": "0",
}

webpage_variables_dropdown_menu: dict[str, str] = {
    "mode_auto": "",
    "mode_manual": "selected",
    "mode_off": "",
}

webpage_variables_progress_bar: dict[str, str] = {
    "progress": "0"
}

def generate_webpage():
    global webpage_variables_text
    global webpage_variables_radio_buttons
    global webpage_variables_switch_buttons
    global webpage_variables_slider
    global webpage_variables_dropdown_menu
    global webpage_variables_progress_bar

    # add to the created dictionary params all the dictionaries used for storing webpage variables
    # together with their keywords used in the HTML code for their accessing.
    params: dict[str, dict] = {
        "text": webpage_variables_text,
        "radio": webpage_variables_radio_buttons,
        "switch": webpage_variables_switch_buttons,
        "sliders": webpage_variables_slider,
        "dropdown": webpage_variables_dropdown_menu,
        "progress": webpage_variables_progress_bar,
    }

    return webpage.render(params=params)


# button press reaction
@app.route('/button_1', methods=['POST'])
async def button_press(request):
    global webpage_variables_text
    print("Button was pressed")
    webpage_variables_text["parameter_1"] = "someone pressed button"
    return Response(generate_webpage())

# data file reaction
@app.route('/data_field_1', methods=['POST'])
async def data_field_entered(request):
    global webpage_variables_text
    name: str = request.form.get("name","")
    print(f"User entered text to the text field: {name}")
    webpage_variables_text["parameter_1"] = "someone entered text"
    return Response(generate_webpage())

# radio buttons reaction
@app.route('/fplf', methods=['POST'])
async def favorite_programing_language_chosen(request):
    global webpage_variables_text
    global webpage_variables_radio_buttons
    programing_language: str = request.form.get("fav_lang", "")
    print(f"Favourite programming language was chosen: {programing_language}")
    for key in webpage_variables_radio_buttons:
        webpage_variables_radio_buttons[key] = ""
    webpage_variables_text["parameter_1"] = "someone chose a radio button"
    if programing_language == "HTML":
        webpage_variables_radio_buttons["fplf_html"] = "checked"
    elif programing_language == "CSS":
        webpage_variables_radio_buttons["fplf_css"] = "checked"
    elif programing_language == "CPP":
        webpage_variables_radio_buttons["fplf_cpp"] = "checked"
    return Response(generate_webpage())

# switch button reaction
@app.route('/switch_button', methods=['POST'])
async def switch_button(request):
    global webpage_variables_text
    global webpage_variables_switch_buttons
    button_name: str = request.form.get("led", "")
    print(f"Switch button was pressed: {button_name}")
    webpage_variables_text["parameter_1"] = "someone choose a switch button"
    if button_name == "on":
        webpage_variables_switch_buttons["led_checked"] = "checked"
    else:
        webpage_variables_switch_buttons["led_checked"] = ""
    return Response(generate_webpage())

# slider reaction
@app.route('/slider', methods=['POST'])
async def slider(request):
    global webpage_variables_text
    global webpage_variables_slider
    slider_value: str = request.form.get("pwm", "0")
    print(f"Slider was used: {slider_value}")
    webpage_variables_text["parameter_1"] = "someone use a slider"
    webpage_variables_slider["pwm_value"] = slider_value
    return Response(generate_webpage())

# dropdown menu reaction
@app.route('/dropdown_menu', methods=['POST'])
async def dropdown_menu(request):
    global webpage_variables_text
    global webpage_variables_dropdown_menu
    dropdown_value: str = request.form.get("mode", "")
    print(f"Dropdown menu was used: {dropdown_value}")
    webpage_variables_text["parameter_1"] = "someone use a dropdown menu"
    for key in webpage_variables_dropdown_menu:
        webpage_variables_dropdown_menu[key] = ""
    if dropdown_value == "auto":
        webpage_variables_dropdown_menu["mode_auto"] = "selected"
    elif dropdown_value == "manual":
        webpage_variables_dropdown_menu["mode_manual"] = "selected"
    elif dropdown_value == "off":
        webpage_variables_dropdown_menu["mode_off"] = "selected"
    return Response(generate_webpage())

# progress bar reaction
@app.route('/progress_bar', methods=['POST'])
async def progress_bar(request):
    global webpage_variables_progress_bar
    global webpage_variables_slider
    webpage_variables_progress_bar["progress"] = webpage_variables_slider["pwm_value"]
    return Response(generate_webpage())







# These two routes and starting the web server must be always present

# loading the CSS file by the webpage
@app.route('/style.css')
async def style(request):
    # with open('./templates/' + WEBPAGE_NAME + '.css') as f:
    #     css = f.read()
    # return Response(css, headers={'Content-Type': 'text/css'})

    with open('./templates/' + WEBPAGE_NAME + '_green.css') as f:
        css = f.read()
    return Response(css, headers={'Content-Type': 'text/css'})

# original webpage
@app.route("/")
async def index(request):
    return Response(generate_webpage())

app.run(port=80)