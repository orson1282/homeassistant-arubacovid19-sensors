# UPDATE 4/13/2020: The sensor is broken as the government changed the website to use an image instead of text. Therefore the values cannot be scraped anymore. I will try to work on a way to recognize the text, but I don't know how long that will take.


# Home Assistant - Aruba COVID19 Sensors

A command line sensor created for Home Assistant that scrapes the data from the official website of the [Aruban Government](https://www.arubacovid19.org/).

**Note:** This is a work in progress and they keep changing the website, I will update the script as soon I catch the new changes to the website. If you catch them before I do, please submit an issue.

## How to use
Place the arubacovid19.py file somewhere inside your Home Assistant Config folder. In this example it will be placed in `config\custom_sensors\`


## Example Sensor Yaml Config
```
sensor:
  - platform: command_line
    name: Aruba COVID19 - Activo
    command: "python3 /config/custom_sensors/arubacovid19.py"
    scan_interval: 30
    value_template: '{{ value_json.activo }}'
    unit_of_measurement: "hende"
  - platform: command_line
    name: Aruba COVID19 - Positivo
    command: "python3 /config/custom_sensors/arubacovid19.py"
    scan_interval: 30
    value_template: '{{ value_json.positivo }}'
    unit_of_measurement: "hende"
  - platform: command_line
    name: Aruba COVID19 - Morto
    command: "python3 /config/custom_sensors/arubacovid19.py"
    scan_interval: 30
    value_template: '{{ value_json.morto }}'
    unit_of_measurement: "hende"
  - platform: command_line
    name: Aruba COVID19 - Recupera
    command: "python3 /config/custom_sensors/arubacovid19.py"
    scan_interval: 30
    value_template: '{{ value_json.recupera }}'
    unit_of_measurement: "hende"
```
