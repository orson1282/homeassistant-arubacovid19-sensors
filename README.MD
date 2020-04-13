# Home Assistant - Aruba COVID19 Sensors

A command line sensor I created for Home Assistant that scrapes the data from ~~the official website of the [Aruban Government](https://www.arubacovid19.org/).~~ the [epidemic-stats](https://epidemic-stats.com/coronavirus/aruba) website

**Note:** This is a work in progress and if anything changes on the website, the sensor will break.

**Update April 13, 2020:** the official website of the [Aruban Government](https://www.arubacovid19.org/) decided to use an image to puublish the stats instead of text, so I am now unable to scrape the data from there, the new site I'm scraping data from may be a bit slower to update.

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
