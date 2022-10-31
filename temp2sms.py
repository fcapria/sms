#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A script theat reads temperature from a DS18B20 sensor
# Run as a cron job daily to verify temp.py warnings will be sent

from w1thermsensor import W1ThermSensor

# Fill in Twilio supplied credentials
from twilio_creds import twilioSID, twilioToken, fromNumber, toNumber
# Install Twilio's python library
from twilio.rest import Client

from IoTlib import c2f

#read the temperature from the sensor
sensor = W1ThermSensor()
temperature = c2f(sensor.get_temperature())

# Send Twilio noticifation
client = Client(twilioSID, twilioToken)
message = client.messages.create(
    to = toNumber,
    from_ = fromNumber,
    body = 'Studio temperature is ' + temperature)
