# Home Assistant - Aruba COVID19 Sensors

A command line sensor I created for Home Assistant that scrapes the data from ~~the official website of the [Aruban Government](https://www.arubacovid19.org/).~~ the [epidemic-stats](https://epidemic-stats.com/coronavirus/aruba) website

**Note:** This is a work in progress and if anything changes on the website, the sensor will break.

**Update April 13, 2020:** the official website of the [Aruban Government](https://www.arubacovid19.org/) decided to use an image to puublish the stats instead of text, so I am now unable to scrape the data from there, the new site I'm scraping data from may be a bit slower to update.

**Second update April 13, 2020:** The way the sensors were setup it meant that they would query the server every 30 seconds per sensor, which translates to allot of traffic.
With this new update I decided to it would be best to create 1 sensor that queries the server once (every 30 seconds) and each of the other sensors query get their state from that first sensor, so they don't need to overload the server with too much traffic. I also changed the sensor names to english. ***Please update your config!***


## How to use
Place the arubacovid19.py file somewhere inside your Home Assistant Config folder. In this example it will be placed in `config\custom_sensors\`


## Example Home Assistant configuration.yaml
```
sensor:
  - platform: command_line
    name: Aruba COVID19
    json_attributes:
      - active
      - infected
      - deaths
      - recovered
    command: "python3 /config/custom_sensors/arubacovid19.py"
    scan_interval: 30

  - platform: template
    sensors:
      aruba_covid19_active:
        friendly_name: Aruba COVID19 - Active
        value_template: "{{ state_attr('sensor.aruba_covid19', 'active') }}"
        unit_of_measurement: "people"
        icon_template: mdi:emoticon-neutral-outline

      aruba_covid19_infected:
        friendly_name: Aruba COVID19 - Infected
        value_template: "{{ state_attr('sensor.aruba_covid19', 'infected') }}"
        unit_of_measurement: "people"
        icon_template: mdi:emoticon-cry-outline

      aruba_covid19_recovered:
        friendly_name: Aruba COVID19 - Recovered
        value_template: "{{ state_attr('sensor.aruba_covid19', 'recovered') }}"
        unit_of_measurement: "people"
        icon_template: mdi:emoticon-happy-outline

      aruba_covid19_deaths:
        friendly_name: Aruba COVID19 - Deaths
        value_template: "{{ state_attr('sensor.aruba_covid19', 'deaths') }}"
        unit_of_measurement: "people"
        icon_template: mdi:emoticon-cry-outline
```
