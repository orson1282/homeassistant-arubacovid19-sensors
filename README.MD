# Home Assistant - Aruba COVID19 Sensors

A command line sensor created for Home Assistant that scrapes the data from the official website of the [Aruban Government](https://www.arubacovid19.org/).

## How to use
Place the arubacovid19.py file somewhere inside your Home Assistant Config folder. In this example it will be placed in `config\custom_sensors\`


## Example Sensor Yaml Config
```
sensor:
  - platform: command_line
    name: Aruba COVID19 - Positivo
    command: "python3 /config/custom_sensors/arubacovid19.py"
    scan_interval: 30
    value_template: '{{ value_json.positivo }}'
  - platform: command_line
    name: Aruba COVID19 - Morto
    command: "python3 /config/custom_sensors/arubacovid19.py"
    scan_interval: 30
    value_template: '{{ value_json.morto }}'
  - platform: command_line
    name: Aruba COVID19 - Recupera
    command: "python3 /config/custom_sensors/arubacovid19.py"
    scan_interval: 30
    value_template: '{{ value_json.recupera }}'
```